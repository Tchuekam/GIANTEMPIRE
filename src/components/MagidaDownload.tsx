// Download section for the MAGIDA Android app.
//
// Mirrors LatestRelease.tsx, with one difference: version, size and checksum are
// read at runtime from the release manifest — the same file the installed apps
// poll for updates. Publishing a new APK therefore updates this page without
// anyone editing it, and the page can never advertise a version the apps
// disagree about.

import React, {useEffect, useState} from 'react';

// Under /downloads/, alongside the desktop installers. Must match the URL
// compiled into the APK (frontend/src/lib/appUpdate.ts) — installed apps poll
// this exact path and cannot be redirected later.
const MANIFEST_URL = '/downloads/magida/latest.json';
const FALLBACK_APK = '/downloads/magida/MAGIDA-latest.apk';

const ACCENT = '#00F2FE';

type Manifest = {
  versionName?: string;
  url?: string;
  size?: string;
  sha256?: string;
  minAndroid?: string;
  notes?: string;
  releasedAt?: string;
};

function trackDownload(version: string) {
  try {
    if (typeof window !== 'undefined' && (window as any).posthog?.capture) {
      (window as any).posthog.capture('download_started', {
        os: 'android',
        asset: 'MAGIDA.apk',
        source: 'docs_site',
        version,
      });
    }
  } catch {}
}

function Spec({label, value}: {label: string; value: string}) {
  return (
    <div style={{minWidth: 0}}>
      <div style={{fontSize: 11, letterSpacing: 0.6, textTransform: 'uppercase', opacity: 0.5}}>{label}</div>
      <div style={{fontSize: 14, fontWeight: 600, marginTop: 2, wordBreak: 'break-all'}}>{value}</div>
    </div>
  );
}

export default function MagidaDownload() {
  const [manifest, setManifest] = useState<Manifest | null>(null);
  const [failed, setFailed] = useState(false);

  useEffect(() => {
    let cancelled = false;
    fetch(MANIFEST_URL, {cache: 'no-store'})
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status)))))
      .then((data) => {
        if (!cancelled) setManifest(data);
      })
      .catch(() => {
        // The page must still offer the app even if the manifest is missing, so
        // fall back to the stable filename rather than showing nothing.
        if (!cancelled) setFailed(true);
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const version = manifest?.versionName;
  const url = manifest?.url || FALLBACK_APK;
  const released = manifest?.releasedAt
    ? new Date(manifest.releasedAt).toLocaleDateString(undefined, {year: 'numeric', month: 'long', day: 'numeric'})
    : null;

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
          {version ? `v${version}` : failed ? 'Latest' : '…'}
        </span>
        <span style={{opacity: 0.6, fontSize: 14}}>
          Android 5.1 and newer{released ? ` · released ${released}` : ''}
        </span>
      </div>

      <p style={{margin: '0 0 20px', opacity: 0.85, lineHeight: 1.6, maxWidth: '60ch'}}>
        The complete Magida point of sale, installed on the phone or tablet. Sells, prints receipts
        and tracks stock with no internet connection, and syncs to your shop server when one is in
        range.
      </p>

      <div style={{display: 'flex', gap: 12, flexWrap: 'wrap', alignItems: 'center', marginBottom: 20}}>
        <a
          href={url}
          download
          className="button button--primary button--lg"
          onClick={() => trackDownload(version || 'unknown')}
          style={{textDecoration: 'none', background: '#00E5FF', color: '#07070d', fontWeight: 700}}
        >
          ⬇ Download for Android
        </a>
        {manifest?.size && <span style={{opacity: 0.55, fontSize: 13}}>APK · {manifest.size}</span>}
      </div>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
          gap: 16,
          paddingTop: 16,
          borderTop: `1px solid ${ACCENT}1A`,
        }}
      >
        <Spec label="Package" value="com.tchuekam.magida" />
        <Spec label="Requires" value={`Android ${manifest?.minAndroid || '5.1'}+`} />
        {manifest?.size && <Spec label="Size" value={manifest.size} />}
      </div>

      {manifest?.sha256 && (
        <div style={{marginTop: 16}}>
          <Spec label="SHA-256" value={manifest.sha256} />
        </div>
      )}

      <p style={{opacity: 0.6, fontSize: 13, marginTop: 18, marginBottom: 0, lineHeight: 1.6}}>
        Distributed directly by GianTecH Empire rather than through the Play Store, so Android will
        ask you to permit installation from this source once. Every release is signed with the same
        key, so later versions install over this one and keep all existing data.
      </p>
    </div>
  );
}
