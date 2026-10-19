---
name: adr-writing
description: Use when a decision affects more than one feature or is hard to reverse — choosing a library, datastore, framework, protocol, architecture pattern, or changing a previous decision. Records it as an Architecture Decision Record in docs/decisions/.
---

<!-- GENERATED from .agents/skills/adr-writing/SKILL.md by scripts/sync_agents.py — edit the source, then run `make sync-agents`. -->

# ADR writing

ADRs capture *why* — so nobody re-litigates a decision, and anyone can see when it's time to revisit it.

## When

- Affects >1 feature, or is costly to reverse, or the human debated options → ADR.
- Local to one feature → a row in that feature's `design.md` decision log instead.

## Steps

1. `make adr title="<decision in imperative>"` (or `python3 scripts/new_adr.py "<title>"`).
2. Fill: Context (forces, constraints) · Decision · Options considered (pros/cons) · Consequences
   (good, bad, follow-ups) · Revisit when.
3. Status starts `Proposed`; becomes `Accepted` when the human agrees.
4. Superseding? New ADR with `Supersedes: ADR-NNNN`; set the old one to `Superseded by ADR-MMMM`.
   Never edit an accepted ADR's decision — write a new one.
5. Link the ADR from the docs it shapes (HLD/LLD/design.md).
