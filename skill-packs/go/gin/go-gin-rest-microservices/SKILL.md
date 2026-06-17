---
name: go-gin-rest-microservices
description: Build Go REST microservices with Gin, clean architecture, context propagation, and production observability. Use for high-performance Go backend APIs and edge services.
disable-model-invocation: true
---

# Go Gin REST Microservices

## Use When

- Building Go HTTP APIs with Gin or similar routers
- Low-latency services, workers, or API gateways in Go
- Standardizing handler → service → repository layering in Go

## Workflow

1. Define handler, service, and repository packages per domain.
2. Use context.Context for cancellation and request-scoped values.
3. Wire middleware: logging, recovery, auth, metrics, tracing.
4. Configure graceful shutdown and health/readiness endpoints.
5. Test handlers with httptest and integration tests with testcontainers-go.

## Required Checks

- context passed to all I/O calls; no context.Background() in request path
- Errors wrapped with fmt.Errorf("%w") for observability
- SQL uses parameterized queries — no string concatenation
- Graceful shutdown drains in-flight requests

## Decision Framework

- Prefer explicit dependency injection (constructors) over global state.
- Use table-driven tests for handlers and pure functions.
- Keep handlers thin — parse, call service, map response.
- OpenTelemetry for traces; structured slog/zap for logs.

## Common Rationalizations And Rebuttals

- "Global DB pool is simpler." -> Complicates testing; inject dependencies.
- "panic/recover is enough error handling." -> Return typed errors; map to HTTP status in one place.
- "We skip context cancellation." -> Leaks resources under client disconnect.

## Evidence Pack

- Middleware chain diagram and auth flow
- Handler tests including error status mapping
- Trace/log sample with correlation ID
- Graceful shutdown test or runbook

## Exit Criteria

- Handlers are thin and testable with mocked services
- Context, errors, and observability follow Go production conventions
- Service shuts down cleanly under SIGTERM
