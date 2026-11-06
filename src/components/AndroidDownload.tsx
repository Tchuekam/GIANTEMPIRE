// Download card for the TchueKAM Mobile Android app (APK), for the docs pages.
//
// Mirrors MagidaDownload.tsx. Whether the APK is published, and its version,
// size and checksum, come from the GitHub release it is attached to (see
// downloads.ts) - so this page can never advertise a download that is not there.

import React from 'react';
import Link from '@docusaurus/Link';
import {
  ANDROID_APK_NAME,
  MOBILE_GUIDE_PATH,
  WEB_APP_URL,
  isApkDownloadable,
  isWebAppAvailable,
  track,
  trackDownload,
  useAndroidApk,
  useWebApp,
} from './downloads';

const ACCENT = '#00F2FE';

function Spec({label, value}: {label: string; value: string}) {
  return (
    <div style={{minWidth: 0}}>
      <div style={{fontSize: 11, letterSpacing: 0.6, textTransform: 'uppercase', opacity: 0.5}}>{label}</div>
      <div style={{fontSize: 14, fontWeight: 600, marginTop: 2, wordBreak: 'break-all'}}>{value}</div>
    </div>
  );
}

export default function AndroidDownload() {
  const apk = useAndroidApk();
  const web = useWebApp();
  const ready = isApkDownloadable(apk);
  const webReady = isWebAppAvailable(web);

  const badge = apk.version ? apk.version : ready ? 'Latest' : 'Coming soon';

  return (
    <div
      style={{
        padding: '1.75rem',
        border: `1px solid ${ACCENT}26`,
        borderRadius: 14,
        background: `linear-gradient(180deg, ${ACCENT}0F 0%, ${ACCENT}05 100%)`,
      }}
    >
      <div style={{display: 'flex', alignItems: 'baseline', gap: 12, flexWrap: 'wrap', marginBottom: 10}}>
        <span
          style={{
            background: `${ACCENT}1F`,
            color: ACCENT,
            padding: '4px 10px',
            borderRadius: 12,
            fontSize: 12,
            fontWeight: 700,
            letterSpacing: 0.5,
          }}
        >
          {badge}
        </span>
        <span style={{opacity: 0.6, fontSize: 14}}>Android 7.0 and newer</span>
      </div>

      <p style={{margin: '0 0 20px', opacity: 0.85, lineHeight: 1.6, maxWidth: '60ch'}}>
        TchueKAM on your phone or tablet, installed as a regular Android app.
      </p>

      <div style={{display: 'flex', gap: 12, flexWrap: 'wrap', alignItems: 'center', marginBottom: 20}}>
        {ready ? (
          <a
            href={apk.url}
            className="button button--primary button--lg tchuekam-cta"
            onClick={() => trackDownload(ANDROID_APK_NAME, apk.url, 'android', apk.version)}
            style={{textDecoration: 'none', background: '#00E5FF', color: '#07070d', fontWeight: 700}}
          >
            ⬇ Download for Android
          </a>
        ) : webReady ? (
          <a
            href={WEB_APP_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="button button--primary button--lg tchuekam-cta"
            onClick={() => track('web_app_opened', {os: 'android'})}
            style={{textDecoration: 'none', background: '#00E5FF', color: '#07070d', fontWeight: 700}}
          >
            🌐 Open the Web App
          </a>
        ) : (
          <span
            className="button button--lg tchuekam-cta tchuekam-cta-secondary tchuekam-cta-disabled"
            aria-disabled="true"
          >
            Coming soon
          </span>
        )}
        {ready && apk.size && <span style={{opacity: 0.55, fontSize: 13}}>APK · {apk.size}</span>}
      </div>

      {!ready && (
        <p style={{margin: '0 0 20px', fontSize: 14, lineHeight: 1.6, maxWidth: '60ch'}}>
          {webReady ? (
            <>
              The Android APK is being published. Until it is, the Web App runs on your phone — add it to your
              home screen with the steps in <Link to={`${MOBILE_GUIDE_PATH}#pwa-install`}>Quick PWA Installation</Link>.
            </>
          ) : (
            'The Android APK and the Web App are being published. This page switches them on as soon as they are available.'
          )}
        </p>
      )}

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
          gap: 16,
          paddingTop: 16,
          borderTop: `1px solid ${ACCENT}1A`,
        }}
      >
        <Spec label="Package" value="com.tchuekam.mobile" />
        <Spec label="Requires" value="Android 7.0+" />
        {ready && apk.size && <Spec label="Size" value={apk.size} />}
      </div>

      {ready && apk.sha256 && (
        <div style={{marginTop: 16}}>
          <Spec label="SHA-256" value={apk.sha256} />
        </div>
      )}

      <p style={{opacity: 0.6, fontSize: 13, marginTop: 18, marginBottom: 0, lineHeight: 1.6}}>
        Distributed directly by TchueKAM rather than through the Play Store, so Android asks you to allow
        installation from your browser or file manager once.
      </p>
    </div>
  );
}
