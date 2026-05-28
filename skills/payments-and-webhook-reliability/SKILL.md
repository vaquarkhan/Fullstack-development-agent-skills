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

## Exit Criteria

- Payment flow is resilient to retries, reordering, and transient outages
- Finance-impacting errors are detectable and recoverable
