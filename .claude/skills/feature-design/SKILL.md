---
name: feature-design
description: Use when writing or revising a feature's design.md — the feature-level HLD and LLD (components, flows, data, interfaces, error handling, alternatives, decision log) — after its spec is agreed and before implementation.
---

<!-- GENERATED from .agents/skills/feature-design/SKILL.md by scripts/sync_agents.py — edit the source, then run `make sync-agents`. -->

# Feature design — HLD + LLD for one feature

`spec.md` says WHAT; `design.md` says HOW, at the level a reviewer can approve and an implementer can
follow without guessing.

## Steps

1. Read the agreed `spec.md`, `architecture/HLD.md`, `LLD.md`, `schema.md`, `api.md`, and relevant ADRs.
2. Read the code areas the feature touches (find existing patterns to reuse — don't invent new ones).
3. Fill `docs/features/<name>/design.md` from the template:
   - **HLD:** where it sits in the system, a mermaid component/sequence diagram, the main flow.
   - **LLD:** files/modules to add or change, data model delta, interface contracts, key algorithms,
     error handling & idempotency, config, security, observability.
   - **Alternatives considered** — at least one, with why rejected.
   - **Test strategy** — map each acceptance criterion (AC-n) from spec to a test.
   - **Rollout** — migration/backfill, flags, backwards compatibility.
4. Changes to shared schema/API: write the *delta* in design.md; the canonical doc is updated when built.
5. Decision that affects other features → ADR, link it.
6. Present the design to the human; on approval tick "Design agreed" in `status.md` with the date.

## Gotchas

- Don't design beyond the spec's **In** list (Rule 07).
- Name real file paths. "Add a service" is not a design; `src/billing/invoice_service.py::create()` is.
- Unknowns go in "Open questions" — ask, don't assume.
