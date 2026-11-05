import React from 'react';
import { SpeedInsights } from '@vercel/speed-insights/react';

// Root component wraps the entire Docusaurus app
// This is the recommended way to add global providers in Docusaurus
export default function Root({ children }: { children: React.ReactNode }) {
  return (
    <>
      {children}
      <SpeedInsights />
    </>
  );
}
