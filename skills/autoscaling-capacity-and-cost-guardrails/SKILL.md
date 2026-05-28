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

## Exit Criteria

- System meets peak demand while keeping predictable cost envelope
- Scaling policy is documented and reproducible across environments
