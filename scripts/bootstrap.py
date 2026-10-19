#!/usr/bin/env python3
"""One-time setup after copying the boilerplate into a new project.

- Replaces {{PROJECT_NAME}} everywhere.
- Stamps today's date into the index, ADR-0001, and the seed lesson.
- Makes hooks executable and regenerates .claude/ from .agents/.

Usage: python3 scripts/bootstrap.py "My Project"
"""
import datetime as dt
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "venv"}
DATE_FILES = [
    "docs/PROJECT_STATUS.md",
    "docs/decisions/README.md",
    "docs/decisions/0001-spec-driven-agentic-development.md",
    "docs/LESSONS.md",
]


def text_files():
    for p in ROOT.rglob("*"):
        if p.is_file() and not p.is_symlink() and not SKIP_DIRS & set(p.relative_to(ROOT).parts):
            if p.suffix in {".md", ".mdc", ".json", ".yml", ".yaml", ".txt", ".example"} or p.name == "Makefile":
                yield p


def main() -> int:
    name = " ".join(sys.argv[1:]).strip()
    if not name:
        print('usage: bootstrap.py "<Project Name>"')
        return 2
    changed = 0
    for p in text_files():
        t = p.read_text(errors="ignore")
        if "{{PROJECT_NAME}}" in t:
            p.write_text(t.replace("{{PROJECT_NAME}}", name))
            changed += 1
    today = dt.date.today().isoformat()
    for rel in DATE_FILES:
        p = ROOT / rel
        if p.exists():
            p.write_text(p.read_text().replace("YYYY-MM-DD", today))
    for hook in (ROOT / ".claude" / "hooks").glob("*.sh"):
        hook.chmod(0o755)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_agents.py")], check=True)
    print(f"✓ project name set in {changed} files; dates stamped; hooks executable")
    print("next: open your agent and run the `project-init` workflow (Claude Code: /project-init)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
