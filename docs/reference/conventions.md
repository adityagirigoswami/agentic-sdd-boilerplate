# Conventions

> Code-level conventions. Guardrails (must/never) live in `.agents/RULES.md`; this is the style guide.

**Last updated:** YYYY-MM-DD

## Code style

- Formatter / linter: <tool + config file>. Run: `<cmd>`.
- Typing: <strictness>.
- Naming: files …, classes `PascalCase`, functions `snake_case`/`camelCase`, constants `UPPER_SNAKE`.
- Imports at top of file; no function-local imports except to break a cycle (comment why).

## Project structure

Where new modules, tests, and assets go (mirror `architecture/LLD.md §1`).

## Branches & commits

- Branches: `feat/<feature>`, `fix/<short>`, `docs/<short>`, `chore/<short>`.
- Commits: [Conventional Commits](https://www.conventionalcommits.org/) — `feat(auth): add refresh tokens`.
- One logical change per commit; code + its docs in the same commit/PR.
- PRs use `.github/pull_request_template.md`; CI (`make check`) must pass.

## Dependencies

- Add only with a reason (in the PR); pin versions; prefer the standard library / existing deps.
- Major new dependency → ADR.

## Testing

- Layout: `<tests/ mirrors src/>`. Names describe behaviour.
- Unit tests mock external services; no live network. Integration tests: <how>.
