# CLAUDE.md

@AGENTS.md

## Claude Code specifics

- Rules: `.agents/RULES.md` — always apply. Docs map: `docs/README.md`.
- `.claude/skills`, `.claude/agents`, `.claude/commands` are **generated** from `.agents/` by
  `make sync-agents`. Edit `.agents/`, never the generated copies.
- Hooks (`.claude/settings.json`):
  - `SessionStart` → injects project status + active features + recent lessons.
  - `PreToolUse` → blocks reading/writing secrets (`.env*`).
  - `Stop` → reminds you once if code changed but `docs/` didn't (set `DOCS_GUARD=0` to silence).
- Use plan mode for anything touching more than one feature or module.
- Found a gotcha? Run `/lesson` — don't just fix it silently.
