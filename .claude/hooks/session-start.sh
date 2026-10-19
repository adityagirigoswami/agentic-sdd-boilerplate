#!/usr/bin/env bash
# SessionStart: inject a compact project-status briefing so every session starts oriented.
# Whatever this prints to stdout is added to Claude's context.
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
S=docs/PROJECT_STATUS.md
[ -f "$S" ] || exit 0

echo "## Project briefing (auto-injected by .claude/hooks/session-start.sh)"
grep -E '^\*\*(Last updated|Phase):\*\*' "$S"
echo
echo "### Features in progress / blocked"
awk '/FEATURES:START/{f=1;next} /FEATURES:END/{f=0} f' "$S" | grep -E '🟡|⛔' || echo "(none)"
echo
echo "### Active focus"
awk '/^## Active focus/{f=1;next} /^## /{f=0} f' "$S" | grep -v '^<!--' | sed '/^[[:space:]]*$/d'
if [ -f docs/LESSONS.md ]; then
  echo
  echo "### Recent lessons (docs/LESSONS.md)"
  grep -E '^### L-[0-9]+' docs/LESSONS.md | head -3
fi
if git rev-parse --git-dir >/dev/null 2>&1; then
  echo
  echo "### Git: $(git branch --show-current 2>/dev/null) · $(git status --porcelain | wc -l | tr -d ' ') uncommitted file(s)"
fi
echo
echo "Before coding: read the feature's status.md (Resume here) → spec.md → design.md. Rules: .agents/RULES.md."
exit 0
