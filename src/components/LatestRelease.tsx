// Self-hosted direct download component for TchueKAM Agent.
// Single source of truth: Direct self-hosted release API endpoints.

import React, {useEffect, useState} from 'react';

const DOWNLOAD_BASE_URL = 'https://tchuekam-backend-production.up.railway.app/api/download';

const DIRECT_DOWNLOADS = {
  'windows': {
    url: `${DOWNLOAD_BASE_URL}/windows`,
    filename: 'TchueKAM-Setup.exe',
    label: 'Windows (64-bit)',
    type: '.exe installer',
  },
  'macos-arm64': {
    url: `${DOWNLOAD_BASE_URL}/mac-arm64`,
    filename: 'TchueKAM-Mac-arm64.dmg',
    label: 'macOS (Apple Silicon)',
    type: '.dmg',
  },
  'macos-x64': {
    url: `${DOWNLOAD_BASE_URL}/mac-x64`,
    filename: 'TchueKAM-Mac-x64.dmg',
    label: 'macOS (Intel)',
    type: '.dmg',
  },
  'linux': {
    url: `${DOWNLOAD_BASE_URL}/linux`,
    filename: 'TchueKAM-Linux.AppImage',
    label: 'Linux',
    type: '.AppImage',
  },
};

type OS = 'windows' | 'macos-arm64' | 'macos-x64' | 'linux';

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

function trackDownload(assetName: string, downloadUrl: string, targetOS: string, version: string = 'v1.0.0') {
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

export function StaticDownloadSection() {
  const [os, setOS] = useState<OS>('windows');

  useEffect(() => {
    setOS(detectOS());
  }, []);

  const primaryDownload = DIRECT_DOWNLOADS[os] || DIRECT_DOWNLOADS.windows;

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
          v1.0.0
        </span>
        <span style={{opacity: 0.6, fontSize: 14}}>
          Latest release
        </span>
      </div>

      <p style={{margin: '0 0 16px', opacity: 0.85, lineHeight: 1.6}}>
        Download TchueKAM Agent for your platform:
      </p>

      <div style={{display: 'flex', gap: 12, flexWrap: 'wrap', marginBottom: 16}}>
        <a
          href={primaryDownload.url}
          download={primaryDownload.filename}
          className="button button--primary button--lg"
          onClick={() => trackDownload(primaryDownload.filename, primaryDownload.url, os, 'v1.0.0')}
          style={{textDecoration: 'none', background: '#00E5FF', color: '#07070d', fontWeight: 700}}
        >
          ⬇ Download for Windows
        </a>
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
          {Object.entries(DIRECT_DOWNLOADS).map(([key, item]) => (
            <tr key={key}>
              <td><strong>{item.label}</strong></td>
              <td><code>{item.type}</code></td>
              <td>
                <a
                  href={item.url}
                  download={item.filename}
                  onClick={() => trackDownload(item.filename, item.url, key, 'v1.0.0')}
                  style={{color: '#00F2FE', fontWeight: 600, textDecoration: 'none'}}
                >
                  Download →
                </a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <p style={{opacity: 0.6, fontSize: 13, marginTop: 12}}>
        All downloads are verified and hosted directly by TchueKAM.
      </p>
    </div>
  );
}

export default function LatestRelease({showAllPlatforms = false}: {showAllPlatforms?: boolean}) {
  return <StaticDownloadSection />;
}
