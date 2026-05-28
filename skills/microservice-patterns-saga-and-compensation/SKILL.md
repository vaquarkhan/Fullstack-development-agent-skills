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

## Required Checks

- Compensation actions are business-correct and reversible where needed
- Duplicate and out-of-order events do not corrupt state
- Saga progress is traceable by correlation ID

## Exit Criteria

- Multi-service workflow is eventually consistent and recoverable
- Operational runbook exists for failed sagas
