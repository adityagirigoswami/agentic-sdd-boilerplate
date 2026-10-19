# AGENTS.md — {{PROJECT_NAME}}

> **Canonical operating manual for every AI agent** (Claude Code, Codex, Cursor, Gemini, Copilot, Antigravity, …).
> Provider-specific files (`CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.cursor/rules/`) only point here.
> This file is a **thin router** — it tells you where facts live; it does not duplicate them.

## 0. Ask, don't assume (highest rule — overrides everything)

If anything is missing, ambiguous, conflicting, or doubtful while planning, designing, or building — **stop and ask**.
Surface trade-offs instead of guessing. A clarifying question before work beats a wrong implementation after.

## 1. Project at a glance

<!-- FILL: 3–5 lines. What this is, who it's for, the key design decision. Detail lives in docs/product/PRD.md. -->
- **What:** <one line>
- **Stack:** <language · framework · datastore · infra>
- **Shape:** <monolith / services / pipeline …> — see `docs/architecture/HLD.md`

### Commands
<!-- FILL: keep in sync with Makefile / package scripts. Agents run these verbatim. -->
| Task | Command |
|---|---|
| Install | `<cmd>` |
| Run (dev) | `<cmd>` |
| Test | `<cmd>` |
| Lint / format | `<cmd>` |
| Docs check | `make docs-check` |

## 2. The layer model — where things live

| Need | Go to | Owner of truth for |
|---|---|---|
| **Where are we?** | `docs/PROJECT_STATUS.md` | feature index, phase, blockers |
| WHAT & WHY (product) | `docs/product/PRD.md` | goals, non-goals, requirements |
| System shape | `docs/architecture/HLD.md` | components, flows, deployment |
| Cross-cutting internals | `docs/architecture/LLD.md` | modules, patterns, errors, config |
| Data model | `docs/architecture/schema.md` | tables/collections, migrations |
| Interfaces | `docs/architecture/api.md` | endpoints, events, contracts |
| One feature | `docs/features/<name>/` | `spec` WHAT · `design` HOW · `status` PROGRESS · `guide` AS-BUILT |
| Why we chose X | `docs/decisions/` (ADRs) | cross-feature decisions |
| What burned us | `docs/LESSONS.md` | lessons learned → promoted to rules |
| Guardrails | `.agents/RULES.md` | always-on rules (**always apply**) |
| Recurring know-how | `.agents/skills/` | procedures (auto-triggered) |
| Invocable procedures | `.agents/workflows/` | `/feature-start`, `/feature-complete`, … |
| Specialist roles | `.agents/roles/` | architect, implementer, reviewer, … |

**Each fact lives in exactly one place.** Link, don't copy. When a fact changes, update its owner.
Full docs map + the "what to update when" matrix: `docs/README.md`.

## 3. The spec-driven loop (every task)

```
read PROJECT_STATUS → read feature spec/design/status → (ask) → plan → build + test → verify → sync docs → log status
```

1. **Orient** — `docs/PROJECT_STATUS.md`, then only the relevant `docs/features/<name>/{spec,design,status}.md`. Don't load the whole repo.
2. **No code without an agreed spec.** New feature → `feature-start` workflow. Spec + design are agreed with the human before implementation.
3. **Build** surgically, per `design.md`. Tests prove each acceptance criterion in `spec.md`.
4. **Verify** — run tests/lint; show evidence. Never claim done without it.
5. **Sync docs in the same change** — follow the `docs-sync` skill (update matrix in `docs/README.md`).
6. **Log** — short entry in `status.md` → "Resume here" must let the next agent continue from docs alone.

Trivial changes (typo, dependency bump, one-line fix with no behaviour change) skip spec/design but still get a CHANGELOG line if user-visible.

## 4. Always-on rules (digest — full text in `.agents/RULES.md`)

00 Ask, don't assume · 01 Spec before code · 02 Docs are part of done · 03 Single source of truth ·
04 Surgical & simple · 05 Evidence before claims · 06 Security & secrets · 07 Scope discipline ·
08 Close the lessons loop · 10+ project-specific rules.

## 5. Workflows (invocable)

| Workflow | Use when |
|---|---|
| `project-init` | Brand-new project — interview the human, fill PRD + HLD + AGENTS §1 |
| `status` | "Where are we?" — read-only status report |
| `resume` | Pick up where the last session left off |
| `feature-start <name>` | Scaffold a feature, draft its spec |
| `feature-design <name>` | Write the feature's `design.md` (HLD/LLD) after spec agreed |
| `feature-complete <name>` | Verify, write `guide.md`, sync docs, flip to ✅ |
| `docs-sync` | Audit + fix doc drift for the current diff |
| `adr-new <title>` | Record a cross-feature decision |
| `lesson <summary>` | Capture a lesson learned (and promote it) |

Claude Code exposes these as `/slash-commands`; other agents: open `.agents/workflows/<name>.md` and follow it.

## 6. Roles (delegate specialist work)

`architect` (specs/design/ADRs, no app code) · `implementer` (builds per design) · `test-engineer` ·
`reviewer` (read-only, BLOCK/PASS) · `docs-keeper` (doc drift audit). Definitions: `.agents/roles/`.
Split `implementer` into domain roles (backend/frontend/data…) as the project grows.

## 7. Project-specific notes

<!-- FILL: anything an agent MUST know that has no better home yet. Prefer moving it to RULES/skills/docs. -->
