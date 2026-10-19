# Agentic Spec-Driven Development Boilerplate

A stack-agnostic starting point for projects built **with AI coding agents** — Claude Code, Codex, Cursor,
Gemini, Copilot, Antigravity, or anything that reads `AGENTS.md`.

It gives you a documentation system where **every feature has a spec, a design, a live status, and an
as-built guide**, architecture docs (HLD, LLD, schema, API) that stay in step with the code, ADRs, a lessons
-learned loop — plus an agent layer (rules, skills, workflows, roles) written once and used by every tool.

## Why

Agents forget between sessions, guess when specs are vague, and let docs rot. This boilerplate makes the
repo itself the memory:

- **Resumable** — any agent picks up from `docs/PROJECT_STATUS.md` → the feature's `status.md` "Resume here".
- **Spec before code** — nothing is built without an agreed `spec.md` (WHAT) and `design.md` (HOW).
- **Docs are part of done** — an update matrix says exactly which doc changes with which kind of code change;
  a Claude hook nudges, CI enforces.
- **Provider-neutral** — `AGENTS.md` + `.agents/` are the source; `.claude/` is generated; other tools get
  thin pointer files.
- **Learns** — lessons are logged and promoted into rules/skills so mistakes don't repeat.

## Layout

```
.
├── AGENTS.md                      ← canonical operating manual (thin router) — every agent reads this
├── CLAUDE.md  GEMINI.md           ← pointers (CLAUDE.md imports AGENTS.md)
├── .cursor/rules/project.mdc      ← pointer for Cursor
├── .github/copilot-instructions.md← pointer for Copilot
│
├── .agents/                       ← provider-neutral agent layer (SOURCE OF TRUTH)
│   ├── RULES.md                   ← always-on guardrails
│   ├── skills/                    ← auto-triggered know-how (SKILL.md)
│   │   ├── spec-workflow/         ← the tracking spine: start → build → end of every task
│   │   ├── docs-sync/             ← walk the update matrix
│   │   ├── feature-design/        ← write feature HLD + LLD
│   │   ├── adr-writing/  lesson-capture/  code-review/
│   ├── workflows/                 ← invocable procedures (/commands in Claude)
│   │   ├── project-init  status  resume
│   │   ├── feature-start  feature-design  feature-complete
│   │   └── docs-sync  adr-new  lesson
│   └── roles/                     ← specialists: architect, implementer, test-engineer, reviewer, docs-keeper
├── .agent → .agents               ← symlink for Antigravity
│
├── .claude/                       ← Claude Code adapter
│   ├── settings.json              ← permissions + hooks
│   ├── hooks/                     ← session-start briefing · secret guard · docs guard
│   └── skills/ agents/ commands/  ← GENERATED from .agents/ (make sync-agents)
│
├── docs/
│   ├── README.md                  ← docs map, lifecycle, UPDATE MATRIX
│   ├── PROJECT_STATUS.md          ← INDEX — start every task here
│   ├── product/PRD.md
│   ├── architecture/              ← HLD.md · LLD.md · schema.md · api.md · diagrams/
│   ├── features/_TEMPLATE/        ← spec.md · design.md · status.md · guide.md
│   ├── decisions/                 ← ADRs (+ index)
│   ├── reference/                 ← glossary · conventions
│   ├── operations/                ← runbook · deployment
│   ├── plans/                     ← dated implementation plans
│   ├── LESSONS.md                 ← lessons learned
│   └── CHANGELOG.md
│
├── scripts/                       ← stdlib-only Python: bootstrap, new_feature, new_adr, docs_check, sync_agents
├── Makefile                       ← make feature / adr / docs-check / sync-agents / check
└── .github/                       ← CI (docs-check + agent sync), PR template, issue templates
```

## Quick start

```bash
# 1. Create your project from this template (GitHub "Use this template", or:)
gh repo create my-app --template adityagirigoswami/agentic-sdd-boilerplate --private --clone
cd my-app

# 2. Bootstrap: sets the project name, stamps dates, chmods hooks, generates .claude/
python3 scripts/bootstrap.py "My App"
cp .env.example .env                                         # your secrets (gitignored)
cp .claude/settings.local.json.example .claude/settings.local.json   # optional personal overrides

# 3. Open your agent and initialize the product docs by interview
claude            # then: /project-init "one-line idea"
```

Not using Claude? Tell your agent: *"Read AGENTS.md, then follow `.agents/workflows/project-init.md`."*

## The loop

```
/project-init           → PRD, HLD, stack ADRs, MVP features registered (⬜)
/feature-start <f>      → spec.md drafted with you → you approve → 🟡
/feature-design <f>     → design.md (HLD + LLD + test strategy) → you approve
  build                 → implementer / test-engineer roles; status.md updated each session
/feature-complete <f>   → every AC proven, guide.md written, docs synced, reviewed → ✅
/status · /resume       → where are we / continue where we stopped
/lesson · /adr-new      → capture what we learned / decided
```

### Per-feature docs

| File | Answers | When written | Changes |
|---|---|---|---|
| `spec.md` | WHAT & WHY — goal, scope in/out, ACs | `feature-start` | rarely, with your approval |
| `design.md` | HOW — HLD diagram, LLD (files, data, contracts, errors), alternatives, decision log | `feature-design` | when the design changes |
| `status.md` | WHERE — Resume here, checklist, short work log | every session | constantly |
| `guide.md` | HOW IT WORKS — as-built flow, file map, run/test, troubleshooting | `feature-complete` | when behaviour changes |

### What updates when

See **[docs/README.md → Update matrix](docs/README.md#update-matrix)**. Examples: a migration updates
`architecture/schema.md`; a new endpoint updates `architecture/api.md`; a new service updates `HLD.md`;
a cross-feature decision creates an ADR; a surprising bug adds a `LESSONS.md` entry.

## Tooling

| Command | Does |
|---|---|
| `make feature name=user-auth` | Scaffold `docs/features/user-auth/` + index row |
| `make adr title="Use Postgres"` | Next-numbered ADR + index row |
| `make docs-check` | Lint: required files, index ↔ status consistency, ✅ checklist complete, staleness, broken links |
| `make sync-agents` | Regenerate `.claude/` from `.agents/` |
| `make check` | Everything CI runs |

Requirements: `git`, `python3` (3.8+). No third-party packages.

## Supported agents

| Tool | Picks up |
|---|---|
| Claude Code | `CLAUDE.md` → `AGENTS.md`; generated skills, subagents, `/commands`; hooks |
| OpenAI Codex | `AGENTS.md`, `.agents/skills/` |
| Cursor | `AGENTS.md`, `.cursor/rules/project.mdc` |
| Gemini CLI | `GEMINI.md` → `AGENTS.md` |
| GitHub Copilot | `AGENTS.md`, `.github/copilot-instructions.md` |
| Antigravity | `AGENTS.md`, `.agent/` (symlink to `.agents/`) |

> Windows: enable `git config core.symlinks true` (or drop the `.agent` symlink if you don't use Antigravity).

## Customizing for a project

1. Fill `AGENTS.md §1` (stack + commands) — agents run these verbatim.
2. Add domain guardrails to `.agents/RULES.md §10+` (e.g. tenant isolation, PII, LLM-call rules).
3. Add domain skills (`.agents/skills/db-migration/`, `…/llm-call/`) and split `implementer` into
   `backend-engineer`, `frontend-engineer`, … in `.agents/roles/`. Run `make sync-agents`.
4. Add a `PostToolUse` lint/test hook in `.claude/settings.json` once the stack exists.
5. Tune `scripts/docs_check.py` (`STALE_DAYS`, required files) to taste.

## Design notes

Built from two earlier setups: a generic Claude Code template (CLAUDE.md sections, one example per
`.claude/` artifact type) and a production multi-tenant project whose docs/agents evolved over months
(thin-router CLAUDE.md, rules file, per-feature spec/status, feature-start/complete commands, domain
skills and specialist agents). Kept what worked; fixed what hurt:

| Observed problem | Fix here |
|---|---|
| `status.md` logs grew to hundreds of lines; decisions buried in them | Split spec / design / status / guide; "Resume here" ≤ 10 lines; Rule 09 |
| Ad-hoc `LLD.md`, `guide.md`, `technical-overview.md` in random features | Standard 4-file feature folder; system HLD/LLD in `architecture/` |
| No ADRs — rationale lost | `docs/decisions/` + `adr-writing` skill |
| Index rows stale / bloated notes | `docs_check.py` enforces index ↔ status consistency, flags stale 🟡 |
| Config locked to one tool | `AGENTS.md` + `.agents/`; `.claude/` generated; pointers for others |
| `.env.*` deny rule also blocked `.env.example` | Hook-based secret guard that exempts `.example` |
| Lessons fixed silently, repeated later | `LESSONS.md` + promotion into rules/skills |

See [ADR-0001](docs/decisions/0001-spec-driven-agentic-development.md).
