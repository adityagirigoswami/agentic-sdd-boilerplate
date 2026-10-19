---
description: Scaffold a new feature (spec/design/status/guide from template), register it in PROJECT_STATUS, and draft its spec with the human. No application code.
argument-hint: "<feature-name>"
---

# Workflow: feature-start

Feature: $ARGUMENTS

1. Validate the name: kebab-case, not overlapping an existing feature in `docs/PROJECT_STATUS.md`.
   Overlap or unclear → ask (Rule 00).
2. Scaffold: `python3 scripts/new_feature.py $ARGUMENTS` (copies `docs/features/_TEMPLATE/`, adds the
   index row with ⬜).
3. Draft `spec.md` from PRD + conversation: Goal, Scope In/Out, user stories, requirements with
   acceptance criteria (AC-n), rules that apply, dependencies.
   **Do not invent acceptance criteria** — propose them clearly marked as proposals and ask.
4. Put every unknown in "Open questions".
5. Ask the human to confirm Scope + Requirements + ACs. On approval:
   tick "Spec agreed (date)" in `status.md`, set status 🟡, update the index row.
6. Suggest next: `feature-design $ARGUMENTS` (or straight to build if trivially small — say why).

Do not write application code in this workflow.
