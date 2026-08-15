import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import LatestRelease from '@site/src/components/LatestRelease';

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title="TchueKAM Agent — Native desktop AI assistant"
      description="Download TchueKAM Agent and turn your computer into an AI-native workspace."
    >
      <main style={{padding: '80px 24px', textAlign: 'center', maxWidth: 1100, margin: '0 auto'}}>
        <span style={{
          display: 'inline-block',
          background: 'rgba(0,242,254,0.12)',
          color: '#00F2FE',
          padding: '6px 14px',
          borderRadius: 20,
          fontSize: 12,
          fontWeight: 600,
          letterSpacing: 1.2,
          textTransform: 'uppercase',
          marginBottom: 24,
        }}>
          TchueKAM Agent is live
        </span>

        <h1 style={{fontSize: 'clamp(36px, 6vw, 64px)', lineHeight: 1.1, marginBottom: 20, fontWeight: 700}}>
          Your native desktop<br/>AI assistant.
        </h1>

        <p style={{fontSize: 'clamp(16px, 2vw, 19px)', opacity: 0.75, maxWidth: 640, margin: '0 auto 40px', lineHeight: 1.5}}>
          {siteConfig.tagline}
        </p>

        <div style={{display: 'flex', gap: 14, justifyContent: 'center', flexWrap: 'wrap', marginBottom: 16}}>
          <LatestRelease />
          <Link to="/getting-started" className="button button--secondary button--lg" style={{textDecoration: 'none'}}>
            Read the docs →
          </Link>
        </div>

        <p style={{opacity: 0.5, fontSize: 13, marginTop: 12}}>
          Free · Open source · Windows, macOS, Linux
        </p>

        <section style={{marginTop: 80, display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 24, textAlign: 'left'}}>
          <Feature
            title="Fast and local"
            body="Runs natively on your machine — no browser tab, no latency."
          />
          <Feature
            title="Private by default"
            body="Your conversations stay on your computer unless you choose to sync."
          />
          <Feature
            title="Auto-updates"
            body="Every release reaches you automatically. No manual reinstalls."
          />
          <Feature
            title="Cross-platform"
            body="Same experience on Windows, macOS, and Linux."
          />
        </section>

        {/* Founder & Enterprise Products Showcase */}
        <section style={{
          marginTop: 90,
          padding: '40px 32px',
          background: 'linear-gradient(135deg, rgba(0, 242, 254, 0.05) 0%, rgba(79, 172, 254, 0.08) 100%)',
          borderRadius: 20,
          border: '1px solid rgba(0, 242, 254, 0.2)',
          textAlign: 'left',
        }}>
          <div style={{display: 'flex', gap: 32, alignItems: 'center', flexWrap: 'wrap'}}>
            <img 
              src="/img/rostand-tchuekam-executive.jpg" 
              alt="Rostand Tchuekam — Founder of GianTecH Empire"
              style={{
                width: 140,
                height: 140,
                borderRadius: '50%',
                objectFit: 'cover',
                border: '3px solid #00F2FE',
                boxShadow: '0 8px 24px rgba(0,242,254,0.25)',
              }}
            />
            <div style={{flex: 1, minWidth: 280}}>
              <span style={{fontSize: 12, fontWeight: 700, letterSpacing: 1.2, textTransform: 'uppercase', color: '#00F2FE'}}>
                Founded by Rostand Tchuekam · GianTecH Empire
              </span>
              <h2 style={{fontSize: 28, margin: '8px 0 12px', fontWeight: 700}}>
                Architecting African AI & Enterprise Software
              </h2>
              <p style={{fontSize: 15, opacity: 0.8, lineHeight: 1.6, margin: '0 0 18px'}}>
                Under the leadership of <strong>Rostand Tchuekam</strong>, GianTecH Empire designs groundbreaking technology—from <strong>TchueKAM Agent</strong> to <strong>Magida</strong>, the supermarket management system powering prominent retail stores and supermarkets.
              </p>
              <div style={{display: 'flex', gap: 12, flexWrap: 'wrap'}}>
                <Link to="/about-founder" className="button button--primary button--sm">
                  About Rostand & GianTecH →
                </Link>
                <Link to="/magida" className="button button--outline button--secondary button--sm">
                  Explore Magida ERP →
                </Link>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}

function Feature({title, body}: {title: string; body: string}) {
  return (
    <div style={{
      padding: '24px 28px',
      background: 'rgba(255,255,255,0.02)',
      border: '1px solid rgba(255,255,255,0.06)',
      borderRadius: 12,
    }}>
      <h3 style={{margin: '0 0 8px', fontSize: 18}}>{title}</h3>
      <p style={{margin: 0, opacity: 0.7, fontSize: 14, lineHeight: 1.6}}>{body}</p>
    </div>
  );
}
