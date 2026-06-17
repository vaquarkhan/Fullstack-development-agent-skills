---
name: spring-cloud-gateway-routing
description: Configure Spring Cloud Gateway for API routing, rate limiting, JWT validation, and canary traffic splitting. Use at the edge of Spring microservice meshes.
disable-model-invocation: true
---

# Spring Cloud Gateway Routing

## Use When

- Centralizing API routing, auth, and cross-cutting edge policies
- Implementing rate limits, circuit breakers, or canary routes at the gateway
- Replacing or complementing NGINX/Kong with Spring-native gateway

## Workflow

1. Define routes with predicates (Path, Header, Weight) and filters.
2. Configure JWT/OAuth2 resource server or custom auth filters at gateway.
3. Add Redis-backed rate limiting and request/response logging.
4. Set up weighted routing for canary or blue-green traffic shifts.
5. Validate with contract tests and failure injection on upstream services.

## Required Checks

- Timeouts and retry policies defined per route — no unbounded upstream waits
- Sensitive headers stripped before forwarding (Authorization whitelist documented)
- Rate limit keys scoped appropriately (IP vs API key vs user)
- Fallback responses defined when upstream circuit opens

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Keep business logic out of gateway filters — auth, routing, and policy only.
- Prefer Spring Cloud Gateway filters over custom global filters when built-ins exist.
- Use Weight predicate for canary; use metadata tags for observability correlation.
- Terminate TLS at gateway or load balancer — document chosen trust boundary.

## Common Rationalizations And Rebuttals

- "Gateway can host business rules." -> Gateway becomes a distributed monolith; keep it thin.
- "Default timeouts are enough." -> Upstream slowness exhausts gateway threads; set per-route timeouts.
- "One global rate limit." -> Different APIs need different quotas; scope limits per route/client.

## Evidence Pack

- Route table with predicates, filters, and upstream URIs
- Rate limit and auth filter test results
- Canary weight configuration and rollback procedure
- Trace showing gateway → service correlation IDs

## Exit Criteria

- Routes, auth, and limits behave as documented under normal and degraded upstream
- No business logic embedded in gateway layer
- Rollback path for canary weight changes is tested
