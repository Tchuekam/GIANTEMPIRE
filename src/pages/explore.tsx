import React, { useEffect } from 'react';
import Head from '@docusaurus/Head';

export default function ExploreRedirect(): JSX.Element {
  useEffect(() => {
    // Immediate hard redirect to static studio showcase
    window.location.replace('/explore/index.html');
  }, []);

  return (
    <>
      <Head>
        <title>TchueKAM AI Creative Studio — Explore</title>
        <meta httpEquiv="refresh" content="0; url=/explore/index.html" />
      </Head>
      <div style={{
        background: '#050507',
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        color: '#c6f833',
        fontFamily: 'monospace',
        textAlign: 'center',
        padding: '20px'
      }}>
        <div style={{
          width: '36px',
          height: '36px',
          border: '3px solid rgba(198, 248, 51, 0.2)',
          borderTopColor: '#c6f833',
          borderRadius: '50%',
          animation: 'spin 0.8s linear infinite',
          marginBottom: '20px'
        }} />
        <h2 style={{ fontSize: '18px', fontWeight: 800, color: '#fff', letterSpacing: '1px', marginBottom: '8px' }}>
          TCHUEKAM AI CREATIVE STUDIO
        </h2>
        <p style={{ fontSize: '12px', color: '#9ba3af' }}>
          Entering cinematic showcase... If not redirected automatically, <a href="/explore/index.html" style={{ color: '#c6f833', textDecoration: 'underline' }}>click here</a>.
        </p>
        <style>{`
          @keyframes spin { to { transform: rotate(360deg); } }
        `}</style>
      </div>
    </>
  );
}
