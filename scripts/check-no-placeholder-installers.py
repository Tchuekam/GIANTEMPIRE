#!/usr/bin/env python3
"""Refuse to deploy a site that is serving a file pretending to be an installer.

A placeholder named TchueKAM-Setup.exe once sat in static/ for long enough to
reach customers. It was 66 bytes of text, so Windows answered "This app can't
run on your PC" for everyone who clicked Download. Nothing in the build looked
at the bytes, because nothing was asked to.

This is that check. It walks everything committed under static/ that is named
like an installer and confirms the content matches the name: a Windows
executable really starts with MZ, a disk image really ends with a UDIF
trailer, an AppImage really is an ELF, an APK really is a zip. Anything that
is only named like an installer fails the deploy.

Desktop installers are not committed here at all any more -- they are resolved
from GitHub releases (see src/components/downloads.ts) -- so for those the
check is simply that they have not crept back.

    python3 scripts/check-no-placeholder-installers.py

Exit status 0 means nothing on this site will download as a broken file.
"""

from __future__ import annotations

import sys
from pathlib import Path

STATIC = Path(__file__).resolve().parent.parent / "static"

# Resolved from GitHub releases now. If one of these reappears as a file, the
# old failure is back: the site would serve it instead of the real release.
NEVER_COMMIT = {
    "TchueKAM-Setup.exe",
    "TchueKAM-Mac-arm64.dmg",
    "TchueKAM-Mac-x64.dmg",
    "TchueKAM-Linux.AppImage",
    "TchueKAM-Mobile.apk",
}

# Suffixes we check the content of, with the minimum size that is plausible.
CHECKED = {
    ".exe": 20 * 1024 * 1024,
    ".msi": 20 * 1024 * 1024,
    ".dmg": 20 * 1024 * 1024,
    ".appimage": 20 * 1024 * 1024,
    ".apk": 1024 * 1024,
}


def content_problem(path: Path) -> str | None:
    """What is wrong with this file's bytes, or None if it is what it claims."""
    suffix = path.suffix.lower()
    size = path.stat().st_size
    with path.open("rb") as fh:
        head = fh.read(8)

    if suffix in (".exe", ".msi"):
        if head[:2] != b"MZ" and head[:8] != b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":
            return f"does not start with a Windows executable header (starts with {head!r})"
    elif suffix == ".appimage":
        if head[:4] != b"\x7fELF":
            return f"is not an ELF binary (starts with {head!r})"
    elif suffix == ".apk":
        if head[:2] != b"PK":
            return f"is not a zip archive (starts with {head!r})"
    elif suffix == ".dmg":
        if size < 512:
            return "is too small to contain a UDIF trailer"
        with path.open("rb") as fh:
            fh.seek(size - 512)
            if fh.read(4) != b"koly":
                return "has no 'koly' UDIF trailer, so macOS will not mount it"

    floor = CHECKED[suffix]
    if size < floor:
        return f"is {size:,} bytes; a real one is at least {floor:,}. This is a placeholder."
    return None


def main() -> int:
    if not STATIC.is_dir():
        print(f"error: no static/ directory at {STATIC}", file=sys.stderr)
        return 2

    failures: list[str] = []
    checked = 0

    for path in sorted(STATIC.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(STATIC.parent)

        if path.name in NEVER_COMMIT:
            failures.append(
                f"{rel} is committed to this repository. Desktop installers are "
                "resolved from GitHub releases; a file here shadows the real "
                "release asset and is how the 66-byte download happened."
            )
            continue

        if path.suffix.lower() not in CHECKED:
            continue

        checked += 1
        problem = content_problem(path)
        if problem:
            failures.append(f"{rel} {problem}")

    if failures:
        print("Refusing to deploy. These files would download as broken installers:\n")
        for f in failures:
            print(f"  FAIL  {f}")
        print(
            "\nIf a platform has no installer yet, publish nothing: the download "
            "card already shows 'Coming soon' until a release carries the asset."
        )
        return 1

    print(f"OK: no placeholder installers. {checked} downloadable file(s) verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
