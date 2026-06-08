---
name: resilience-timeouts-retries-and-circuit-breakers
description: Harden service calls with timeout budgets, retry discipline, circuit-breaker states, and graceful degradation. Use when dependency failures can cascade through the system.
disable-model-invocation: true
---

# Resilience Timeouts Retries And Circuit Breakers

## Use When

- Critical requests depend on external or internal services
- Cascading failures and latency storms are observed

## Workflow

1. Define per-call timeout budgets tied to end-to-end SLO.
2. Apply bounded retries with jitter and retry budget caps.
3. Implement circuit-breaker thresholds and half-open probes.
4. Provide fallback responses or queued deferral paths.
5. Monitor open-circuit events and dependency saturation.

## Required Checks

- Retry policy does not exceed dependency capacity
- Circuit transitions are observable and alertable
- Fallback paths preserve user experience expectations

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

- Dependency outages are contained without systemic failure
- Recovery behavior is predictable and test-proven
