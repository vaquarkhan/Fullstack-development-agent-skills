---
name: microservice-patterns-outbox-and-cdc
description: Publish reliable domain events using outbox and CDC patterns to avoid dual-write failures. Use when transactional updates must trigger downstream processing.
disable-model-invocation: true
---

# Microservice Patterns Outbox And CDC

## Use When

- Service writes to database and emits events
- Event delivery reliability is critical for downstream systems

## Workflow

1. Store domain event in outbox table in same transaction as data change.
2. Relay outbox entries through CDC or polling worker.
3. Publish to broker with ordering and partition strategy.
4. Track delivery state and retries with poison-message handling.
5. Add replay and reconciliation jobs for missed events.

## Required Checks

- No dual-write path bypasses outbox transaction
- Relay worker is idempotent and restart-safe
- Backlog metrics and alert thresholds are configured

## Exit Criteria

- Event publishing survives process and network failures
- Consumers can recover using replay-safe semantics
