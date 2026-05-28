---
name: microservice-patterns-service-mesh-and-traffic-management
description: Manage service-to-service traffic with mesh policies for retries, timeouts, mTLS, canary, and fault isolation. Use when platform-level network controls are needed across many services.
disable-model-invocation: true
---

# Microservice Patterns Service Mesh And Traffic Management

## Use When

- Fleet-wide traffic policies need consistency
- Teams require canary and security controls without app rewrites

## Workflow

1. Define baseline traffic policy: timeout, retry budget, circuit behavior.
2. Enforce mTLS identity and authorization between services.
3. Configure canary, blue-green, or weighted routing rules.
4. Apply outlier detection and connection pool limits.
5. Monitor policy impact on latency and error budgets.

## Required Checks

- Retry policy does not amplify downstream outages
- Service identity and policy scopes are explicit
- Canary rollback can be triggered quickly

## Exit Criteria

- Traffic behavior is controllable and observable at platform layer
- Security and release routing are repeatable across services
