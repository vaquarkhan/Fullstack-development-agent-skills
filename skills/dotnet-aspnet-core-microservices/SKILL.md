---
name: dotnet-aspnet-core-microservices
description: Design and implement .NET ASP.NET Core microservices with explicit contracts, resilience, observability, and safe release patterns. Use when users request .NET backend services, C# APIs, distributed service design, or production hardening.
disable-model-invocation: true
---

# .NET ASP.NET Core Microservices

## Workflow

1. Define service boundary and ownership.
2. Define API contract and versioning approach.
3. Implement resilience and fault-handling strategy.
4. Add metrics, logs, and distributed tracing.
5. Validate with contract tests and failure-mode checks.

## Required Checks

- Explicit dependency lifetimes and clean DI setup
- Idempotency and concurrency safeguards
- Health probes and readiness endpoints
- Rollout plan with rollback criteria
