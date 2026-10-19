---
name: docs-sync
description: Use after any code change and before declaring a task done, or when asked to update/audit docs. Walks the update matrix so architecture, schema, API, feature docs, changelog, and lessons stay in step with the code.
---

# Docs sync — keep docs true in the same change

Docs that lag the code are a bug (Rule 02). This runs at the end of every task.

## Steps

1. List what changed: `git status --short` and `git diff --stat` (include staged).
2. For each change, find its row in **`docs/README.md#update-matrix`** and update the owner doc.
   Quick version:

   | You changed | Update |
   |---|---|
   | Feature behaviour / scope | `features/<f>/spec.md` (ask first — spec is a contract) |
   | How a feature is built | `features/<f>/design.md` (+ decision log row) |
   | Progress of any kind | `features/<f>/status.md` |
   | Tables, columns, indexes, migrations | `architecture/schema.md` |
   | Endpoints, events, payloads, CLI | `architecture/api.md` |
   | New component, service, queue, external dependency | `architecture/HLD.md` |
   | Cross-cutting pattern, module layout, config, error model | `architecture/LLD.md` |
   | Env var | `.env.example` + `operations/deployment.md` |
   | Ops procedure, deploy step, incident fix | `operations/runbook.md` |
   | Decision affecting >1 feature | new ADR (`adr-writing` skill) |
   | User-visible change | `CHANGELOG.md` → `[Unreleased]` |
   | Non-obvious failure / correction | `LESSONS.md` (`lesson-capture` skill) |
   | Commands / stack | `AGENTS.md §1` |

3. Link, don't copy (Rule 03). If you're about to paste a schema or payload into a feature doc, link instead.
4. Run `make docs-check` and fix every error.
5. In your final message, list the docs you updated (or "no doc impact" with a reason).

## Gotchas

- `spec.md` is a contract: changing scope/acceptance criteria needs the human's OK. Record it in `status.md`.
- Don't let `status.md` become the design doc. Why → `design.md`; how it works → `guide.md` (Rule 09).
- Renamed/moved a file? grep docs for the old path.
