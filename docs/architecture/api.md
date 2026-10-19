# {{PROJECT_NAME}} — Interfaces (canonical)

> Endpoints, events, and other contracts. Feature docs **link here**. Update in the same change as the code.

**Last updated:** YYYY-MM-DD

## Conventions

- Base path / versioning: e.g. `/api/v1`.
- Auth: e.g. `Authorization: Bearer <jwt>`.
- Errors: e.g. `{ "error": { "code": "string", "message": "string", "details": {} } }`.
- Pagination, filtering, idempotency keys: …

## Endpoints

| Method | Path | Auth / permission | Request | Response | Feature |
|---|---|---|---|---|---|
| GET | `/health` | none | — | `200 {status}` | — |

## Events / messages

| Name | Producer | Consumers | Payload | Delivery guarantees |
|---|---|---|---|---|

## External integrations

| System | Direction | Protocol | Auth | Rate limits |
|---|---|---|---|---|
