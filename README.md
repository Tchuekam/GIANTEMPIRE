# TchueKAM Agent — Documentation

Official documentation for [TchueKAM Agent](https://tchuekam.com), built with [Docusaurus](https://docusaurus.io).

Lives at **[docs.tchuekam.com](https://docs.tchuekam.com)**.

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

Same for download buttons — `<LatestRelease />` pulls the latest release's assets dynamically.

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

`docs.tchuekam.com` → CNAME → `tchuekam.github.io`

(See the project SETUP.md for full DNS instructions.)
