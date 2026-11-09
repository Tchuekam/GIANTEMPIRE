# TchueKAM Agent — Documentation

Official documentation for [TchueKAM Agent](https://tchuekam.com), built with [Docusaurus](https://docusaurus.io).

Lives at **[tchuekam.com](https://tchuekam.com)**.

## Develop locally

```bash
npm install
npm start
```

Opens `http://localhost:3000`. Edits hot-reload.

## Build for production

```bash
npm run build
npm run serve
```

## How the changelog stays current

The Changelog page (`docs/changelog.mdx`) renders `<Changelog />`, which fetches `https://api.github.com/repos/Tchuekam/tchuekam-agent/releases` at page load. Publish a new GitHub Release → it shows up here automatically. No edits needed.

## Downloads: desktop, Android, and the Web App

`<LatestRelease />` (the card on the home page and on `/installation`) offers every way to get TchueKAM:

| Platform | Where it comes from |
|---|---|
| Windows, macOS, Linux | Static files in `static/`, served from this site (`/TchueKAM-Setup.exe`, …) |
| Android | The APK attached to a GitHub release of [`Tchuekam/tchuekam-desktop`](https://github.com/Tchuekam/tchuekam-desktop/releases) |
| iPhone / iPad, any browser | Web App (Coming soon) |

The primary button follows the visitor's platform (Android → APK, iPhone/iPad → Web App, otherwise the matching desktop installer).

### The Web App must be reachable

Before offering the Web App, the page checks that `WEB_APP_URL` answers (a `no-cors` `HEAD` request from the visitor's browser; it only needs to know the host responded). If the address does not resolve or the app is down, the card, the Android docs card and the Mobile Companion page show "Coming soon" / a notice instead of a link to a browser error page, and switch back on by themselves once the host answers. To move the Web App, change `WEB_APP_URL`.

### Publishing the Android APK

1. Build the APK from `apps/mobile` in `tchuekam-desktop`.
2. On GitHub, open the release (Releases → Edit) and attach the file as **`TchueKAM-Mobile.apk`**. Keep that exact name: the app's own "Download APK" links (`/api/download/android`) use it too, so one upload turns on every link.
3. That's all. The site asks the GitHub releases API for the newest published release that carries the APK, so the download switches on by itself — no edit or redeploy here. Until it exists, the card shows "Coming soon" (and points visitors at the Web App while that is reachable) instead of a dead link.

The release can be the desktop one or a separate Android release; the site finds the newest release that has the APK.

## Adding a new page

1. Create `docs/your-page.md` (or `.mdx` for React components)
2. Add the frontmatter:
   ```yaml
   ---
   id: your-page
   title: Your Page
   sidebar_position: 99
   ---
   ```
3. Add the page ID to the relevant category in `sidebars.js`

That's it. Push to `main`, GitHub Actions builds and deploys to GitHub Pages within ~2 minutes.

## Editing the branding

- **Colors:** `src/css/custom.css`
- **Navbar / footer:** `docusaurus.config.js`
- **Landing page:** `src/pages/index.tsx`

## Source of truth

| What | Where |
|---|---|
| Site config | `docusaurus.config.js` |
| Sidebar order | `sidebars.js` |
| Doc pages | `docs/` |
| React components | `src/components/` |
| Brand CSS | `src/css/custom.css` |
| Domain config | `static/CNAME` |
| Deploy workflow | `.github/workflows/deploy.yml` |

## DNS

`tchuekam.com` on Vercel

(See the project SETUP.md for full DNS instructions.)
