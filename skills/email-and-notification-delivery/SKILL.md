---
name: email-and-notification-delivery
description: Deliver reliable email and multi-channel notifications with templates, idempotency, and deliverability controls.
disable-model-invocation: true
---

# Email And Notification Delivery

## Use When

- User-facing alerts and transactional messages
- Marketing or operational notification flows

## Workflow

1. Define notification types and priority classes
2. Use template versioning and localization hooks
3. Implement provider failover and retry policy
4. Track delivery, bounce, and complaint events
5. Validate unsubscribe and consent requirements

## Required Checks

- Duplicate sends prevented with idempotency keys
- PII minimized in notification payloads
- Bounce and complaint handling configured
- Critical templates tested across environments

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

- Workflow is production-ready with verified evidence
- Operational and security guardrails are in place
- Release and rollback expectations are documented
