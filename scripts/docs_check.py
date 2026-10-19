#!/usr/bin/env python3
"""Lint the docs so they stay structured, consistent, and resumable.

Errors (exit 1):
  - feature folder missing spec/design/status/guide
  - feature folder without an index row in PROJECT_STATUS.md, or index row without a folder
  - status emoji in status.md != status in the index
  - ✅ feature with unticked checklist items or an unwritten guide.md
  - ADR missing **Status:** or missing from docs/decisions/README.md
  - duplicate lesson IDs
  - broken relative markdown links
Warnings:
  - 🟡 feature not updated in > STALE_DAYS days
  - "Resume here" longer than 10 lines (Rule 09)
  - {{PROJECT_NAME}} placeholders left (run scripts/bootstrap.py)

Usage: python3 scripts/docs_check.py
"""
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
FEATURES = DOCS / "features"
INDEX = DOCS / "PROJECT_STATUS.md"
STALE_DAYS = 14
STATUSES = "⬜🟡✅⛔🅿️♻️"
REQUIRED = ("spec.md", "design.md", "status.md", "guide.md")
GUIDE_SENTINEL = "What it does in 3–5 lines."  # template text; gone once guide.md is written
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build"}

errors: list = []
warnings: list = []


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def status_of(text: str):
    m = re.search(r"\*\*Status:\*\*\s*(\S+)", text)
    return m.group(1) if m else None


def last_updated(text: str):
    m = re.search(r"\*\*Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})", text)
    return dt.date.fromisoformat(m.group(1)) if m else None


def section(text: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def index_rows() -> dict:
    text = INDEX.read_text()
    block = re.search(r"<!-- FEATURES:START -->(.*?)<!-- FEATURES:END -->", text, re.S)
    if not block:
        errors.append(f"{rel(INDEX)}: FEATURES:START/END markers missing")
        return {}
    rows = {}
    for line in block.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        m = re.search(r"features/([a-z0-9-]+)/?", cells[0])
        name = m.group(1) if m else re.sub(r"[\[\]`]", "", cells[0])
        rows[name] = cells[1]
    return rows


def check_features() -> None:
    rows = index_rows()
    dirs = sorted(p for p in FEATURES.iterdir() if p.is_dir() and not p.name.startswith("_"))
    for d in dirs:
        missing = [f for f in REQUIRED if not (d / f).exists()]
        if missing:
            errors.append(f"{rel(d)}: missing {', '.join(missing)}")
        st_file = d / "status.md"
        if not st_file.exists():
            continue
        text = st_file.read_text()
        st = status_of(text)
        if not st or st[0] not in STATUSES:
            errors.append(f"{rel(st_file)}: header needs **Status:** <one of {' '.join(STATUSES)}>")
            continue
        if d.name not in rows:
            errors.append(f"{rel(d)}: no row in docs/PROJECT_STATUS.md (Features table)")
        elif not rows[d.name].startswith(st[0]):
            errors.append(f"{d.name}: status.md says {st} but PROJECT_STATUS.md says {rows[d.name]}")

        if st.startswith("✅"):
            unticked = re.findall(r"^- \[ \] (.+)$", section(text, "Checklist"), re.M)
            if unticked:
                errors.append(f"{rel(st_file)}: marked ✅ but unticked: {'; '.join(unticked)}")
            guide = d / "guide.md"
            if guide.exists() and GUIDE_SENTINEL in guide.read_text():
                errors.append(f"{rel(guide)}: feature is ✅ but guide.md is still the template")
        if st.startswith("🟡"):
            lu = last_updated(text)
            if lu and (dt.date.today() - lu).days > STALE_DAYS:
                warnings.append(f"{d.name}: 🟡 but status.md not updated for {(dt.date.today() - lu).days} days")
        resume = [l for l in section(text, "Resume here").splitlines() if l.strip() and not l.strip().startswith("<!--")]
        if len(resume) > 10:
            warnings.append(f"{rel(st_file)}: 'Resume here' is {len(resume)} lines (keep ≤ 10, Rule 09)")
    for name in rows:
        if not (FEATURES / name).is_dir():
            errors.append(f"PROJECT_STATUS.md: row '{name}' has no docs/features/{name}/ folder")


def check_adrs() -> None:
    d = DOCS / "decisions"
    readme = (d / "README.md").read_text() if (d / "README.md").exists() else ""
    for p in sorted(d.glob("[0-9][0-9][0-9][0-9]-*.md")):
        if p.name.startswith("0000-"):
            continue
        if not status_of(p.read_text()):
            errors.append(f"{rel(p)}: missing **Status:**")
        if p.name not in readme:
            errors.append(f"{rel(p)}: not listed in docs/decisions/README.md")


def check_lessons() -> None:
    p = DOCS / "LESSONS.md"
    if p.exists():
        ids = re.findall(r"^### (L-\d{4})", p.read_text(), re.M)
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        if dupes:
            errors.append(f"{rel(p)}: duplicate lesson ids {', '.join(dupes)}")


def markdown_files():
    for p in ROOT.rglob("*.md"):
        parts = set(p.relative_to(ROOT).parts)
        if not parts & SKIP_DIRS and ".agent" not in p.relative_to(ROOT).parts[:1]:
            yield p


def check_links_and_placeholders() -> None:
    link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    placeholder_files = []
    for p in markdown_files():
        text = p.read_text(errors="ignore")
        if "{{PROJECT_NAME}}" in text:
            placeholder_files.append(rel(p))
        body = re.sub(r"```.*?```", "", text, flags=re.S)
        body = re.sub(r"`[^`\n]*`", "", body)
        for target in link.findall(body):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = target.split("#", 1)[0]
            if path and not (p.parent / path).exists():
                errors.append(f"{rel(p)}: broken link → {target}")
    if placeholder_files:
        warnings.append(f"{{{{PROJECT_NAME}}}} still in {len(placeholder_files)} files — run scripts/bootstrap.py")


def main() -> int:
    check_features()
    check_adrs()
    check_lessons()
    check_links_and_placeholders()
    for w in warnings:
        print(f"⚠ {w}")
    for e in errors:
        print(f"✗ {e}")
    if errors:
        print(f"\ndocs-check: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"✓ docs-check passed ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
