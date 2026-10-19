---
description: Audit and fix documentation drift for the current diff (or a named feature) using the update matrix, then run docs-check.
argument-hint: "[feature-name | diff]"
---

<!-- GENERATED from .agents/workflows/docs-sync.md by scripts/sync_agents.py — edit the source, then run `make sync-agents`. -->

# Workflow: docs-sync

Target: $ARGUMENTS (default: current working diff)

1. Apply the `docs-sync` skill to the target. Delegate a read-only audit to `docs-keeper` for large diffs.
2. Fix drift directly in the owner docs. Spec (contract) changes → ask before editing.
3. `make docs-check` → fix all errors; report warnings.
4. Report: docs updated, drift found and fixed, anything needing a human decision.
