---
name: rust-axum-microservices
description: Build Rust HTTP microservices with Axum, Tower middleware, SQLx/SeaORM, structured errors, and Tokio async runtime. Use for high-performance Rust APIs and edge services.
disable-model-invocation: true
---

# Rust Axum Microservices

## Use When

- Building Rust backend APIs with Axum and Tokio
- Teams need memory-safe, high-throughput services with explicit error handling
- Replacing or complementing Go/Node edge services with Rust

## Workflow

1. Structure crates: domain, application, infrastructure, api binary.
2. Define AppState with Arc-wrapped pools and services; inject via State extractor.
3. Map errors to IntoResponse with consistent problem JSON.
4. Add Tower layers: trace, timeout, compression, auth.
5. Use SQLx compile-time queries or SeaORM with migrations.
6. Test handlers with axum::test and integration tests with testcontainers.

## Required Checks

- No unwrap/expect in request handlers
- Timeouts on outbound HTTP and DB pool acquire
- SQL parameterized — sqlx macros or bind parameters only
- Graceful shutdown on SIGTERM via with_graceful_shutdown

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer thiserror/anyhow boundary pattern — domain errors vs internal errors.
- Keep handlers thin; business logic in async service functions.
- Use tracing spans with request IDs propagated from middleware.
- Actix-web only when team already standardized — Axum + Tower is default here.

## Common Rationalizations And Rebuttals

- "unwrap is fine for prototypes." -> Panics become 500 storms under load; use Result.
- "Clone Arc everywhere is free." -> Profile hot paths; prefer references in service layer.
- "Blocking std::fs in async fn." -> Use tokio::fs or spawn_blocking.

## Evidence Pack

- Handler tests with mock services
- Trace sample with request_id through DB call
- Load test summary for target RPS
- Graceful shutdown behavior under in-flight requests

## Exit Criteria

- Handlers return typed errors mapped to HTTP problem responses
- Observability and timeouts configured on all I/O boundaries
- Service passes clippy and fmt in CI
