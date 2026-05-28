---
name: backend-microservices-architecture
description: Design and implement backend microservices with explicit boundaries, resilience, observability, and safe deployment patterns. Use when the user asks for service design, microservice APIs, reliability, scaling, or incident-hardening.
disable-model-invocation: true
---

# Backend Microservices Architecture

## Use When

- Creating a new microservice
- Refactoring monolith logic into services
- Adding reliability and operability controls

## Workflow

1. Define service boundary, ownership, and data responsibilities.
2. Define API contracts and compatibility policy.
3. Implement idempotency and failure handling.
4. Add telemetry: logs, metrics, traces.
5. Prove readiness with load/error tests and rollback plan.

## Required Checks

- API and event contracts are versioned
- Timeouts, retries, and circuit breakers are explicit
- Dead-letter handling exists for async failures
- Health checks and SLOs are documented
- Rollout strategy includes canary or phased release
