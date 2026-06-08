---
name: autoscaling-capacity-and-cost-guardrails
description: Tune autoscaling for services and frontend workloads using demand signals, protection windows, and cost guardrails. Use for production scale growth and volatility.
disable-model-invocation: true
---

# Autoscaling Capacity And Cost Guardrails

## Use When

- Traffic patterns are bursty or unpredictable
- Scaling incidents or cloud cost spikes are recurring

## Workflow

1. Select scaling signals (CPU, queue depth, RPS, latency).
2. Define min, max, and cooldown boundaries per service tier.
3. Add pre-scaling and scale-in protection for critical services.
4. Establish budget alarms and utilization dashboards.
5. Run load tests to validate policy stability.

## Required Checks

- Scaling policy avoids thrash and delayed recovery
- Critical services have reserved baseline capacity
- Cost alerts map to actionable scaling controls

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

- System meets peak demand while keeping predictable cost envelope
- Scaling policy is documented and reproducible across environments
