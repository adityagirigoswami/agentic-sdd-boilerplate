#!/usr/bin/env bash
# Stop: if code changed but nothing under docs/ did, ask Claude (once) to walk the docs-sync matrix.
# Uses stop_hook_active to avoid loops. Disable with DOCS_GUARD=0.
[ "${DOCS_GUARD:-1}" = "0" ] && exit 0
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0
INPUT=$(cat)
printf '%s' "$INPUT" | python3 -c '
import json, subprocess, sys
d = json.load(sys.stdin)
if d.get("stop_hook_active"):
    sys.exit(0)
out = subprocess.run(["git", "status", "--porcelain", "-uall"], capture_output=True, text=True).stdout
paths = [l[3:].split(" -> ")[-1].strip("\"") for l in out.splitlines() if l.strip()]
NON_CODE = ("docs/", ".agents/", ".agent/", ".claude/", ".github/", ".cursor/")
code = [p for p in paths if not p.startswith(NON_CODE) and not p.endswith(".md")]
docs = [p for p in paths if p.startswith("docs/")]
if code and not docs:
    shown = ", ".join(code[:5]) + (" …" if len(code) > 5 else "")
    print(json.dumps({"decision": "block", "reason":
        f"Code changed ({shown}) but nothing under docs/ did. Before finishing: walk the docs-sync matrix "
        "(docs/README.md#update-matrix) and update the feature status.md (Resume here + log). "
        "If there is genuinely no doc impact, say so and why, then stop."}))
'
exit 0
