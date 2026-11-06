// A heads-up for pages whose steps start with "open the Web App": shown only while the web app's
// host cannot be reached, so readers are not sent to a browser error page without warning.
// Renders nothing the rest of the time - and stops showing by itself once the app answers again.

import React from 'react';
import {WEB_APP_URL, isWebAppAvailable, useWebApp} from './downloads';

export default function WebAppNotice() {
  const web = useWebApp();
  if (isWebAppAvailable(web)) return null;

  return (
    <div className="alert alert--warning" role="status" style={{marginBottom: '1.5rem'}}>
      The Web App at <code>{new URL(WEB_APP_URL).host}</code> is not reachable right now, so the steps below
      will not work yet. This notice disappears by itself as soon as it is back online.
    </div>
  );
}
