#!/usr/bin/env python3
"""Scaffold additional language/framework skill packs."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PACKS: dict[str, dict[str, str]] = {
    "skill-packs/java/quarkus/quarkus-cloud-native-apis/SKILL.md": """---
name: quarkus-cloud-native-apis
description: Build cloud-native REST and reactive APIs with Quarkus, GraalVM native images, and Kubernetes-ready health probes. Use for Java microservices targeting fast startup and low memory footprint.
disable-model-invocation: true
---

# Quarkus Cloud Native APIs

## Use When

- Building Java APIs with Quarkus instead of Spring Boot
- Native image compilation or Kubernetes-first deployment is required
- Sub-second startup and low memory footprint are goals

## Workflow

1. Define REST resources with JAX-RS or RESTEasy Reactive.
2. Use CDI (@ApplicationScoped) for services; avoid static singletons.
3. Configure datasource, Flyway/Liquibase, and health/liveness probes.
4. Add OpenTelemetry and Micrometer metrics via Quarkus extensions.
5. Build and test JVM mode first, then native profile in CI.

## Required Checks

- /q/health/live and /q/health/ready configured with dependency checks
- Panache or repository layer does not leak entities in REST responses
- Native build profile tested in CI or documented as manual gate
- Config externalized via application.properties and env vars

## Decision Framework

- Prefer RESTEasy Reactive for high-concurrency I/O-bound endpoints.
- Use Panache active record only for simple CRUD; repository pattern for complex domains.
- Enable native image only after JVM-mode test suite is green.
- Use SmallRye Fault Tolerance for timeout, retry, and circuit breaker.

## Common Rationalizations And Rebuttals

- "Quarkus is just Spring Boot lite." -> CDI and extension model differ; follow Quarkus idioms.
- "Native build later." -> Native-incompatible reflection fails late; test native profile early.
- "Panache everywhere." -> Complex queries need repositories or projections.

## Evidence Pack

- Quarkus extension list and rationale
- Health probe output under dependency failure
- JVM vs native startup/memory comparison (if native enabled)
- OpenTelemetry trace sample through REST → service → DB

## Exit Criteria

- API runs in JVM mode with passing tests and health checks
- Cloud deployment manifests include probe paths and resource limits
- Observability and config follow twelve-factor expectations
""",
    "skill-packs/java/micronaut/micronaut-reactive-microservices/SKILL.md": """---
name: micronaut-reactive-microservices
description: Build reactive Micronaut microservices with compile-time DI, non-blocking I/O, and GraalVM-ready APIs. Use for low-latency Java services with Netty and Project Reactor.
disable-model-invocation: true
---

# Micronaut Reactive Microservices

## Use When

- Building reactive Java microservices with Micronaut
- Compile-time dependency injection and fast startup are priorities
- Non-blocking integration with databases, HTTP clients, or messaging

## Workflow

1. Define @Controller endpoints returning Mono/Flux for I/O-bound work.
2. Use @Singleton services with constructor injection (compile-time validated).
3. Configure Netty server, connection pools, and reactive data access.
4. Add Micronaut Security, validation, and OpenAPI where needed.
5. Verify with @MicronautTest and Testcontainers for integration paths.

## Required Checks

- Blocking calls not on event loop thread (use schedulers or blocking executor)
- HTTP client timeouts and retry policies configured explicitly
- Secrets via environment; no credentials in application.yml committed to git
- GraalVM native hints or build args documented if targeting native

## Decision Framework

- Prefer reactive end-to-end for high fan-out I/O; use blocking MVC style only when team lacks reactive expertise.
- Use Micronaut Data for repository abstraction; avoid leaking entities in API responses.
- Use declarative HTTP clients (@Client) with explicit read timeouts.
- Enable distributed tracing via Micronaut Tracing + OpenTelemetry.

## Common Rationalizations And Rebuttals

- "Blocking JDBC is fine on reactive threads." -> Blocks Netty event loop; offload or use reactive drivers.
- "Micronaut works like Spring." -> Annotation processors and config differ; follow Micronaut docs.
- "We can add timeouts later." -> Missing timeouts cause hung requests under load.

## Evidence Pack

- Thread/event-loop safety review for blocking calls
- Client timeout and circuit breaker configuration
- Integration test output with Testcontainers
- Trace showing non-blocking request path

## Exit Criteria

- Reactive endpoints handle load without event-loop blocking
- Services start quickly with compile-time DI validation at build time
- Security, config, and observability baselines are met
""",
    "skill-packs/java/spring-boot/spring-cloud-gateway-routing/SKILL.md": """---
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
""",
    "skill-packs/java/spring-boot/spring-webflux-reactive/SKILL.md": """---
name: spring-webflux-reactive
description: Build reactive Spring WebFlux APIs with non-blocking I/O, backpressure-aware streams, and Project Reactor. Use for high-concurrency Java services without virtual-thread blocking models.
disable-model-invocation: true
---

# Spring WebFlux Reactive

## Use When

- Building non-blocking REST or SSE APIs with Spring WebFlux
- High fan-out I/O with external HTTP, DB, or messaging clients
- Streaming responses (SSE, Flux) to clients

## Workflow

1. Define @RestController methods returning Mono/Flux.
2. Use WebClient for outbound calls with explicit timeouts.
3. Choose reactive drivers (R2DBC, reactive Mongo) or offload blocking work.
4. Handle errors with onErrorMap and consistent ProblemDetail responses.
5. Load-test with concurrent clients to validate backpressure behavior.

## Required Checks

- No blocking JDBC or Thread.sleep on reactor threads
- WebClient configured with connect/read/write timeouts
- Error signals mapped to RFC 9457 or project error envelope
- SSE/stream endpoints document client disconnect handling

## Decision Framework

- Prefer WebFlux when I/O-bound concurrency dominates; use MVC + virtual threads when team prefers imperative style.
- Blockhound or reactor debugging in CI for accidental blocking detection.
- Use bounded elastic scheduler for unavoidable blocking sections.
- Keep reactive chains readable — extract operators into named methods.

## Common Rationalizations And Rebuttals

- "Reactive is always faster." -> Reactive adds complexity; use only when concurrency gains justify it.
- "block() is fine once." -> block() on reactive thread stalls event loop; use publishOn/subscribeOn.
- "Same service layer as MVC." -> Shared blocking services need scheduler isolation in WebFlux.

## Evidence Pack

- Blockhound or thread audit showing no blocking on event loop
- WebClient timeout configuration and failure test output
- Load test summary for target concurrency
- Sample SSE/stream client disconnect behavior

## Exit Criteria

- Reactive endpoints scale under I/O load without event-loop stalls
- Error and timeout behavior matches API contract
- Team can maintain reactor chains with documented patterns
""",
    "skill-packs/python/fastapi/fastapi-async-backend/SKILL.md": """---
name: fastapi-async-backend
description: Build async Python APIs with FastAPI, Pydantic v2, SQLAlchemy 2 async, and OpenAPI-first contracts. Use for high-performance Python backend services and ML inference APIs.
disable-model-invocation: true
---

# FastAPI Async Backend

## Use When

- Building async Python REST APIs with FastAPI
- OpenAPI-first contracts with Pydantic validation are required
- ML inference or I/O-heavy Python services need low latency

## Workflow

1. Define Pydantic models for request/response schemas.
2. Implement async route handlers; use async DB sessions (SQLAlchemy 2 + asyncpg).
3. Generate OpenAPI spec; wire dependency injection for auth and DB.
4. Add structured logging, Prometheus metrics, and health endpoints.
5. Test with pytest-asyncio and httpx AsyncClient.

## Required Checks

- No blocking I/O in async def routes without run_in_executor
- Pydantic models versioned; breaking changes documented
- Secrets via environment; Settings class with validation
- DB migrations via Alembic with rollback notes

## Decision Framework

- Prefer async end-to-end when using asyncpg/httpx; use sync workers (gunicorn) for CPU-bound only routes.
- Use APIRouter modules per domain; avoid monolithic main.py.
- Background tasks for fire-and-forget; Celery/ARQ for durable async jobs.
- CORS, auth, and rate limits configured at app factory level.

## Common Rationalizations And Rebuttals

- "Sync ORM in async route is fine." -> Blocks event loop; use async session or sync worker pool.
- "Pydantic will validate in prod." -> Validate at boundary; return 422 with clear errors.
- "OpenAPI auto-gen is enough docs." -> Add examples and error response schemas explicitly.

## Evidence Pack

- OpenAPI diff for changed endpoints
- pytest-asyncio test output including auth and validation failures
- Alembic migration script with rollback note
- Sample structured log and metric for a request

## Exit Criteria

- Async routes pass tests without event-loop blocking
- OpenAPI spec matches implementation
- Auth, validation, and error envelopes are consistent
""",
    "skill-packs/python/django/django-enterprise-backend/SKILL.md": """---
name: django-enterprise-backend
description: Build enterprise Django REST APIs with DRF, async views, Celery tasks, and multi-tenant patterns. Use for admin-heavy Python backends and content platforms.
disable-model-invocation: true
---

# Django Enterprise Backend

## Use When

- Building Django + Django REST Framework APIs
- Admin interfaces, ORM-heavy domains, or Celery background jobs are needed
- Multi-app Django project structure with clear app boundaries

## Workflow

1. Split domain into Django apps with models, serializers, and viewsets.
2. Use DRF for API layer; keep business logic in services or model methods.
3. Configure Celery for async tasks; Redis/RabbitMQ as broker.
4. Add migrations, permissions, and queryset scoping for multi-tenant data.
5. Test with pytest-django and factory_boy fixtures.

## Required Checks

- select_related/prefetch_related used on list endpoints (N+1 prevention)
- Permissions and queryset filtering enforce tenant/user boundaries
- Migrations reviewed for locking impact on large tables
- Celery tasks idempotent with retry and dead-letter handling

## Decision Framework

- Prefer class-based views/viewsets over function views for consistency.
- Use custom User model from project start if auth customization expected.
- Keep fat models vs fat services decision explicit per app.
- Use database constraints for invariants, not only serializer validation.

## Common Rationalizations And Rebuttals

- "Admin can handle ops tasks." -> Admin is not a substitute for API authz and audit trails.
- "Serializer validation is enough." -> DB constraints catch race conditions serializers miss.
- "Celery retries forever." -> Set max retries and dead-letter queues.

## Evidence Pack

- DRF permission test matrix results
- Query count assertions for list endpoints
- Migration plan for large tables
- Celery task idempotency test evidence

## Exit Criteria

- API permissions and tenant scoping verified by tests
- N+1 queries eliminated on critical list views
- Background jobs recover safely from retries
""",
    "skill-packs/go/gin/go-gin-rest-microservices/SKILL.md": """---
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
""",
    "skill-packs/php/laravel/laravel-api-platform/SKILL.md": """---
name: laravel-api-platform
description: Build Laravel REST and JSON:API backends with Sanctum/Passport auth, queues, and Eloquent best practices. Use for PHP fullstack and API-first Laravel applications.
disable-model-invocation: true
---

# Laravel API Platform

## Use When

- Building Laravel API backends with Eloquent ORM
- Sanctum token auth, Horizon queues, or Nova admin are in stack
- PHP fullstack teams need API conventions and testing patterns

## Workflow

1. Define routes in api.php with FormRequest validation.
2. Use API Resources for response transformation — hide internal model shape.
3. Configure Sanctum/Passport, policies, and middleware for authz.
4. Offload long work to queued jobs with Horizon monitoring.
5. Test with Pest/PHPUnit feature tests and factory states.

## Required Checks

- N+1 prevented with eager loading on index endpoints
- Policies gate model actions; not only route middleware
- Mass assignment guarded via $fillable or DTOs
- Queue jobs idempotent with failed-job handling

## Decision Framework

- Prefer FormRequest for validation; keep controllers thin.
- Use API Resources and conditional fields for response stability.
- Version breaking API changes (/api/v1 → v2) with deprecation headers.
- Cache config/routes in production; document opcache requirements.

## Common Rationalizations And Rebuttals

- "Returning models directly is faster." -> Leaks schema; use API Resources.
- "Jobs can retry without idempotency." -> Duplicate side effects under at-least-once delivery.
- "Policies later." -> Auth bugs are expensive; define policies with endpoints.

## Evidence Pack

- Feature test output for authz matrix
- Query count or debugbar proof for N+1 fixes
- API Resource diff for response changes
- Horizon failed-job recovery procedure

## Exit Criteria

- API responses stable via Resources; authz enforced by policies
- Queues and failed jobs monitored
- Validation and error format consistent across endpoints
""",
    "skill-packs/ruby/rails/rails-api-backend/SKILL.md": """---
name: rails-api-backend
description: Build Ruby on Rails API-only applications with ActiveRecord, Pundit authorization, Sidekiq jobs, and JSON:API patterns. Use for convention-driven Ruby backend services.
disable-model-invocation: true
---

# Rails API Backend

## Use When

- Building API-only Rails 7+ applications
- ActiveRecord, Sidekiq, and convention-over-configuration fit the team
- Rapid delivery with strong testing culture (RSpec/Minitest)

## Workflow

1. Use rails new --api; organize controllers, models, serializers/blueprints.
2. Add Pundit policies and strong params or dedicated param objects.
3. Configure Sidekiq for background jobs; Redis for cache and Action Cable if needed.
4. Use strong migrations and zero-downtime patterns for schema changes.
5. Test with request specs and policy specs.

## Required Checks

- Includes/preloads on index actions to prevent N+1
- Policies tested for each controller action
- Migrations safe for large tables (disable_ddl_transaction, concurrent indexes)
- Sidekiq jobs idempotent with unique-job locks where needed

## Decision Framework

- Prefer service objects for multi-model orchestration over fat controllers.
- Use blueprinter/alba/serializers — do not render models directly.
- API versioning via routes or Accept header — document chosen strategy.
- Flipper or similar for feature flags on risky releases.

## Common Rationalizations And Rebuttals

- "Rails magic handles it." -> Explicit N+1 and authz tests still required.
- "Callbacks for business logic." -> Callbacks hide flow; prefer services.
- "Big bang migrations." -> Use strong_migrations for zero-downtime deploys.

## Evidence Pack

- Request spec coverage for auth and validation
- Bullet gem or query log proving N+1 fixes
- Migration safety checklist for production tables
- Sidekiq retry/idempotency test notes

## Exit Criteria

- API responses consistent via serializers/blueprints
- Authorization verified per action
- Background jobs and migrations are production-safe
""",
}


def main() -> None:
    for rel_path, content in PACKS.items():
        path = ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"created {rel_path}")
    print(f"OK: created {len(PACKS)} additional skill packs")


if __name__ == "__main__":
    main()
