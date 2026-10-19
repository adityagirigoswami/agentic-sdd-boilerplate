#!/usr/bin/env python3
"""Generate .claude/{skills,agents,commands} from the provider-neutral .agents/ layer.

.agents/skills/<n>/   -> .claude/skills/<n>/      (whole folder; SKILL.md gets a GENERATED notice)
.agents/roles/<n>.md  -> .claude/agents/<n>.md
.agents/workflows/<n>.md -> .claude/commands/<n>.md

Only files carrying the GENERATED marker are ever overwritten or removed, so Claude-only files you add
by hand under .claude/ are left alone.

Usage:  python3 scripts/sync_agents.py          # write
        python3 scripts/sync_agents.py --check  # exit 1 if .claude/ is out of date (CI)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / ".agents"
DST = ROOT / ".claude"
MARKER = "GENERATED from"


def notice(src: Path) -> str:
    rel = src.relative_to(ROOT)
    return f"<!-- {MARKER} {rel} by scripts/sync_agents.py — edit the source, then run `make sync-agents`. -->\n"


def with_notice(text: str, src: Path) -> str:
    """Insert the notice right after YAML frontmatter (frontmatter must stay first)."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            cut = end + len("\n---\n")
            return text[:cut] + "\n" + notice(src) + text[cut:]
    return notice(src) + "\n" + text


def expected() -> dict:
    """Map destination path -> expected content (str for text, bytes for binary)."""
    out = {}
    for skill in sorted(p for p in (SRC / "skills").iterdir() if p.is_dir()):
        for f in sorted(p for p in skill.rglob("*") if p.is_file()):
            dst = DST / "skills" / skill.name / f.relative_to(skill)
            out[dst] = with_notice(f.read_text(), f) if f.name == "SKILL.md" else f.read_bytes()
    for kind, target in (("roles", "agents"), ("workflows", "commands")):
        for f in sorted((SRC / kind).glob("*.md")):
            out[DST / target / f.name] = with_notice(f.read_text(), f)
    return out


def is_generated(path: Path) -> bool:
    try:
        return MARKER in path.read_text(errors="ignore")[:2000]
    except OSError:
        return False


def current_generated() -> set:
    found = set()
    for sub in ("skills", "agents", "commands"):
        base = DST / sub
        if base.exists():
            found |= {p for p in base.rglob("*.md") if p.is_file() and is_generated(p)}
    return found


def main() -> int:
    check = "--check" in sys.argv
    want = expected()
    stale = current_generated() - set(want)
    drift = []
    for dst, content in want.items():
        old = dst.read_bytes() if dst.exists() else None
        new = content.encode() if isinstance(content, str) else content
        if old != new:
            drift.append(dst)
            if not check:
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(new)
    for p in stale:
        drift.append(p)
        if not check:
            p.unlink()
            if p.parent != DST / "skills" and not any(p.parent.iterdir()):
                p.parent.rmdir()

    rel = sorted(str(p.relative_to(ROOT)) for p in drift)
    if check:
        if rel:
            print("✗ .claude/ is out of sync with .agents/ — run `make sync-agents`:")
            print("\n".join(f"  {r}" for r in rel))
            return 1
        print("✓ .claude/ in sync with .agents/")
        return 0
    print(f"synced {len(want)} files" + (f"; updated/removed {len(rel)}" if rel else "; no changes"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
