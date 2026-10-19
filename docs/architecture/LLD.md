# {{PROJECT_NAME}} — Low-Level Design (cross-cutting)

> System-wide internals every feature builds on. Feature-specific LLD lives in `features/<f>/design.md`.
> Update when you introduce or change a pattern, module boundary, config mechanism, or error model.

**Last updated:** YYYY-MM-DD · **Related:** [HLD](./HLD.md) · [schema](./schema.md) · [api](./api.md)

## 1. Repository / module map

| Path | Responsibility | Depends on |
|---|---|---|
| `src/…` | … | … |

## 2. Layering & dependency rules

e.g. `routes → services → repositories → db`; what may import what.

## 3. Patterns in use

| Pattern | Where | Why |
|---|---|---|
| Repository | `src/…/repo.py` | isolate persistence |

## 4. Error handling

Error types, how they map to API responses, retry/backoff policy, idempotency keys.

## 5. Logging & observability

Logger, structured fields, correlation IDs, metrics, tracing. What must never be logged.

## 6. Configuration

How config loads (env → settings object), precedence, validation. Every var listed in `.env.example`.

## 7. Auth & authorization internals

## 8. Concurrency & background work

## 9. Testing architecture

Test layout, fixtures, what's mocked, test data, CI stages.
