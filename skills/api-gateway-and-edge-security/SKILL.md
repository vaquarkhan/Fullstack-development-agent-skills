---
name: api-gateway-and-edge-security
description: Design API gateway policies for auth, rate limits, WAF controls, request validation, and zero-trust edge posture. Use for internet-facing APIs and multi-client access management.
disable-model-invocation: true
---

# API Gateway And Edge Security

## Use When

- Exposing APIs to public clients or partners
- Centralized edge policy is required for governance

## Workflow

1. Define route-level authn and authz requirements.
2. Configure request validation and schema enforcement at edge.
3. Apply IP, token, and tenant-aware rate limiting.
4. Add WAF, bot mitigation, and abuse detection rules.
5. Emit security audit logs and anomaly alerts.

## Required Checks

- Unauthorized traffic is blocked before backend invocation
- Sensitive headers and payload fields are sanitized
- Rate limits protect downstream services under burst traffic

## Exit Criteria

- Edge security posture is enforceable and monitored
- API consumers receive consistent error and quota semantics
