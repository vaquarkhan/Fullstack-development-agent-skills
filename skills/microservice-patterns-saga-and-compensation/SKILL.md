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

## Decision Framework

- Prefer choreography when domain ownership is clear and event contracts are mature.
- Prefer orchestration when visibility, sequencing, and centralized recovery are required.
- Use compensation for business reversal, not technical rollback assumptions.
- Model irreversibility explicitly for steps like external settlement or notifications.

## Common Rationalizations And Rebuttals

- "A single DB transaction is easier." -> It does not scale across services; use saga for distributed consistency.
- "Compensation is just delete the row." -> Real workflows need business-level reversal semantics.
- "Event ordering is guaranteed." -> Assume disorder and duplication; enforce idempotent handlers.

## Evidence Pack

- Saga state machine diagram with terminal and failure states
- Compensation matrix by step and side effect
- Replay test evidence with duplicate and out-of-order event scenarios
- Operational playbook for stuck or poisoned saga execution

## Exit Criteria

- Multi-service workflow is eventually consistent and recoverable
- Operational runbook exists for failed sagas
