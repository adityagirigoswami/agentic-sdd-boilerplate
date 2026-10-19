---
name: lesson-capture
description: Use when something broke in a non-obvious way, a fix took multiple attempts, a wrong assumption was discovered, or the human corrected the agent. Records a lesson in docs/LESSONS.md and promotes it to a rule, skill step, or checklist so it can't recur.
---

# Lesson capture — close the loop

A bug fixed without a lesson is a bug that comes back.

## Steps

1. Append a new entry at the **top** of `docs/LESSONS.md` (next free `L-NNNN`), using the entry format
   in that file: context · what happened · root cause · lesson · action · tags.
2. Decide promotion (pick the strongest that fits):
   - Could recur anywhere → rule in `.agents/RULES.md` (10+), cite the lesson ID.
   - Recurs in one kind of task → add a step/gotcha to the relevant skill.
   - Environment/ops issue → `docs/operations/runbook.md`.
   - Design-level → ADR or `design.md` decision log.
   - One-off → no promotion; say so in "Action".
3. If you changed `.agents/`, run `make sync-agents`.
4. Tell the human the lesson ID and where it was promoted.

## Gotchas

- Root cause, not symptom. "Test failed" is a symptom; "fixture reused a DB session across tenants" is a cause.
- Keep each entry ≤ 10 lines. Link the PR/commit/feature for detail.
