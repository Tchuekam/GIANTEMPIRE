---
id: configuration
title: Configuration
sidebar_position: 6
---

# Configuration

TchueKAM works out of the box. Tune it from **Settings** when you want to customize.

## Where settings live

Settings are stored in:
- **Windows:** `%AppData%\TchueKAM\config.json`
- **macOS:** `~/Library/Application Support/TchueKAM/config.json`
- **Linux:** `~/.config/TchueKAM/config.json`

You can edit this file directly when TchueKAM is closed, or use the Settings UI.

## Key settings

### Workspace
- **Default project directory** — where TchueKAM opens new projects
- **Auto-save** — save edits as you go (default: on)
- **Indexing** — let TchueKAM build a searchable index of your projects (default: on)

### Updates
- **Check frequency** — how often TchueKAM looks for new releases (default: every 4 hours)
- **Auto-download** — download updates in the background (default: on)
- **Install on quit** — apply updates when you close TchueKAM (default: on)

See [Updates](updates) for the full update flow.

### Privacy
- **Telemetry** — anonymous usage statistics (default: on, can be turned off)
- **Crash reports** — send stack traces when TchueKAM crashes (default: on)
- **Conversation sync** — sync conversations across devices (default: off)

### Appearance
- **Theme** — dark, light, or follow system
- **Font size** — small / medium / large
- **Accent color** — match your system or pick a custom hex

### Keyboard shortcuts
All shortcuts are remappable in **Settings → Keyboard**. Defaults:

| Action | Windows / Linux | macOS |
|---|---|---|
| New chat | `Ctrl+N` | `⌘N` |
| Search | `Ctrl+K` | `⌘K` |
| Toggle sidebar | `Ctrl+B` | `⌘B` |
| Settings | `Ctrl+,` | `⌘,` |

## Environment variables

Some advanced settings can be controlled via environment variables for power users:

| Variable | Effect |
|---|---|
| `TCHUEKAM_DATA_DIR` | Override the default data directory |
| `TCHUEKAM_LOG_LEVEL` | `debug`, `info`, `warn`, `error` |
| `TCHUEKAM_DISABLE_UPDATER` | Disable automatic update checks |

## Reset to defaults

Close TchueKAM, delete `config.json`, relaunch. All settings revert to defaults; your conversations are preserved.
