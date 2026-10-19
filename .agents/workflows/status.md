---
description: Read-only project status report — phase, features by status, blockers, open questions, suggested next action.
---

# Workflow: status

Read-only. Do not modify files.

1. Read `docs/PROJECT_STATUS.md`.
2. For each 🟡 / ⛔ feature, read the "Resume here" block of its `status.md`.
3. Report concisely:
   - Phase / current milestone.
   - Features grouped ✅ / 🟡 / ⬜ / ⛔ / 🅿️ / ♻️.
   - Blockers and open questions (feature `status.md` + PRD "Open questions").
   - Drift: index vs `status.md` mismatches, 🟡 features not updated in > 14 days (`make docs-check` shows these).
   - **Suggested next action** (one).
4. If the index looks stale, say so and offer to run `docs-sync`.
