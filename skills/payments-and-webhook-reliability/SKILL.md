---
name: payments-and-webhook-reliability
description: Implement reliable payment and webhook flows with idempotency, reconciliation, and failure recovery. Use when integrating billing providers and processing external payment events.
disable-model-invocation: true
---

# Payments And Webhook Reliability

## Use When

- Integrating checkout, subscription, or invoice workflows
- Consuming asynchronous webhook events from payment providers

## Workflow

1. Define payment state machine and idempotency keys.
2. Verify webhook signatures and reject malformed payloads.
3. Persist event receipts and process with retry-safe handlers.
4. Add reconciliation jobs for missing or delayed events.
5. Instrument alerts for failed settlements and event lag.

## Required Checks

- Duplicate webhook deliveries do not double-charge users
- Payment state transitions are auditable and reversible when possible
- Reconciliation path is documented and tested

## Decision Framework

- Model payments as a state machine with idempotency keys on every mutation path.
- Verify webhook signatures before persistence; store raw payloads for audit and replay.
- Run reconciliation jobs for missing, delayed, or out-of-order provider events.
- Never double-apply financial state on duplicate webhook delivery.

## Common Rationalizations And Rebuttals

- "Provider guarantees exactly-once." -> All major providers retry; design for at-least-once delivery.
- "We can reconcile manually." -> Manual reconciliation does not scale and misses subtle drift; automate daily diffs.
- "Refunds can reuse charge handlers." -> Refunds have distinct states and idempotency rules; separate handlers and tests.

## Evidence Pack

- Payment state diagram with terminal states and idempotency key placement
- Webhook signature verification and replay test results (duplicate delivery scenarios)
- Reconciliation job output showing matched, missing, and disputed events
- Audit log samples for charge, refund, and dispute transitions

## Exit Criteria

- Payment flow is resilient to retries, reordering, and transient outages
- Finance-impacting errors are detectable and recoverable
