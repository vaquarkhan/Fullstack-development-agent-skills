---
name: serverless-event-driven-and-workflow-orchestration
description: Design event-driven serverless workflows with queues, topics, schedulers, and orchestration patterns across cloud providers.
disable-model-invocation: true
---

# Serverless Event Driven And Workflow Orchestration

## Use When

- Async domain workflows and integrations
- Need reliable processing under retries and spikes

## Workflow

1. Define event contracts and versioning policy
2. Choose queue vs topic vs workflow engine per use case
3. Implement idempotent consumers and poison-message handling
4. Add observability for lag, age, and failure rates
5. Run chaos drills for broker outage and backlog catch-up

## Required Checks

- Every consumer is idempotent
- DLQ and replay procedures are documented
- Backpressure strategy protects downstream systems
- Scheduling and ordering assumptions are explicit

## Decision Framework

- Use choreography for loosely coupled domains
- Use orchestration when step visibility and recovery are critical
- Cap retry attempts with jitter and budgets
- Alert on consumer lag before user impact

## Common Rationalizations And Rebuttals

- "At-least-once is good enough without idempotency." -> Duplicates will corrupt state.
- "We can process events synchronously for simplicity." -> Spikes will cascade failures.
- "DLQ review is optional." -> Poison messages will stall pipelines silently.

## Evidence Pack

- Contract compatibility note
- Replay test output with duplicate events
- Lag and DLQ dashboard snapshots
- Runbook for backlog recovery

## Exit Criteria

- Event pipelines are resilient under failure and replay
- Operational ownership is clear per queue/topic
