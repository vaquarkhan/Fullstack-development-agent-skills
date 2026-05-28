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

## Exit Criteria

- Dependency outages are contained without systemic failure
- Recovery behavior is predictable and test-proven
