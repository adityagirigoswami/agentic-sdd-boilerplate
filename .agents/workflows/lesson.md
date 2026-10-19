---
description: Capture a lesson learned (bug, wrong assumption, correction) in docs/LESSONS.md and promote it to a rule, skill, or runbook entry.
argument-hint: "<what happened, one line>"
---

# Workflow: lesson

Lesson: $ARGUMENTS

Apply the `lesson-capture` skill. If the summary is thin, reconstruct context from the conversation and
`git log`, and ask the human only for what you can't find.
