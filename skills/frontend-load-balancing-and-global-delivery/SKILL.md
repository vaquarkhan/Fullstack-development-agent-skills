---
name: frontend-load-balancing-and-global-delivery
description: Scale frontend delivery with global load balancing, CDN strategy, cache control, and origin failover. Use for high-traffic and multi-region user experiences.
disable-model-invocation: true
---

# Frontend Load Balancing And Global Delivery

## Use When

- User traffic spans regions or large demand spikes
- Frontend latency and availability targets are strict

## Workflow

1. Define global traffic steering and health-check strategy.
2. Configure CDN caching by asset type and content volatility.
3. Set origin shielding and failover for degraded regions.
4. Implement cache-busting and purge controls for safe rollouts.
5. Validate latency and error rates across geographies.

## Required Checks

- Cache headers align with release and invalidation policy
- Regional failover behavior is tested
- Static and dynamic content paths have clear scaling model

## Exit Criteria

- Frontend delivery remains available during regional or origin failures
- Global performance objectives are measurable and stable
