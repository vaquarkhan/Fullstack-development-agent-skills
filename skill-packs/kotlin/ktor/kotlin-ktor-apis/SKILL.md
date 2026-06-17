---
name: kotlin-ktor-apis
description: Build Kotlin backend APIs with Ktor, kotlinx.serialization, coroutines, and Koin/DI. Use for lightweight JVM services without Spring Boot ceremony.
disable-model-invocation: true
---

# Kotlin Ktor APIs

## Use When

- Building Kotlin HTTP APIs with Ktor instead of Spring Boot
- Coroutine-first services with kotlinx.serialization JSON
- Teams want minimal framework surface on the JVM

## Workflow

1. Configure Application.module with plugins: ContentNegotiation, Authentication, StatusPages.
2. Define @Serializable request/response models with validation.
3. Organize routes in extension functions per domain.
4. Inject services via Koin or manual composition root.
5. Use Exposed/Flyway or R2DBC drivers for persistence.
6. Test with testApplication and mocked services.

## Required Checks

- No runBlocking in request pipeline — use suspend handlers
- Serialization ignores unknown keys policy documented
- Auth plugin validates issuer/audience for JWT
- StatusPages map domain exceptions to consistent error JSON

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer Ktor for API-only Kotlin services; Spring when ecosystem integration dominates.
- Use CIO engine for prototyping; Netty for production concurrency.
- HttpClient with timeouts for outbound calls.
- Structured logging via kotlin-logging + logback JSON encoder.

## Common Rationalizations And Rebuttals

- "Ktor is only for prototypes." -> Production patterns exist for auth, testing, and metrics.
- "Blocking JDBC in suspend is fine." -> Blocks dispatcher; use R2DBC or dedicated pool.
- "Map responses are flexible." -> Breaks contract; use typed @Serializable models.

## Evidence Pack

- testApplication route tests including 401/422 cases
- kotlinx.serialization schema diff for API changes
- Coroutine dispatcher audit (no blocking on Default)
- JWT validation test vectors

## Exit Criteria

- Routes are suspend-based with typed models
- Errors and auth behavior match API contract
- Tests cover validation and authorization paths
