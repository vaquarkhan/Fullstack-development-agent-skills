---
name: microservice-patterns-saga-and-compensation
description: Coordinate distributed business transactions with saga choreography or orchestration and reliable compensation logic. Use when workflows span multiple services with partial-failure risk.
disable-model-invocation: true
---

# Microservice Patterns Saga And Compensation

## Use When

- Business workflow updates data in multiple services
- Two-phase commit is not feasible or too costly

## Workflow

1. Define local transactions and compensation actions for each step.
2. Choose choreography or orchestration based on ownership and visibility needs.
3. Persist saga state and step execution history.
4. Implement idempotent command and event handlers.
5. Add timeout, retry, and dead-letter handling for stuck steps.

## Pattern Selection Guide

- Prefer choreography when domain ownership is clear and event contracts are mature.
- Prefer orchestration when visibility, sequencing, and centralized recovery are required.
- Use compensation for business reversal, not technical rollback assumptions.
- Model irreversibility explicitly for steps like external settlement or notifications.

## Required Checks

- Compensation actions are business-correct and reversible where needed
- Duplicate and out-of-order events do not corrupt state
- Saga progress is traceable by correlation ID

## Common Rationalizations And Rebuttals

- "A single DB transaction is easier." -> It does not scale across services; use saga for distributed consistency.
- "Compensation is just delete the row." -> Real workflows need business-level reversal semantics.
- "Event ordering is guaranteed." -> Assume disorder and duplication; enforce idempotent handlers.

## Evidence Pack

- Saga state machine diagram with terminal and failure states
- Compensation matrix by step and side effect
- Replay test evidence with duplicate and out-of-order event scenarios
- Operational playbook for stuck or poisoned saga execution

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

- Multi-service workflow is eventually consistent and recoverable
- Operational runbook exists for failed sagas
