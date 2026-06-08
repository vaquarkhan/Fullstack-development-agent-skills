# Postgres, Redis, and Kafka Fullstack Tutorial

## Goal

Wire a typical fullstack backend with relational storage, cache/session layer, and an event backbone.

## Steps

1. Load `starter-packs/data-platform-and-events-starter.yaml`.
2. Apply `postgres-and-relational-data-modeling` for schema and migrations.
3. Add `redis-caching-and-session-store-patterns` for hot reads and sessions.
4. Introduce `kafka-event-backbone-patterns` for cross-service workflows.
5. Validate with `references/microservice-patterns-checklist.md`.

## Exit

- Migrations are expand-migrate-contract safe
- Cache invalidation defined for each write path
- Consumers are idempotent with DLQ handling
