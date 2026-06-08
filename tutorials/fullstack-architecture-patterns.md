# Fullstack Architecture Patterns

## Goal

Design fullstack systems with clear boundaries across UI, API, data, and operations.

## Pattern Map

| Concern | Skill |
| --- | --- |
| Scope and contracts | fullstack-product-specification |
| Frontend architecture | react-nextjs-frontend-architecture |
| Backend services | nodejs-nestjs-backend-microservices |
| API compatibility | api-contract-first-development |
| Auth and access | authentication-and-authorization-fullstack |

## Workflow

1. Define bounded contexts and ownership.
2. Lock API contracts before UI implementation details.
3. Implement vertical slices with tests at each boundary.
4. Review with `references/fullstack-architecture-review-checklist.md`.

## Exit Signal

Teams can ship independently across UI and backend without contract drift.
