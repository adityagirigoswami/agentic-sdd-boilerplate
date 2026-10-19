#!/usr/bin/env python3
"""Create the next ADR from docs/decisions/0000-template.md and add it to the index.

Usage: python3 scripts/new_adr.py "Use PostgreSQL for primary storage"
"""
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "docs" / "decisions"
END = "<!-- ADRS:END -->"


def main() -> int:
    title = " ".join(sys.argv[1:]).strip()
    if not title:
        print('usage: new_adr.py "<decision title>"')
        return 2
    nums = [int(m.group(1)) for p in DIR.glob("*.md") if (m := re.match(r"(\d{4})-", p.name))]
    num = f"{max(nums, default=0) + 1:04d}"
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
    path = DIR / f"{num}-{slug}.md"
    today = dt.date.today().isoformat()

    text = (DIR / "0000-template.md").read_text()
    text = text.replace("NNNN", num, 1).replace("<title — the decision, imperative>", title)
    path.write_text(text.replace("YYYY-MM-DD", today))

    readme = DIR / "README.md"
    idx = readme.read_text()
    row = f"| [{num}]({path.name}) | {title} | Proposed | {today} |\n"
    readme.write_text(idx.replace(END, row + END, 1) if END in idx else idx + row)

    print(f"✓ created {path.relative_to(ROOT)} (status: Proposed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
