// Download section for the TchueKAM Agent desktop app.
//
// The installers are release assets on GitHub, so this component asks GitHub
// which release is current and links straight to the asset. It never links to a
// file hosted on this site: the previous version did, and the "installers" in
// static/ were 66-byte text placeholders, so every download saved a file named
// TchueKAM-Setup.exe that could not be opened.
//
// Without JavaScript, or when the GitHub API is unreachable or rate limited,
// every link falls back to the latest release page, which always works.

import React, {useEffect, useState} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

const DEFAULT_REPO = 'Tchuekam/tchuekam-desktop';
const CACHE_TTL_MS = 10 * 60 * 1000;

type OS = 'windows' | 'macos-arm64' | 'macos-x64' | 'linux';

interface Asset {
  name: string;
  size: number;
  browser_download_url: string;
}

interface Release {
  tag_name: string;
  published_at: string;
  html_url: string;
  assets: Asset[];
}

interface Platform {
  label: string;
  short: string;
  type: string;
  match: (name: string) => boolean;
}

const PLATFORMS: Record<OS, Platform> = {
  windows: {
    label: 'Windows (64-bit)',
    short: 'Windows',
    type: '.exe installer',
    match: (name) => /\.exe$/i.test(name),
  },
  'macos-arm64': {
    label: 'macOS (Apple Silicon)',
    short: 'macOS',
    type: '.dmg',
    match: (name) => /\.dmg$/i.test(name) && /(arm64|aarch64|universal)/i.test(name),
  },
  'macos-x64': {
    label: 'macOS (Intel)',
    short: 'macOS',
    type: '.dmg',
    match: (name) => /\.dmg$/i.test(name) && /(x64|x86_64|intel|universal)/i.test(name),
  },
  linux: {
    label: 'Linux',
    short: 'Linux',
    type: '.AppImage',
    match: (name) => /\.AppImage$/i.test(name),
  },
};

function detectOS(): OS {
  if (typeof navigator === 'undefined') return 'windows';
  const ua = navigator.userAgent || '';
  const plat = (navigator.platform || '').toLowerCase();
  if (/win/.test(plat) || /Windows/i.test(ua)) return 'windows';
  if (/mac/.test(plat) || /Mac OS/i.test(ua)) {
    if (/arm|aarch64|Apple M/i.test(ua)) return 'macos-arm64';
    return 'macos-x64';
  }
  if (/linux/.test(plat) || /Linux/i.test(ua)) return 'linux';
  return 'windows';
}

// Prefer an asset called "...Setup..." when a release carries several that
// match, so the NSIS installer wins over any stray .exe.
function findAsset(release: Release | null, os: OS): Asset | null {
  if (!release) return null;
  const matches = release.assets.filter((a) => PLATFORMS[os].match(a.name));
  return matches.find((a) => /setup/i.test(a.name)) || matches[0] || null;
}

function formatSize(bytes: number): string {
  return `${Math.round(bytes / (1024 * 1024))} MB`;
}

function readCache(key: string): Release | null {
  try {
    const raw = window.sessionStorage.getItem(key);
    if (!raw) return null;
    const {at, release} = JSON.parse(raw);
    return Date.now() - at < CACHE_TTL_MS ? release : null;
  } catch {
    return null;
  }
}

function writeCache(key: string, release: Release) {
  try {
    window.sessionStorage.setItem(key, JSON.stringify({at: Date.now(), release}));
  } catch {}
}

function trackDownload(assetName: string, downloadUrl: string, targetOS: string, version: string) {
  try {
    if (typeof window !== 'undefined' && (window as any).posthog?.capture) {
      (window as any).posthog.capture('download_started', {
        os: targetOS,
        asset: assetName,
        source: 'docs_site',
        version,
        download_url: downloadUrl,
      });
    }
  } catch {}
}

export function ReleaseDownloadSection() {
  const {siteConfig} = useDocusaurusContext();
  const repo = String(siteConfig.customFields?.githubRepo || DEFAULT_REPO);
  const releasesUrl = `https://github.com/${repo}/releases/latest`;

  const [os, setOS] = useState<OS>('windows');
  const [release, setRelease] = useState<Release | null>(null);

  useEffect(() => {
    setOS(detectOS());

    const cacheKey = `tchuekam-latest-release:${repo}`;
    const cached = readCache(cacheKey);
    if (cached) {
      setRelease(cached);
      return;
    }

    let cancelled = false;
    fetch(`https://api.github.com/repos/${repo}/releases/latest`, {
      headers: {Accept: 'application/vnd.github+json'},
    })
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status)))))
      .then((data: Release) => {
        if (cancelled) return;
        setRelease(data);
        writeCache(cacheKey, data);
      })
      .catch(() => {
        // Leave `release` null: every link below degrades to the release page.
      });
    return () => {
      cancelled = true;
    };
  }, [repo]);

  const version = release?.tag_name;
  // A browser can't tell Apple Silicon from Intel (both report "Intel Mac OS X"),
  // so on a Mac offer whichever build the release actually carries.
  const primaryAsset =
    findAsset(release, os) ||
    (os.startsWith('macos') ? findAsset(release, 'macos-arm64') || findAsset(release, 'macos-x64') : null);
  const primaryUrl = primaryAsset?.browser_download_url || release?.html_url || releasesUrl;
  // The only Mac build published so far is Apple Silicon; say so, because an
  // Intel Mac looks identical to the browser and cannot run it.
  const appleSilicon = os.startsWith('macos') && primaryAsset !== null && /arm64|aarch64/i.test(primaryAsset.name);
  const primaryLabel = primaryAsset
    ? `⬇ Download for ${PLATFORMS[os].short}${appleSilicon ? ' (Apple Silicon)' : ''}`
    : release
      ? `View ${PLATFORMS[os].short} downloads`
      : '⬇ Download';
  const released = release?.published_at
    ? new Date(release.published_at).toLocaleDateString(undefined, {year: 'numeric', month: 'long', day: 'numeric'})
    : null;

  return (
    <div style={{padding: '1.5rem', border: '1px solid rgba(0,242,254,0.15)', borderRadius: 12, background: 'rgba(0,242,254,0.04)'}}>
      <div style={{display: 'flex', alignItems: 'baseline', gap: 12, flexWrap: 'wrap', marginBottom: 16}}>
        <span style={{
          background: 'rgba(0,242,254,0.12)',
          color: '#00F2FE',
          padding: '4px 10px',
          borderRadius: 12,
          fontSize: 12,
          fontWeight: 600,
          letterSpacing: 0.5,
        }}>
          {version || 'Latest'}
        </span>
        <span style={{opacity: 0.6, fontSize: 14}}>
          Latest release{released ? ` · ${released}` : ''}
        </span>
      </div>

      <p style={{margin: '0 0 16px', opacity: 0.85, lineHeight: 1.6}}>
        Download TchueKAM Agent for your platform:
      </p>

      <div style={{display: 'flex', gap: 12, flexWrap: 'wrap', alignItems: 'center', marginBottom: 16}}>
        <a
          href={primaryUrl}
          className="button button--primary button--lg"
          onClick={() => primaryAsset && trackDownload(primaryAsset.name, primaryUrl, os, version || 'unknown')}
          style={{textDecoration: 'none', background: '#00E5FF', color: '#07070d', fontWeight: 700}}
        >
          {primaryLabel}
        </a>
        {primaryAsset && (
          <span style={{opacity: 0.55, fontSize: 13}}>
            {primaryAsset.name} · {formatSize(primaryAsset.size)}
          </span>
        )}
      </div>

      <table>
        <thead>
          <tr>
            <th>Platform</th>
            <th>File type</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {(Object.keys(PLATFORMS) as OS[]).map((key) => {
            const asset = findAsset(release, key);
            return (
              <tr key={key}>
                <td><strong>{PLATFORMS[key].label}</strong></td>
                <td><code>{PLATFORMS[key].type}</code></td>
                <td>
                  {asset ? (
                    <a
                      href={asset.browser_download_url}
                      onClick={() => trackDownload(asset.name, asset.browser_download_url, key, version || 'unknown')}
                      style={{color: '#00F2FE', fontWeight: 600, textDecoration: 'none'}}
                    >
                      Download →
                    </a>
                  ) : release ? (
                    <span style={{opacity: 0.5}}>Not in this release yet</span>
                  ) : (
                    <a href={releasesUrl} style={{color: '#00F2FE', fontWeight: 600, textDecoration: 'none'}}>
                      Releases →
                    </a>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>

      <p style={{opacity: 0.7, fontSize: 13, marginTop: 12, marginBottom: 0, lineHeight: 1.6}}>
        Windows may show <strong>“Windows protected your PC”</strong> because the installer is not
        code-signed yet. Choose <strong>More info → Run anyway</strong>. The first launch sets up
        the agent runtime, needs an internet connection and can take several minutes — keep the
        window open. Files are served by GitHub Releases; see{' '}
        <a href={releasesUrl} style={{color: '#00F2FE'}}>the release page</a> for checksums.
      </p>
    </div>
  );
}

export default function LatestRelease({showAllPlatforms = false}: {showAllPlatforms?: boolean}) {
  return <ReleaseDownloadSection />;
}
