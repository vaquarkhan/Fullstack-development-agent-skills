# Example: Payments Webhook Platform

## Architecture

- Billing API manages subscription lifecycle
- Webhook ingress validates signatures and stores event receipts
- Reconciliation worker repairs delayed or missing events

## Skills Used

- payments-and-webhook-reliability
- microservice-patterns-outbox-and-cdc
- incident-triage-and-oncall-runbooks

## Validation Focus

- Duplicate webhook replay safety
- Idempotent state transitions
- Reconciliation alert thresholds
