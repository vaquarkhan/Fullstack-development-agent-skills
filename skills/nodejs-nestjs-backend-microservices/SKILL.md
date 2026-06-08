---
name: nodejs-nestjs-backend-microservices
description: Build Node.js and NestJS backend microservices with contract-first APIs, resilient runtime behavior, secure defaults, and operational readiness. Use for service creation, endpoint additions, and backend modernization.
disable-model-invocation: true
---

# Node.js NestJS Backend Microservices

## Use When

- Building or extending Node.js and NestJS services
- Adding new API endpoints, async consumers, or domain workflows
- Improving service reliability, observability, or deployment safety

## Workflow

1. Define bounded context and service ownership, including dependencies.
2. Define API or event contracts before implementation.
3. Implement business logic in domain-focused modules, not controllers.
4. Add validation, authn and authz hooks, idempotency, and error mapping.
5. Add telemetry (structured logs, metrics, traces) with correlation IDs.
6. Verify with unit, integration, contract, and failure-mode tests.

## Decision Framework

- If endpoint is customer-critical, require explicit SLO, retry budget, and circuit policy.
- If processing is asynchronous, require dead-letter and replay strategy before release.
- If schema changes are non-trivial, require expand-migrate-contract or dual-read/write plan.
- If service has more than one external dependency, require fallback behavior per dependency class.

## Runtime Guardrails

- Timeouts and retries are explicit and bounded
- External calls have circuit breaker or fallback behavior
- Async processing has dead-letter and replay strategy
- Configuration and secrets are injected via environment boundaries
- Health checks reflect dependency health, not process-only liveness

## Required Checks

- API compatibility and deprecation policy are documented
- Schema migrations are reversible or dual-read/write safe
- P95 latency and error budgets are known for critical endpoints
- Incident triage notes include dashboard, logs, and rollback commands

## Common Rationalizations And Rebuttals

- "We can add idempotency later." -> Retries will happen in production; enforce idempotency now.
- "Health check passing means ready." -> Liveness is not readiness; include dependency-aware probes.
- "Retry everything by default." -> Unbounded retries amplify outages; define retry budget.

## Evidence Pack

- API contract artifact and compatibility note
- Failure-mode test output for timeout and dependency outage scenarios
- Runbook snippet with rollback command sequence
- Observability snapshot showing latency/error baseline

## Exit Criteria

- New backend behavior is testable and contract-backed
- Failure handling is deterministic under partial outage
- Service has enough operational metadata for on-call support
