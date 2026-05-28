---
name: fullstack-product-specification
description: Define fullstack product changes with clear UI journeys, API contracts, domain model updates, non-functional requirements, and release constraints. Use this before implementation when work spans frontend and backend.
disable-model-invocation: true
---

# Fullstack Product Specification

## Use When

- Work spans UI and backend in one delivery slice
- Requirements are unclear, conflicting, or incomplete
- Teams need a shared source of truth before coding

## Workflow

1. Capture business outcome, user roles, and success metrics.
2. Define journeys and states for each persona (happy path, empty, error, denied).
3. Specify API contracts, including request and response schemas, errors, and versioning.
4. Define domain and persistence impact (new entities, migration, indexing, retention).
5. Set non-functional requirements (latency, throughput, accessibility, security, auditability).
6. Record rollout strategy, migration or backfill needs, and rollback criteria.

## Required Artifacts

- Feature brief with acceptance criteria
- API contract draft (OpenAPI, JSON Schema, or equivalent)
- UI state matrix covering loading, empty, error, and success
- Data model or schema change note
- Rollout and rollback note with decision owner

## Red Flags

- Requirements only describe UI visuals without behavior rules
- Backend assumptions are embedded in frontend code comments only
- API errors and edge cases are not defined
- No migration story for schema or contract changes

## Exit Criteria

- Acceptance criteria are testable and implementation-neutral
- Contract compatibility strategy is documented
- UI and backend ownership boundaries are explicit
- Release risk and rollback path are approved
