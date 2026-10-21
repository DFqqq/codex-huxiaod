#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Install the bundled Hu Xiao D pet using Python 3.8+ (standard library only)."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
import uuid


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_source(source):
    manifest_path = source / "pet.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    pet_id = manifest.get("id", "")
    atlas = manifest.get("spritesheetPath", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", pet_id):
        raise ValueError("Invalid pet id")
    if pet_id != "hu-xiao-d" or manifest.get("spriteVersionNumber") != 2:
        raise ValueError("Expected the hu-xiao-d v2 package")
    if atlas != "spritesheet.webp":
        raise ValueError("Unexpected spritesheet filename")
    expected = {}
    for line in (source / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        checksum, name = line.split(maxsplit=1)
        name = name.lstrip("*")
        if not re.fullmatch(r"[a-f0-9]{64}", checksum) or name in expected:
            raise ValueError("Malformed SHA256SUMS")
        expected[name] = checksum
    if set(expected) != {"pet.json", atlas}:
        raise ValueError("SHA256SUMS must cover exactly pet.json and the atlas")
    for name, checksum in expected.items():
        path = source / name
        if path.is_symlink() or not path.is_file() or sha256(path) != checksum:
            raise ValueError("Source checksum mismatch: " + name)
    # Read both runtime files before changing the destination.
    payloads = {name: (source / name).read_bytes() for name in expected}
    for name, data in payloads.items():
        if hashlib.sha256(data).hexdigest() != expected[name]:
            raise ValueError("Source changed while reading: " + name)
    return manifest, expected, payloads


def atomic_write(destination, data):
    fd, temporary_name = tempfile.mkstemp(prefix=".foxiaod-", dir=str(destination.parent))
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
        os.replace(str(temporary), str(destination))
    finally:
        if temporary.exists():
            temporary.unlink()


def install(source, codex_home):
    manifest, expected, payloads = validate_source(source)
    pet_id = manifest["id"]
    codex_home = codex_home.expanduser().resolve()
    pets = codex_home / "pets"
    target = pets / pet_id
    if pets.is_symlink() or target.is_symlink():
        raise ValueError("Refusing a symlinked pet destination")
    if target.exists() and not target.is_dir():
        raise ValueError("Pet destination is not a directory")
    if target.exists() and any(path.is_symlink() for path in target.rglob("*")):
        raise ValueError("Refusing an existing pet directory containing symlinks")
    unchanged = target.is_dir() and all(
        (target / name).is_file() and sha256(target / name) == checksum
        for name, checksum in expected.items()
    )
    notice_names = ("RIGHTS-NOTICE.md", "ATTRIBUTION.md", "SHA256SUMS")
    for name in notice_names:
        if not (source / name).is_file():
            raise ValueError("Missing required notice: " + name)
    notices_unchanged = target.is_dir() and all(
        (target / name).is_file() and (target / name).read_bytes() == (source / name).read_bytes()
        for name in notice_names
    )
    legacy_notice = target / ("LICENSE-" + "CC-" + "BY-4.0.txt")
    if unchanged and notices_unchanged and not legacy_notice.exists():
        return {"status": "already_installed", "path": str(target), "backup": None}
    backup = None
    if target.exists():
        backup_root = pets / ".backups"
        if backup_root.is_symlink():
            raise ValueError("Refusing a symlinked backup directory")
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup = backup_root / (pet_id + "-" + stamp + "-" + uuid.uuid4().hex[:8])
        shutil.copytree(str(target), str(backup), symlinks=True)
    target.mkdir(parents=True, exist_ok=True)
    # Install the image before making its manifest visible to Codex.
    atomic_write(target / manifest["spritesheetPath"], payloads[manifest["spritesheetPath"]])
    for name in notice_names:
        path = source / name
        if path.is_file():
            atomic_write(target / name, path.read_bytes())
    if legacy_notice.is_file():
        legacy_notice.unlink()
    atomic_write(target / "pet.json", payloads["pet.json"])
    for name, checksum in expected.items():
        if sha256(target / name) != checksum:
            raise ValueError("Installed checksum mismatch: " + name)
    return {"status": "installed", "path": str(target), "backup": str(backup) if backup else None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1] / "pets" / "hu-xiao-d")
    parser.add_argument("--codex-home", type=Path, help="Override CODEX_HOME for installation or testing")
    args = parser.parse_args()
    codex_home = args.codex_home or Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    try:
        result = install(args.source.expanduser().resolve(), codex_home)
    except (OSError, ValueError, KeyError) as error:
        print("Installation failed: " + str(error), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=True, indent=2))
    print("Next: Settings > Pets > Refresh > select Hu Xiao D, then enter /pet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
