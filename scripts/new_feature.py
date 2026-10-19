#!/usr/bin/env python3
"""Scaffold docs/features/<name>/ from _TEMPLATE and register it in PROJECT_STATUS.md.

Usage: python3 scripts/new_feature.py <kebab-case-name>
"""
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FEATURES = ROOT / "docs" / "features"
INDEX = ROOT / "docs" / "PROJECT_STATUS.md"
END = "<!-- FEATURES:END -->"


def main() -> int:
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        print("usage: new_feature.py <kebab-case-name>")
        return 2
    name = sys.argv[1].strip()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        print(f"✗ '{name}' is not kebab-case (e.g. user-auth)")
        return 2
    dest = FEATURES / name
    if dest.exists():
        print(f"✗ {dest.relative_to(ROOT)} already exists")
        return 1

    today = dt.date.today().isoformat()
    shutil.copytree(FEATURES / "_TEMPLATE", dest)
    for f in dest.glob("*.md"):
        f.write_text(f.read_text().replace("<name>", name).replace("YYYY-MM-DD", today))

    index = INDEX.read_text()
    if END not in index:
        print(f"✗ {END} marker missing from PROJECT_STATUS.md — add the row by hand")
        return 1
    row = f"| [{name}](features/{name}/) | ⬜ | — | {today} | |\n"
    index = index.replace(END, row + END, 1)
    index = re.sub(r"\*\*Last updated:\*\* \S+", f"**Last updated:** {today}", index, count=1)
    INDEX.write_text(index)

    print(f"✓ created docs/features/{name}/ (spec, design, status, guide) and index row")
    print(f"  next: draft spec.md with the human → `feature-start {name}` workflow")
    return 0


if __name__ == "__main__":
    sys.exit(main())
