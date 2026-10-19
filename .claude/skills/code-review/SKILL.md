---
name: code-review
description: Use when reviewing a diff, branch, or PR — your own before declaring done, or someone else's. Checks correctness, security, simplicity, spec conformance, tests, and doc sync. One line per finding, severity-tagged, BLOCK/PASS verdict.
---

<!-- GENERATED from .agents/skills/code-review/SKILL.md by scripts/sync_agents.py — edit the source, then run `make sync-agents`. -->

# Code review

## Gather

1. Diff: `git diff <base>...HEAD` (or `gh pr diff <n>`). Changed-files list.
2. The feature's `spec.md` (acceptance criteria) and `design.md` (intended approach).

## Review against

- **Correctness** — logic, edge cases, error paths, concurrency/async, resource cleanup.
- **Spec conformance** — every AC implemented and tested; nothing from **Out** built (Rule 07).
- **Design conformance** — follows `design.md`; deviations recorded in its decision log.
- **Security** (Rule 06) — input validation, authz, secrets, injection, PII in logs.
- **Simplicity** (Rule 04) — speculative abstractions, unrelated edits, dead code, orphan imports.
- **Tests** (Rule 05) — meaningful, deterministic, cover failure paths.
- **Docs** (Rule 02) — matrix rows for this diff updated; `status.md` updated.
- **Project rules** — RULES.md §10+.

## Output

One line per finding: `path:line: <critical|major|minor>: <problem>. <fix>.`
No praise, no style nits unless they change meaning.
**Verdict:** `BLOCK` on any critical/major correctness, security, or missing-test issue; otherwise `PASS`
with optional follow-ups.
