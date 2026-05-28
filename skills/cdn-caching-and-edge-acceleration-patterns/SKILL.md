---
name: cdn-caching-and-edge-acceleration-patterns
description: Optimize global performance and resilience with CDN cache strategy, origin shielding, signed delivery, and edge failover controls. Use when serving high-volume frontend assets and APIs.
disable-model-invocation: true
---

# CDN Caching And Edge Acceleration Patterns

## Use When

- Global users require low-latency content delivery
- Origin load or spikes affect frontend reliability

## Workflow

1. Classify cacheability by asset and response type.
2. Define TTL, revalidation, and purge strategy.
3. Configure origin shielding and geo failover behavior.
4. Apply signed URLs/cookies and edge access controls where needed.
5. Monitor hit ratio, origin offload, and stale-content incidents.

## Required Checks

- Cache invalidation strategy supports safe releases
- Sensitive content is never cached in public paths
- CDN outage fallback path is documented and tested

## Exit Criteria

- CDN improves performance without stale or unauthorized content risks
- Edge delivery is measurable and operable
