// Self-hosted direct download component for TchueKAM Agent.
//
// Desktop installers: direct root static installer endpoints (single source of truth).
// Android: the APK attached to a GitHub release; see downloads.ts for how its
//          availability is checked, so the page never offers a dead link.
// Web:     the hosted web app, which also installs to a phone's home screen.

import React, {useEffect, useState} from 'react';
import Link from '@docusaurus/Link';
import {
  ANDROID_APK_NAME,
  MOBILE_GUIDE_PATH,
  WEB_APP_URL,
  detectOS,
  isApkDownloadable,
  track,
  trackDownload,
  useAndroidApk,
} from './downloads';
import type {AndroidApk, OS} from './downloads';

type DesktopOS = 'windows' | 'macos-arm64' | 'macos-x64' | 'linux';

const DIRECT_DOWNLOADS: Record<DesktopOS, {url: string; filename: string; label: string; type: string}> = {
  'windows': {
    url: '/TchueKAM-Setup.exe',
    filename: 'TchueKAM-Setup.exe',
    label: 'Windows (64-bit)',
    type: '.exe installer',
  },
  'macos-arm64': {
    url: '/TchueKAM-Mac-arm64.dmg',
    filename: 'TchueKAM-Mac-arm64.dmg',
    label: 'macOS (Apple Silicon)',
    type: '.dmg',
  },
  'macos-x64': {
    url: '/TchueKAM-Mac-x64.dmg',
    filename: 'TchueKAM-Mac-x64.dmg',
    label: 'macOS (Intel)',
    type: '.dmg',
  },
  'linux': {
    url: '/TchueKAM-Linux.AppImage',
    filename: 'TchueKAM-Linux.AppImage',
    label: 'Linux',
    type: '.AppImage',
  },
};

// Short platform name for the primary button, e.g. "Download for macOS".
const DESKTOP_NAME: Record<DesktopOS, string> = {
  'windows': 'Windows',
  'macos-arm64': 'macOS',
  'macos-x64': 'macOS',
  'linux': 'Linux',
};

interface Cta {
  href: string;
  label: string;
  /** Present for same-origin file downloads only. */
  download?: string;
  /** Opens another site (the web app) in a new tab. */
  external?: boolean;
  onClick: () => void;
}

// The one button the visitor most likely wants, based on what they are using.
function primaryCta(os: OS, apk: AndroidApk): Cta {
  if (os === 'android' && isApkDownloadable(apk)) {
    return {
      href: apk.url,
      label: '⬇ Download for Android',
      onClick: () => trackDownload(ANDROID_APK_NAME, apk.url, 'android', apk.version),
    };
  }
  // iPhone/iPad have no installer, and an Android visitor has nothing to download
  // until the APK is published. The web app works on both today.
  if (os === 'android' || os === 'ios') {
    return {
      href: WEB_APP_URL,
      label: '🌐 Open the Web App',
      external: true,
      onClick: () => track('web_app_opened', {os}),
    };
  }
  const direct = DIRECT_DOWNLOADS[os];
  return {
    href: direct.url,
    download: direct.filename,
    label: `⬇ Download for ${DESKTOP_NAME[os]}`,
    onClick: () => trackDownload(direct.filename, direct.url, os, 'v1.0.0'),
  };
}

const linkStyle: React.CSSProperties = {color: '#00F2FE', fontWeight: 600, textDecoration: 'none'};

// Notes under the table wrap to the card's width (set by the buttons and the table) instead of
// stretching the card to fit one long line. `width: 0` removes the text from the card's natural
// width; `min-width: 100%` then fills whatever width the card ended up with.
const wrapToCard: React.CSSProperties = {width: 0, minWidth: '100%'};

// One row of the platform table. The file type is rendered twice on purpose: in its own column
// for wide screens, and under the platform name on phones (where that column is hidden - see
// custom.css) so the download link in the last column is never clipped.
function PlatformRow({label, type, size, children}: {label: string; type: string; size?: string; children: React.ReactNode}) {
  return (
    <tr>
      <td>
        <strong>{label}</strong>
        <span className="tchuekam-dl-type-inline">{size ? `${type} · ${size}` : type}</span>
      </td>
      <td className="tchuekam-dl-type">
        <code>{type}</code>
        {size && <span style={{opacity: 0.6, fontSize: 12, marginLeft: 6}}>{size}</span>}
      </td>
      <td>{children}</td>
    </tr>
  );
}

export function StaticDownloadSection() {
  const [os, setOS] = useState<OS>('windows');
  const apk = useAndroidApk();

  useEffect(() => {
    setOS(detectOS());
  }, []);

  const apkReady = isApkDownloadable(apk);
  const primary = primaryCta(os, apk);

  return (
    <div style={{padding: '1.5rem', border: '1px solid rgba(0,242,254,0.15)', borderRadius: 12, background: 'rgba(0,242,254,0.04)', minWidth: 0, maxWidth: '100%', boxSizing: 'border-box'}}>
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
          v1.0.0
        </span>
        <span style={{opacity: 0.6, fontSize: 14}}>
          Latest release
        </span>
      </div>

      <p style={{margin: '0 0 16px', opacity: 0.85, lineHeight: 1.6}}>
        Download TchueKAM Agent for your platform:
      </p>

      <div className="tchuekam-cta-row" style={{display: 'flex', gap: 12, flexWrap: 'wrap', marginBottom: 16}}>
        <a
          href={primary.href}
          download={primary.download}
          {...(primary.external ? {target: '_blank', rel: 'noopener noreferrer'} : {})}
          className="button button--primary button--lg tchuekam-cta"
          onClick={primary.onClick}
          style={{textDecoration: 'none', background: '#00E5FF', color: '#07070d', fontWeight: 700}}
        >
          {primary.label}
        </a>

        {primary.external ? (
          <Link to={MOBILE_GUIDE_PATH} className="button button--lg tchuekam-cta tchuekam-cta-secondary">
            📱 Add to home screen
          </Link>
        ) : (
          <a
            href={WEB_APP_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="button button--lg tchuekam-cta tchuekam-cta-secondary"
            onClick={() => track('web_app_opened', {os})}
          >
            🌐 Open the Web App
          </a>
        )}
      </div>

      <table className="tchuekam-dl-table">
        <thead>
          <tr>
            <th>Platform</th>
            <th className="tchuekam-dl-type">File type</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(DIRECT_DOWNLOADS).map(([key, item]) => (
            <PlatformRow key={key} label={item.label} type={item.type}>
              <a
                href={item.url}
                download={item.filename}
                onClick={() => trackDownload(item.filename, item.url, key, 'v1.0.0')}
                style={linkStyle}
              >
                Download →
              </a>
            </PlatformRow>
          ))}

          <PlatformRow label="Android" type=".apk" size={apk.status === 'available' ? apk.size : undefined}>
            {apkReady ? (
              <a
                href={apk.url}
                onClick={() => trackDownload(ANDROID_APK_NAME, apk.url, 'android', apk.version)}
                style={linkStyle}
              >
                Download →
              </a>
            ) : (
              <span style={{opacity: 0.6, fontWeight: 600}} title="The Android app is being published">
                Coming soon
              </span>
            )}
          </PlatformRow>
          <PlatformRow label={'iPhone & iPad'} type="Web app (PWA)">
            <Link to={MOBILE_GUIDE_PATH} style={linkStyle}>
              Install guide →
            </Link>
          </PlatformRow>
          <PlatformRow label="Web" type="Any modern browser">
            <a
              href={WEB_APP_URL}
              target="_blank"
              rel="noopener noreferrer"
              onClick={() => track('web_app_opened', {os: 'web'})}
              style={linkStyle}
            >
              Open Web App →
            </a>
          </PlatformRow>
        </tbody>
      </table>

      {apk.status === 'unpublished' && (
        <p style={{margin: '12px 0 0', fontSize: 13, lineHeight: 1.6, ...wrapToCard}}>
          The Android app is being published. The Web App already runs on your phone — see the{' '}
          <Link to={MOBILE_GUIDE_PATH}>install guide</Link> to add it to your home screen.
        </p>
      )}

      <p style={{opacity: 0.6, fontSize: 13, marginTop: 12, ...wrapToCard}}>
        All downloads are verified and hosted directly by TchueKAM.
        {apkReady && ' On Android, your phone asks once to allow installs from your browser, because the app is distributed outside the Play Store.'}
      </p>
    </div>
  );
}

export default function LatestRelease({showAllPlatforms = false}: {showAllPlatforms?: boolean}) {
  return <StaticDownloadSection />;
}
