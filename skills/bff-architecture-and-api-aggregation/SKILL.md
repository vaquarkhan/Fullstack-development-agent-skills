---
name: bff-architecture-and-api-aggregation
description: Build Backend-for-Frontend services that aggregate APIs for specific clients while preserving domain boundaries and performance. Use for complex UI composition and multi-client experiences.
disable-model-invocation: true
---

# BFF Architecture And API Aggregation

## Use When

- Frontend depends on multiple backend services per screen
- Different clients (web, mobile, partner) need tailored payloads

## Workflow

1. Define client-specific BFF boundary and ownership.
2. Design response contracts optimized for UI rendering.
3. Implement upstream call orchestration with timeouts and fallbacks.
4. Add partial-failure handling and graceful degradation.
5. Measure end-to-end latency and payload efficiency.

## Required Checks

- BFF does not duplicate core domain business rules
- Upstream failure handling is deterministic
- Aggregated endpoint performance budget is documented

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

- Client complexity decreases without coupling domain services
- BFF reliability is observable and operable
