# ADR-0001: Spec-driven, agent-first development workflow

**Status:** Accepted · **Date:** YYYY-MM-DD · **Deciders:** project owner · **Supersedes:** —

## Context

Work is done largely by AI coding agents across sessions and providers. Agents lose context between
sessions, invent requirements when specs are vague, and let docs drift from code. Earlier projects showed
specific failure modes: status logs that grew into unreadable essays, decisions buried inside progress logs,
ad-hoc design docs in inconsistent places, and index rows that went stale.

## Decision

- Every feature has four docs: `spec.md` (WHAT), `design.md` (HOW), `status.md` (PROGRESS), `guide.md` (AS-BUILT).
- No implementation without an agreed spec (and design for non-trivial work).
- Docs update in the same change as code, per the update matrix in `docs/README.md`.
- Agent instructions live once in `AGENTS.md` + `.agents/`; provider files point there; `.claude/` is generated.
- Cross-feature decisions are ADRs; lessons learned are logged and promoted into rules/skills.
- `make docs-check` runs in CI.

## Options considered

| Option | Pros | Cons |
|---|---|---|
| Spec-driven + generated agent config (chosen) | resumable, provider-neutral, enforced | upfront doc effort |
| Code-first, docs later | fast start | docs rot; agents guess |
| Per-provider config only (`.claude/` only) | simple | locks in one tool; duplication when adding others |

## Consequences

- **Good:** any agent resumes from docs alone; decisions are traceable; drift is caught in CI.
- **Bad:** more files per feature; discipline needed to keep status docs short (Rule 09).
- **Follow-ups:** tune `docs_check.py` rules to the project; add domain rules/skills/roles.

## Revisit when

Doc upkeep cost clearly exceeds the value (e.g. a solo throwaway prototype).
