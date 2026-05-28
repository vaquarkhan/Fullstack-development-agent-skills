---
name: cqrs-and-event-sourcing-patterns
description: Apply CQRS and event sourcing for complex domains that require auditability, temporal queries, and scalable read models. Use when write and read concerns diverge significantly.
disable-model-invocation: true
---

# CQRS And Event Sourcing Patterns

## Use When

- Domain behavior requires immutable event history
- Query shapes differ heavily from command workflows

## Workflow

1. Define command model invariants and event schema strategy.
2. Persist domain events as source of truth.
3. Build projections for query-optimized read models.
4. Design replay, snapshot, and projection catch-up operations.
5. Implement versioning and backward-compatible event evolution.

## Required Checks

- Event schemas include versioning and migration policy
- Projection rebuild process is tested and bounded
- Command-side validation prevents invalid state transitions

## Exit Criteria

- System can replay history to restore consistent state
- Query performance improves without compromising write integrity
