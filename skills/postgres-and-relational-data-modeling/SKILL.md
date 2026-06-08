---
name: postgres-and-relational-data-modeling
description: Design PostgreSQL schemas, migrations, indexing, and query patterns for fullstack applications with performance and integrity controls.
disable-model-invocation: true
---

# Postgres And Relational Data Modeling

## Use When

- Relational persistence is core to the product
- Schema or query performance issues appear

## Workflow

1. Model entities, constraints, and ownership boundaries
2. Plan migrations with expand-migrate-contract
3. Define indexes and query paths for hot endpoints
4. Add connection pooling and timeout policies
5. Validate backup, restore, and replication assumptions

## Required Checks

- Migrations are backward compatible during rollout
- Indexes reviewed for read/write paths
- Secrets and credentials are not embedded in app code
- Restore drill documented for critical tables

## Decision Framework

- Prefer explicit contracts and compatibility rules before implementation.
- If dependency risk is high, require timeout, retry, and fallback strategy per call path.
- If async messaging is used, require idempotency, replay, and dead-letter handling.
- If traffic patterns are volatile, require load, failover, and scaling validation before ship.

## Common Rationalizations And Rebuttals

- "Retries will handle failures automatically." -> Unbounded retries can amplify outages; use budgets.
- "We can skip runbooks for now." -> Operational ambiguity delays incident recovery.
- "Contract changes are minor." -> Small breaking changes cause broad downstream regressions.

## Evidence Pack

- Contract compatibility note and migration strategy (if applicable)
- Failure-mode test evidence for dependency degradation and recovery
- Observability snapshot (latency, error, saturation, or queue health)
- Rollout and rollback steps with clear trigger thresholds

## Exit Criteria

- Workflow is production-ready with verified evidence
- Operational and security guardrails are in place
- Release and rollback expectations are documented
