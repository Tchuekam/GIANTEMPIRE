// Renders TchueKAM Agent release notes and changelog history.

import React from 'react';

const STATIC_CHANGELOG = [
  {
    version: 'v1.0.0',
    title: 'Initial Production Release',
    date: '2026-07-24',
    notes: `
- Native desktop AI assistant with full tool execution & session persistence.
- High-aesthetic web dashboard, terminal interface, and Docusaurus site integration.
- Direct self-hosted installer distribution endpoints for Windows, macOS, and Linux.
- End-to-end authentication security and public API route allowlists.
    `,
  },
];

export default function Changelog() {
  return (
    <div className="tchuekam-changelog">
      {STATIC_CHANGELOG.map(r => (
        <article
          key={r.version}
          style={{
            padding: '24px 0',
            borderBottom: '1px solid rgba(255,255,255,0.08)',
          }}
        >
          <header style={{display: 'flex', alignItems: 'baseline', gap: 12, marginBottom: 12}}>
            <h2 style={{margin: 0, fontSize: '1.25rem', color: '#00F2FE'}}>{r.version} — {r.title}</h2>
            <time style={{opacity: 0.5, fontSize: '0.85rem'}}>{r.date}</time>
          </header>
          <div
            style={{lineHeight: 1.6, opacity: 0.9}}
          >
            <ul>
              {r.notes.trim().split('\n').filter(line => line.startsWith('- ')).map((line, idx) => (
                <li key={idx}>{line.substring(2)}</li>
              ))}
            </ul>
          </div>
        </article>
      ))}
    </div>
  );
}
