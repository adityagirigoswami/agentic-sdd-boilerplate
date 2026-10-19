---
description: Initialize a brand-new project — interview the human, then fill PRD, HLD, AGENTS.md §1, and the first milestones/features. Run once, right after cloning the boilerplate.
argument-hint: "[one-line project idea]"
---

<!-- GENERATED from .agents/workflows/project-init.md by scripts/sync_agents.py — edit the source, then run `make sync-agents`. -->

# Workflow: project-init

Idea (may be empty): $ARGUMENTS

Do **not** write application code in this workflow.

1. If `{{PROJECT_NAME}}` placeholders remain, ask for the project name and run
   `python3 scripts/bootstrap.py "<name>"`.
2. **Interview** the human in small batches (≤ 4 questions at a time), until you can fill each section:
   - Problem, users, key flows → PRD §1–3
   - Goals vs explicit non-goals → PRD §2
   - Functional requirements (numbered FR-n) and NFRs (performance, security, availability, cost) → PRD §4–5
   - Stack + hosting constraints, existing systems to integrate → HLD
   - Milestones and what "MVP done" means → PRD §6
   Offer options with a recommendation when they're unsure. Never fill a section with invented facts —
   leave `<!-- OPEN: … -->` and list it under PRD "Open questions".
3. Write `docs/product/PRD.md`, `docs/architecture/HLD.md` (context + containers + main flows), and
   `AGENTS.md §1` (what / stack / commands).
4. Record each stack choice as an ADR (`adr-writing` skill) — status `Proposed` until confirmed.
5. Fill `docs/PROJECT_STATUS.md` milestones; for each MVP feature run `python3 scripts/new_feature.py <name>`
   (creates folder + index row, status ⬜).
6. Add project-specific guardrails to `.agents/RULES.md` §10+ if the domain needs them (multi-tenancy,
   PII, payments, LLM calls…). Then `make sync-agents`.
7. Run `make docs-check`. Summarize: what's filled, what's open, suggested first feature.
