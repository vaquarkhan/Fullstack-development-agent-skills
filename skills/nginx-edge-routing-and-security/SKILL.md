---
name: nginx-edge-routing-and-security
description: Configure NGINX for reverse proxy routing, TLS termination, security headers, rate controls, and resilient upstream handling. Use for internet-facing edge and gateway traffic management.
disable-model-invocation: true
---

# NGINX Edge Routing And Security

## Use When

- NGINX is used as ingress, reverse proxy, or edge gateway
- Teams need stronger edge security and request control

## Workflow

1. Define route topology, upstream pools, and health checks.
2. Configure TLS, HSTS, and secure header policies.
3. Apply request limits, throttling, and abuse controls.
4. Add caching and compression with explicit invalidation policy.
5. Instrument logs and metrics for edge behavior and anomalies.

## Required Checks

- Upstream failover and timeout behavior is tested
- Security headers and TLS configuration meet policy requirements
- Rate limiting protects backend dependencies without false positives

## Exit Criteria

- NGINX edge behavior is predictable under load and failure
- Security posture is enforceable and observable
