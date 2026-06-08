# Case Study: Payments Subscription Reliability

## Context

A subscription product must process provider webhooks reliably under retries and duplicates.

## Applied Assets

- Starter pack: `starter-packs/payments-and-subscriptions-starter.yaml`
- Skills: payments-and-webhook-reliability, api-contract-first-development
- Checklist: `references/microservice-reliability-checklist.md`

## Delivery Sequence

1. Define payment state machine and idempotency keys.
2. Implement signed webhook ingestion and replay-safe handlers.
3. Add reconciliation job for delayed or missing events.
4. Validate duplicate delivery and provider outage scenarios.

## Outcome Metrics

- No duplicate charge incidents in replay tests
- Reconciliation backlog alert threshold defined
- Finance audit trail complete for state transitions
