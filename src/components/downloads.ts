// Shared pieces of the download experience: which platform the visitor is on,
// where the web app lives, and whether the Android APK has actually been
// published yet.
//
// The desktop installers are static files (see LatestRelease.tsx). The Android
// APK is different: it is an asset on a GitHub release of the public app repo,
// and it may not be attached yet. Rather than hard-code a link that can 404,
// the hook below asks GitHub which release carries it and lets the page say
// "coming soon" until it exists. Attaching the APK to a release is then all it
// takes to turn the download on - no site change, no redeploy.

import {useEffect, useState} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

/** The hosted web app. Opens in any browser, and can be added to a phone's home screen. */
export const WEB_APP_URL = 'https://agent.tchuekam.com';

/** Install guide for the web app (PWA) and the Android APK. */
export const MOBILE_GUIDE_PATH = '/mobile-companion';

/**
 * File name the APK must carry on the GitHub release. It is the name the app
 * itself uses for its in-app "Download APK" links (/api/download/android), so a
 * single upload makes the website and the app's own links work together.
 */
export const ANDROID_APK_NAME = 'TchueKAM-Mobile.apk';

/** Used only if siteConfig.customFields.githubRepo is ever removed. */
const DEFAULT_REPO = 'Tchuekam/tchuekam-desktop';

export type OS = 'windows' | 'macos-arm64' | 'macos-x64' | 'linux' | 'android' | 'ios';

export function detectOS(): OS {
  if (typeof navigator === 'undefined') return 'windows';
  const ua = navigator.userAgent || '';
  const plat = (navigator.platform || '').toLowerCase();

  // Phones and tablets first. Android reports "Linux" in both its user agent and
  // its platform, and iPadOS 13+ asks for the desktop site by default, so it
  // calls itself a Mac - a touch screen is what gives it away.
  if (/android/i.test(ua)) return 'android';
  if (/iphone|ipad|ipod/i.test(ua) || (plat === 'macintel' && (navigator.maxTouchPoints || 0) > 1)) return 'ios';

  if (/win/.test(plat) || /Windows/i.test(ua)) return 'windows';
  if (/mac/.test(plat) || /Mac OS/i.test(ua)) {
    if (/arm|aarch64|Apple M/i.test(ua)) return 'macos-arm64';
    return 'macos-x64';
  }
  if (/linux/.test(plat) || /Linux/i.test(ua)) return 'linux';
  return 'windows';
}

export interface AndroidApk {
  /**
   * checking    - first paint, lookup in flight
   * available   - a published release carries the APK
   * unpublished - GitHub answered and no published release carries it
   * unknown     - the lookup failed (offline, rate limited); we cannot tell
   */
  status: 'checking' | 'available' | 'unpublished' | 'unknown';
  /** Where the download button should point. */
  url: string;
  /** Release tag the APK is attached to, e.g. "v1.0.0". */
  version?: string;
  /** Human readable size, e.g. "62.4 MB". */
  size?: string;
  /** Hex SHA-256 of the APK, when GitHub reports one. */
  sha256?: string;
}

/** Only an actual "no APK anywhere" answer may hide the download. Not knowing must not. */
export function isApkDownloadable(apk: AndroidApk): boolean {
  return apk.status !== 'unpublished';
}

interface GhAsset {
  name?: string;
  size?: number;
  browser_download_url?: string;
  digest?: string;
}

interface GhRelease {
  tag_name?: string;
  draft?: boolean;
  prerelease?: boolean;
  assets?: GhAsset[];
}

function formatBytes(bytes?: number): string | undefined {
  if (!bytes || bytes <= 0) return undefined;
  if (bytes >= 1024 * 1024) return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
  return `${Math.max(1, Math.round(bytes / 1024))} KB`;
}

/** GitHub resolves this to the asset on the *latest* release, and 404s if it is not there. */
export function apkFallbackUrl(repo: string): string {
  return `https://github.com/${repo}/releases/latest/download/${ANDROID_APK_NAME}`;
}

/**
 * Pick the newest published release that carries the APK.
 *
 * Searching the recent releases (instead of only the latest one) lets the
 * desktop app ship new versions without dragging the APK along: the Android
 * build keeps working until a newer one is attached.
 */
export function findAndroidApk(releases: unknown, repo: string): AndroidApk {
  const fallback = apkFallbackUrl(repo);
  if (!Array.isArray(releases)) return {status: 'unknown', url: fallback};

  // Never put a URL on the page that does not point at this repo's release downloads.
  const trusted = `https://github.com/${repo}/releases/download/`;

  for (const release of releases as GhRelease[]) {
    if (!release || release.draft || release.prerelease) continue;
    const assets = Array.isArray(release.assets) ? release.assets : [];
    // Prefer the canonical name; accept any .apk so a differently named upload still works.
    const asset =
      assets.find((a) => a?.name === ANDROID_APK_NAME) ?? assets.find((a) => /\.apk$/i.test(a?.name ?? ''));
    const url = asset?.browser_download_url;
    if (asset && typeof url === 'string' && url.startsWith(trusted)) {
      return {
        status: 'available',
        url,
        version: release.tag_name,
        size: formatBytes(asset.size),
        sha256: asset.digest?.startsWith('sha256:') ? asset.digest.slice('sha256:'.length) : undefined,
      };
    }
  }
  return {status: 'unpublished', url: fallback};
}

const CACHE_TTL_MS = 10 * 60 * 1000;

function readCache(key: string): AndroidApk | null {
  try {
    const raw = window.sessionStorage.getItem(key);
    if (!raw) return null;
    const entry = JSON.parse(raw);
    if (typeof entry?.t !== 'number' || Date.now() - entry.t > CACHE_TTL_MS) return null;
    const apk = entry.apk;
    return apk && (apk.status === 'available' || apk.status === 'unpublished') && typeof apk.url === 'string'
      ? apk
      : null;
  } catch {
    return null; // storage can be blocked (private mode, sandboxed frames)
  }
}

function writeCache(key: string, apk: AndroidApk): void {
  try {
    window.sessionStorage.setItem(key, JSON.stringify({t: Date.now(), apk}));
  } catch {
    // Not worth failing over.
  }
}

/**
 * Whether the Android APK is published, and where to get it.
 *
 * Starts optimistic ("checking" still offers the download) so the server-rendered
 * page and a failed lookup both behave like a normal download link.
 */
export function useAndroidApk(): AndroidApk {
  const {siteConfig} = useDocusaurusContext();
  const repo = (siteConfig.customFields?.githubRepo as string | undefined) || DEFAULT_REPO;
  const [apk, setApk] = useState<AndroidApk>({status: 'checking', url: apkFallbackUrl(repo)});

  useEffect(() => {
    let cancelled = false;
    const cacheKey = `tchuekam_android_apk_v1:${repo}`;

    const cached = readCache(cacheKey);
    if (cached) {
      setApk(cached);
      return undefined;
    }

    fetch(`https://api.github.com/repos/${repo}/releases?per_page=30`, {
      headers: {Accept: 'application/vnd.github+json'},
    })
      .then((res) => (res.ok ? res.json() : Promise.reject(new Error(String(res.status)))))
      .then((releases) => {
        const found = findAndroidApk(releases, repo);
        if (found.status === 'available' || found.status === 'unpublished') writeCache(cacheKey, found);
        if (!cancelled) setApk(found);
      })
      .catch(() => {
        if (!cancelled) setApk({status: 'unknown', url: apkFallbackUrl(repo)});
      });

    return () => {
      cancelled = true;
    };
  }, [repo]);

  return apk;
}

export function track(event: string, props: Record<string, unknown> = {}): void {
  try {
    if (typeof window !== 'undefined' && (window as any).posthog?.capture) {
      (window as any).posthog.capture(event, {source: 'docs_site', ...props});
    }
  } catch {
    // Analytics must never break a download.
  }
}

export function trackDownload(assetName: string, downloadUrl: string, targetOS: string, version: string = 'v1.0.0'): void {
  track('download_started', {os: targetOS, asset: assetName, version, download_url: downloadUrl});
}
