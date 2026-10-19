---
name: spec-workflow
description: Use at the START and END of any development task — starting a feature, resuming work, fixing a bug, or finishing a change. The tracking spine that prevents context loss — orient from PROJECT_STATUS, work from the feature spec/design, leave status.md resumable.
---

# Spec workflow — the tracking spine

Goal: the next agent (or you, tomorrow) resumes from docs alone, without re-reading the repo or chat.

## Start of task

1. Read `docs/PROJECT_STATUS.md`. Find the feature this task belongs to (or note there is none).
2. Read that feature's `status.md` → **"Resume here"** first, then `spec.md`, then `design.md`.
   Read only these plus docs they link. Don't crawl the repo.
3. Check which `.agents/RULES.md` rules apply (spec lists them under "Rules that apply").
4. Gate check:
   - No feature / no spec → run the `feature-start` workflow. Do not code.
   - Spec not marked agreed in `status.md` checklist → get agreement first (Rule 01).
   - Non-trivial and no agreed `design.md` → run `feature-design`.
   - Anything unclear → ask (Rule 00).
5. Bug fix with no feature? Attach it to the closest feature's `status.md`; if none fits, log in
   `CHANGELOG.md` and (if non-obvious) `docs/LESSONS.md`.

## During work

- Follow `design.md`. If reality forces a different design → stop, update `design.md` decision log, tell
  the human. Don't silently diverge.
- Surgical changes (Rule 04). Delegate domain work to `.agents/roles/`.
- Long task? Write a dated plan in `docs/plans/` and link it from `status.md`.

## End of task (before saying "done")

1. Verify — run tests/lint; keep the output (Rule 05).
2. Run the `docs-sync` skill: walk the update matrix in `docs/README.md` for your diff.
3. `status.md`: rewrite **Resume here** (state · next step · blockers), add a short work-log entry,
   tick checklist items that are genuinely done, bump **Last updated**.
4. `PROJECT_STATUS.md`: status emoji + one-line note match `status.md`.
5. Hit a non-obvious problem? `lesson-capture` skill.
6. Feature finished → `feature-complete` workflow.

## Checklist (track as todos)

- [ ] Oriented: PROJECT_STATUS → status → spec → design
- [ ] Gates passed (spec agreed, design agreed, no open questions)
- [ ] Built per design, surgical
- [ ] Tests cover acceptance criteria; output shown
- [ ] Docs synced (matrix walked)
- [ ] status.md Resume-here + log + checklist updated; index matches
