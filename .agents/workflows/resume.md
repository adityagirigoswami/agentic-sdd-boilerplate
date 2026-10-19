---
description: Resume work where the last session stopped — find the active feature, load only its docs, restate the next step, and confirm before continuing.
argument-hint: "[feature-name]"
---

# Workflow: resume

Feature (optional): $ARGUMENTS

1. No feature given → read `docs/PROJECT_STATUS.md`; pick the 🟡 feature with the newest
   **Last updated**. Several candidates → ask which.
2. Read its `status.md` (**Resume here** + last 3 work-log entries), then `spec.md`, `design.md`, and any
   active plan in `docs/plans/` linked from status.
3. Check reality vs docs: `git status`, `git log --oneline -10`, current branch. Note mismatches.
4. Tell the human in ≤ 8 lines: where things stand, the next step, blockers, any doc/code mismatch.
5. Wait for a go-ahead, then continue under the `spec-workflow` skill.
