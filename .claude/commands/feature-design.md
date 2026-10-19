---
description: Write the feature's design.md (feature-level HLD + LLD) after its spec is agreed, and get it approved before implementation.
argument-hint: "<feature-name>"
---

<!-- GENERATED from .agents/workflows/feature-design.md by scripts/sync_agents.py — edit the source, then run `make sync-agents`. -->

# Workflow: feature-design

Feature: $ARGUMENTS

1. Confirm `docs/features/$ARGUMENTS/status.md` has "Spec agreed" ticked. If not → stop, run `feature-start`.
2. Apply the `feature-design` skill to fill `design.md` (delegate to the `architect` role if available).
3. For work spanning > ~1 day, also write a step-by-step plan at
   `docs/plans/YYYY-MM-DD-$ARGUMENTS.md` (tasks with file paths + verification per step) and link it in
   `status.md`.
4. Present the design summary + open questions. On approval: tick "Design agreed (date)" in `status.md`.

No application code until the design is agreed.
