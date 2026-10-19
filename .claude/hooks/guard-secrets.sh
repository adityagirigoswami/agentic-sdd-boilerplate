#!/usr/bin/env bash
# PreToolUse: block agents from reading or writing secret files (.env, .env.*, keys), except .env.example.
# Exit 2 = block the tool call; stderr is shown to Claude.
INPUT=$(cat)
printf '%s' "$INPUT" | python3 -c '
import json, os, re, sys
d = json.load(sys.stdin)
tool, inp = d.get("tool_name", ""), d.get("tool_input", {}) or {}
SECRET = re.compile(r"(^|[\s/\x27\x22=<>|;&(])(\.env(\.[\w.-]+)?|[\w.-]*\.(pem|key)|[\w.-]*-key\.json)(?=$|[\s\x27\x22;|&)>])")

def is_secret(name):
    base = os.path.basename(name)
    if base.endswith(".example") or base.endswith(".sample") or base.endswith(".template"):
        return False
    return bool(re.fullmatch(r"\.env(\.[\w.-]+)?|.*\.(pem|key)|.*-key\.json", base))

hit = None
if tool in ("Read", "Edit", "Write", "MultiEdit", "NotebookEdit"):
    path = inp.get("file_path") or inp.get("notebook_path") or ""
    if is_secret(path):
        hit = path
elif tool == "Bash":
    for m in SECRET.finditer(inp.get("command", "")):
        if is_secret(m.group(2)):
            hit = m.group(2)
            break
if hit:
    print(f"Blocked by .claude/hooks/guard-secrets.sh: \"{hit}\" looks like a secret file. "
          "Agents must not read or write secrets (RULES §06). Use .env.example to document variables; "
          "ask the human to set real values.", file=sys.stderr)
    sys.exit(2)
'
