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

- Start with clear scope and ownership boundaries.
- Prefer incremental, testable slices over broad rewrites.
- Define compatibility and rollback expectations before release.
- Require evidence for reliability and operability outcomes.

## Common Rationalizations And Rebuttals

- "We can fill gaps after merge." -> Critical gaps are harder and riskier to fix in production.
- "This change is too small for process." -> Small changes still need clear validation criteria.
- "Docs can wait." -> Missing context increases future delivery and incident cost.

## Evidence Pack

- Scope and acceptance criteria with owner
- Test or validation evidence for changed behavior
- Compatibility and rollback notes
- Operational visibility requirements for production impact

## Exit Criteria

- Migration executes without downtime
- Schema cleanup is completed after verification window
