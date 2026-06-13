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

## Decision Framework

- Prefer expand-migrate-contract over big-bang DDL; never drop old columns until all readers and writers are migrated.
- For constraint changes use NOT VALID then VALIDATE CONSTRAINT to avoid long locks on hot tables.
- Run dual-write or dual-read windows when application versions overlap during rollout.
- Use resumable batch backfills with keyed cursors; set lock_timeout and statement_timeout on migration sessions.

## Common Rationalizations And Rebuttals

- "We can run the ALTER in a maintenance window." -> Maintenance windows still hurt SLOs; expand/contract avoids hard downtime.
- "Shadow reads are overkill." -> Shadow reads catch semantic drift before cutover; skip them only for low-risk columns.
- "Rollback is just restore backup." -> Backups miss in-flight writes; document expand-phase rollback that preserves data.

## Evidence Pack

- Expand/migrate/contract plan with phase gates and app version matrix
- Backfill job config: batch size, cursor key, idempotency proof, resume test
- Shadow-read or dual-write validation results with mismatch counts
- DDL scripts with lock_timeout/statement_timeout settings and estimated row impact

## Exit Criteria

- Migration executes without downtime
- Schema cleanup is completed after verification window
