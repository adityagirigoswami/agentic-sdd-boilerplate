# Rules — always apply

> Always-on guardrails for every agent and every task. Referenced from `AGENTS.md §4`.
> Rules are **short and enforceable**. Procedures belong in `skills/`; facts belong in `docs/`.
> New rules usually arrive via the lessons loop (Rule 08) — note the lesson ID next to the rule.

## Core rules (keep)

**00 Ask, don't assume** — Missing, ambiguous, conflicting, or doubtful → stop and ask. Offer options with
trade-offs and a recommendation. Never invent requirements, acceptance criteria, or business rules.

**01 Spec before code** — No implementation without an agreed `docs/features/<name>/spec.md` (WHAT) and,
for non-trivial work, an agreed `design.md` (HOW). "Agreed" = the human said yes; record it in `status.md`.
Trivial changes (typo, dep bump, one-line fix with no behaviour change) are exempt.

**02 Docs are part of done** — A change is not done until every doc it affects is updated *in the same
change* (matrix: `docs/README.md#update-matrix`). Code and docs disagree → docs are a bug; fix them.

**03 Single source of truth** — Each fact has exactly one owner doc. Link, don't copy. Don't restate
schema in a spec, or API shapes in a guide — link `architecture/schema.md` / `api.md`.

**04 Surgical & simple** — Minimum code that solves the task. Touch only what the task needs; match the
existing style; no speculative abstractions, flags, or config. Mention unrelated problems — don't fix them
silently. Remove only orphans your change created. Imports at top of file.

**05 Evidence before claims** — Run the tests/lint/build and show the output before saying "done",
"fixed", or "passing". Every acceptance criterion in `spec.md` maps to a test or a recorded manual check.

**06 Security & secrets** — Never read, print, or commit secrets; `.env*` (except `.env.example`) is
off-limits. Validate untrusted input at boundaries. Secrets/keys stay server-side. No PII in logs.
Destructive or outward-facing actions (deploy, push, delete data, migrations on shared DBs) → ask first.

**07 Scope discipline** — Build only what the spec's **In** list says. Anything on the PRD non-goals or the
spec's **Out** list is not built; if a task implies it, ask.

**08 Close the lessons loop** — When something breaks in a non-obvious way, or the human corrects you:
fix it, then add an entry to `docs/LESSONS.md`. If it could recur, promote it — to a rule here, a skill
step, or a checklist item — and link the lesson ID.

## Status-doc hygiene (learned the hard way)

**09 Keep status docs resumable, not encyclopaedic** — `status.md` "Resume here" ≤ 10 lines and always
current. Work-log entries ≤ ~8 lines, newest first. Long explanations go to `design.md` (why) or
`guide.md` (how it works). Feature-local decisions → `design.md` decision log; cross-feature → ADR.
`PROJECT_STATUS.md` notes column: one line per feature.

## Project-specific rules (10+)

<!-- FILL: domain guardrails, e.g.
**10 Tenant isolation** — every query on tenant-owned data filters tenant_id from auth context. (L-0003)
**11 LLM calls** — go through the single client; structured output; validate before persist; log every call.
-->
