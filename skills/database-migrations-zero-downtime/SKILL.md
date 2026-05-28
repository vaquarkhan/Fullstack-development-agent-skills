---
name: database-migrations-zero-downtime
description: Plan and execute zero-downtime schema and data migrations for fullstack applications. Use when evolving production schemas without service interruption.
disable-model-invocation: true
---

# Database Migrations Zero Downtime

## Use When

- Changing schema used by active production services
- Migrating large tables or high-traffic query paths

## Workflow

1. Choose compatible migration strategy (expand, migrate, contract).
2. Add backward-compatible reads and writes.
3. Run data backfill in controlled batches.
4. Verify application compatibility across versions.
5. Remove old schema only after rollout validation.

## Required Checks

- Previous app version can still operate during migration
- Backfill is resumable and idempotent
- Rollback path is documented with trigger thresholds

## Exit Criteria

- Migration executes without downtime
- Schema cleanup is completed after verification window
