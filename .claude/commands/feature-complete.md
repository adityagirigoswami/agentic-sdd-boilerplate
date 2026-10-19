---
description: Finalize a feature — verify every acceptance criterion with evidence, write guide.md (how it works, as built), sync all docs, flip status to done.
argument-hint: "<feature-name>"
---

<!-- GENERATED from .agents/workflows/feature-complete.md by scripts/sync_agents.py — edit the source, then run `make sync-agents`. -->

# Workflow: feature-complete

Feature: $ARGUMENTS

1. Open `docs/features/$ARGUMENTS/spec.md` + `status.md`. For **each** acceptance criterion, point to the
   test or recorded manual check that proves it. Any unproven → stop, report, do not mark complete.
2. Run the full test suite + lint; show the output (Rule 05).
3. Write/refresh `guide.md` — how it works **as built**: end-to-end flow, file map, key code paths,
   config, how to run/test, troubleshooting, known limitations.
4. Run `docs-sync` (HLD/LLD/schema/api/CHANGELOG/runbook as the diff requires).
5. Review: delegate to the `reviewer` role (or record the human PR review — reviewer names + PR link).
6. Set ✅ in `status.md` (header + checklist) and in `PROJECT_STATUS.md`; add a CHANGELOG entry.
7. Anything learned along the way → `lesson-capture`.
8. `make docs-check` must pass. Summarize what shipped + docs touched.
