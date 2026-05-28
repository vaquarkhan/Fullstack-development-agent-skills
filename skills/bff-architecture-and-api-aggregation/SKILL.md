---
name: bff-architecture-and-api-aggregation
description: Build Backend-for-Frontend services that aggregate APIs for specific clients while preserving domain boundaries and performance. Use for complex UI composition and multi-client experiences.
disable-model-invocation: true
---

# BFF Architecture And API Aggregation

## Use When

- Frontend depends on multiple backend services per screen
- Different clients (web, mobile, partner) need tailored payloads

## Workflow

1. Define client-specific BFF boundary and ownership.
2. Design response contracts optimized for UI rendering.
3. Implement upstream call orchestration with timeouts and fallbacks.
4. Add partial-failure handling and graceful degradation.
5. Measure end-to-end latency and payload efficiency.

## Required Checks

- BFF does not duplicate core domain business rules
- Upstream failure handling is deterministic
- Aggregated endpoint performance budget is documented

## Exit Criteria

- Client complexity decreases without coupling domain services
- BFF reliability is observable and operable
