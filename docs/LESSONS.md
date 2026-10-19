# Lessons Learned

> What burned us, why, and what we changed so it can't happen again. Newest first.
> Add via the `lesson-capture` skill / `lesson` workflow. Promote recurring lessons into
> `.agents/RULES.md`, a skill, or the runbook — and record where in **Action**.

## Entry format

```
### L-NNNN — <short title> (YYYY-MM-DD)
- **Context:** feature / area / task
- **What happened:** symptom
- **Root cause:** the real cause
- **Lesson:** the generalizable takeaway
- **Action:** promoted to RULES §NN / skill <name> / runbook / ADR-NNNN / none (one-off)
- **Tags:** #area #type
```

## Entries

<!-- LESSONS:START -->
### L-0001 — Status logs bloat until nobody can resume from them (YYYY-MM-DD)
- **Context:** inherited from earlier agent-driven projects.
- **What happened:** feature `status.md` files grew to hundreds of lines; decisions and explanations were buried in the progress log; index notes became paragraphs.
- **Root cause:** one file used for progress, design rationale, and as-built explanation.
- **Lesson:** separate PROGRESS (status) from WHY (design/ADR) and HOW-IT-WORKS (guide); keep a short "Resume here".
- **Action:** promoted to RULES §09; templates split into spec/design/status/guide.
- **Tags:** #docs #process
<!-- LESSONS:END -->
