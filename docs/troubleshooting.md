---
id: troubleshooting
title: Troubleshooting
sidebar_position: 10
---

# Troubleshooting

Common issues and how to fix them.

## TchueKAM won't launch

### Windows: "Windows protected your PC"
Click **More info** → **Run anyway**. This appears because TchueKAM is new — Windows SmartScreen learns to trust it over time.

### macOS: "TchueKAM can't be opened because Apple cannot check it for malicious software"
1. Right-click TchueKAM in Applications → **Open**
2. Click **Open** in the dialog
Alternatively, run: `xattr -d com.apple.quarantine /Applications/TchueKAM.app`

### Linux: AppImage won't run
Make it executable: `chmod +x TchuekaM-Setup-linux-x64.AppImage`. If you see _"AppImage requires FUSE"_, install it: `sudo apt install libfuse2` (Ubuntu/Debian) or `sudo dnf install fuse` (Fedora).

## TchueKAM crashes on startup
1. Check **Settings → Updates** for a newer version
2. Delete `config.json` to reset settings (see [Configuration](configuration))
3. Send us your crash log — find it in:
   - Windows: `%AppData%\TchueKAM\logs\crash.log`
   - macOS: `~/Library/Logs/TchueKAM/crash.log`
   - Linux: `~/.config/TchueKAM/logs/crash.log`

## Updates aren't being applied
1. Check **Settings → Updates → History** for failed attempts
2. Make sure your firewall allows TchueKAM to reach `github.com` and `objects.githubusercontent.com`
3. If you're behind a proxy, configure it in **Settings → Network**
4. As a fallback, [download the latest installer](installation) and run it manually

## AI responses are slow or hang
- Slow responses usually indicate a network bottleneck — try a different network
- Hangs often mean a tool call is stuck — restart the conversation
- Very large files can time out — break the task into smaller pieces

## TchueKAM is using too much memory
- Close conversations you're not actively using (memory is per-tab)
- Restart TchueKAM weekly to clear caches
- Lower the **indexing depth** in **Settings → Workspace**

## I lost my conversations
Conversations are stored locally in the data folder ([see Configuration](configuration#where-settings-live)). If you have backups of that folder, copy them back. There's no cloud recovery unless you enabled conversation sync.

## Microphone doesn't work
1. **Settings → Privacy → Microphone** — make sure TchueKAM is allowed
2. **OS settings** — Windows / macOS / Linux must also grant microphone access to TchueKAM
3. Restart TchueKAM after granting permissions

## Still stuck?

[Contact us](contact) with the relevant log file from your data folder. We respond within one business day.
