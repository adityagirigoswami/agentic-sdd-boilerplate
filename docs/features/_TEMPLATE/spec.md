# Feature: <name> — Spec (WHAT)

> The **contract**. Stable once agreed; changes are deliberate and recorded in `status.md`.
> Says WHAT and WHY — never HOW (that's `design.md`).

**Status:** ⬜ not started · **Owner:** <agent/person> · **Created:** YYYY-MM-DD · **PRD refs:** FR-?

## Goal

One sentence: what this feature delivers and for whom.

## Background

Why now. Link the PRD section, issue, or conversation that motivated it.

## Scope

**In:**
- …

**Out:** (and which feature/phase owns it)
- …

## User stories

- As a <role>, I want <capability> so that <benefit>.

## Requirements & acceptance criteria

| ID | Requirement | Acceptance criterion (verifiable) |
|---|---|---|
| FR-1 | … | AC-1: Given …, when …, then … |

**Non-functional:** performance, security, accessibility, limits — each with a measurable target.

## Data & interface touchpoints

Which tables / endpoints / events / UI screens this feature reads or changes.
Link `../../architecture/schema.md` and `../../architecture/api.md` — don't restate them.

## Rules that apply

Which `.agents/RULES.md` rules matter here (e.g. 06 security, 10 tenant isolation) and why.

## Dependencies

Features, ADRs, external services this needs.

## Open questions

- [ ] … (Rule 00 — must be answered before the affected part is built)
