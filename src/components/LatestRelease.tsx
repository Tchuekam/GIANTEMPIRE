// Download component for TchueKAM Agent.
//
// Desktop installers: the assets attached to a published GitHub release.
//          They used to be static files under static/, which is how the site
//          came to serve a 66-byte text file named TchueKAM-Setup.exe and
//          Windows answered "This app can't run on your PC" for every visitor.
//          Resolving them from the release means the page cannot offer an
//          installer that does not exist.
// Android: the APK attached to a GitHub release; see downloads.ts for how its
//          availability is checked, so the page never offers a dead link.
// Web:     the hosted web app, which also installs to a phone's home screen.

import React, {useEffect, useState} from 'react';
import Link from '@docusaurus/Link';
import {
  ANDROID_APK_NAME,
  DESKTOP_ASSETS,
  MOBILE_GUIDE_PATH,
  WEB_APP_URL,
  detectOS,
  isApkDownloadable,
  isWebAppAvailable,
  track,
  trackDownload,
  useAndroidApk,
  useDesktopDownloads,
  useWebApp,
} from './downloads';
import type {AndroidApk, DesktopDownloads, DesktopOS, OS} from './downloads';

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

// The one button the visitor most likely wants, based on what they are using. Null means a phone
// visitor with nothing to offer yet (no APK published and the web app unreachable).
function primaryCta(os: OS, apk: AndroidApk, webReady: boolean, desktop: DesktopDownloads): Cta | null {
  if (os === 'android' && isApkDownloadable(apk)) {
    return {
      href: apk.url,
      label: '⬇ Download for Android',
      onClick: () => trackDownload(ANDROID_APK_NAME, apk.url, 'android', apk.version),
    };
  }
  // iPhone/iPad have no installer, and an Android visitor has nothing to download
  // until the APK is published. The web app covers both, as long as it is reachable.
  if (os === 'android' || os === 'ios') {
    if (!webReady) return null;
    return {
      href: WEB_APP_URL,
      label: '🌐 Open the Web App',
      external: true,
      onClick: () => track('web_app_opened', {os}),
    };
  }
  // Offer this visitor's own installer when the release carries it. We do not
  // fall back to another platform's build: handing a Mac user a .exe is a
  // worse answer than telling them it is not ready.
  const spec = DESKTOP_ASSETS[os];
  const asset = desktop.assets[os];
  if (!spec || !asset) return null;
  return {
    href: asset.url,
    label: `⬇ Download for ${DESKTOP_NAME[os]}${asset.size ? ` (${asset.size})` : ''}`,
    onClick: () => trackDownload(spec.filename, asset.url, os, desktop.version),
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

function ComingSoon() {
  return <span style={{opacity: 0.6, fontWeight: 600}}>Coming soon</span>;
}

export function StaticDownloadSection() {
  const [os, setOS] = useState<OS>('windows');
  const apk = useAndroidApk();
  const web = useWebApp();
  const desktop = useDesktopDownloads();

  useEffect(() => {
    setOS(detectOS());
  }, []);

  const apkReady = isApkDownloadable(apk);
  const webReady = isWebAppAvailable(web);
  const primary = primaryCta(os, apk, webReady, desktop);
  const desktopSpec = DESKTOP_ASSETS[os as DesktopOS];

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
          {desktop.version ?? (desktop.status === 'checking' ? '…' : '—')}
        </span>
        <span style={{opacity: 0.6, fontSize: 14}}>
          Latest release
        </span>
      </div>

      <p style={{margin: '0 0 16px', opacity: 0.85, lineHeight: 1.6}}>
        Download TchueKAM Agent for your platform:
      </p>

      <div className="tchuekam-cta-row" style={{display: 'flex', gap: 12, flexWrap: 'wrap', marginBottom: 16}}>
        {primary ? (
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
        ) : (
          <span
            className="button button--lg tchuekam-cta tchuekam-cta-secondary tchuekam-cta-disabled"
            aria-disabled="true"
          >
            {desktopSpec
              ? `${desktopSpec.label} build coming soon`
              : '📱 Mobile app coming soon'}
          </span>
        )}

        {primary?.external ? (
          <Link to={MOBILE_GUIDE_PATH} className="button button--lg tchuekam-cta tchuekam-cta-secondary">
            📱 Add to home screen
          </Link>
        ) : webReady ? (
          <a
            href={WEB_APP_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="button button--lg tchuekam-cta tchuekam-cta-secondary"
            onClick={() => track('web_app_opened', {os})}
          >
            🌐 Open the Web App
          </a>
        ) : null}
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
          {(Object.keys(DESKTOP_ASSETS) as DesktopOS[]).map((key) => {
            const spec = DESKTOP_ASSETS[key];
            const asset = desktop.assets[key];
            return (
              <PlatformRow key={key} label={spec.label} type={spec.type} size={asset?.size}>
                {asset ? (
                  <a
                    href={asset.url}
                    onClick={() => trackDownload(spec.filename, asset.url, key, desktop.version)}
                    style={linkStyle}
                  >
                    Download →
                  </a>
                ) : (
                  <ComingSoon />
                )}
              </PlatformRow>
            );
          })}

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
              <ComingSoon />
            )}
          </PlatformRow>
          <PlatformRow label={'iPhone & iPad'} type="Web app (PWA)">
            {webReady ? (
              <Link to={MOBILE_GUIDE_PATH} style={linkStyle}>
                Install guide →
              </Link>
            ) : (
              <ComingSoon />
            )}
          </PlatformRow>
          <PlatformRow label="Web" type="Any modern browser">
            {webReady ? (
              <a
                href={WEB_APP_URL}
                target="_blank"
                rel="noopener noreferrer"
                onClick={() => track('web_app_opened', {os: 'web'})}
                style={linkStyle}
              >
                Open Web App →
              </a>
            ) : (
              <ComingSoon />
            )}
          </PlatformRow>
        </tbody>
      </table>

      {apk.status === 'unpublished' && (
        <p style={{margin: '12px 0 0', fontSize: 13, lineHeight: 1.6, ...wrapToCard}}>
          {webReady ? (
            <>
              The Android app is being published. The Web App already runs on your phone — see the{' '}
              <Link to={MOBILE_GUIDE_PATH}>install guide</Link> to add it to your home screen.
            </>
          ) : (
            'The Android app and the Web App are being published.'
          )}
        </p>
      )}

      <p style={{opacity: 0.6, fontSize: 13, marginTop: 12, ...wrapToCard}}>
        Every installer is published as a release asset and checked for a valid
        executable header and realistic size before release.
        {apkReady && ' On Android, your phone asks once to allow installs from your browser, because the app is distributed outside the Play Store.'}
      </p>
    </div>
  );
}

export default function LatestRelease({showAllPlatforms = false}: {showAllPlatforms?: boolean}) {
  return <StaticDownloadSection />;
}
