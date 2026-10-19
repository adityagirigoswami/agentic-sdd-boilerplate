# `.agents/` — provider-neutral agent layer (source of truth)

Everything an AI agent needs to *behave* correctly in this repo, written once, usable by any tool.

```
.agents/
├── RULES.md      always-on guardrails (every agent, every task)
├── skills/       know-how, auto-triggered by description      → SKILL.md format (Claude, Codex, Antigravity…)
├── workflows/    procedures a human invokes by name             → /slash-commands in Claude Code
└── roles/        specialist personas to delegate to            → subagents in Claude Code
```

`.agent` is a symlink to this folder (Antigravity reads `.agent/workflows`, `.agent/skills`).

## How each tool picks this up

| Tool | Reads |
|---|---|
| Claude Code | `CLAUDE.md` (imports `AGENTS.md`) + **generated** `.claude/{skills,agents,commands}` |
| OpenAI Codex | `AGENTS.md` + `.agents/skills/` |
| Cursor | `AGENTS.md` + `.cursor/rules/project.mdc` |
| Gemini CLI | `GEMINI.md` → `AGENTS.md` |
| GitHub Copilot | `AGENTS.md` + `.github/copilot-instructions.md` |
| Antigravity | `AGENTS.md` + `.agent/` (symlink) |
| Anything else | Point it at `AGENTS.md`; workflows are plain markdown checklists |

## Editing rules

1. Edit **here**, never in `.claude/` — then run `make sync-agents`. CI fails on drift (`make check-agents`).
2. Frontmatter: `name` + `description` are required for skills and roles; `description` is required for
   workflows. The description is the trigger — make it specific ("Use when …").
3. Keep files short. A skill is a checklist with gotchas, not an essay. Link docs for facts.
4. Roles may carry `tools:` / `model:` (Claude-specific; others ignore them).
5. Workflows receive arguments as `$ARGUMENTS` (Claude substitutes; other agents read it as "the argument").

## Adding your own

- Domain procedure (e.g. "adding a DB migration") → `skills/<name>/SKILL.md`.
- Repeatable multi-step task you trigger → `workflows/<name>.md`.
- Specialist (e.g. `backend-engineer`, `security-auditor`) → `roles/<name>.md`.
