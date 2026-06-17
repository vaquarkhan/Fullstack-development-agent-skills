---
name: nestjs-enterprise-backend
description: Build enterprise NestJS APIs with modular architecture, class-validator DTOs, TypeORM/Prisma persistence, guards, interceptors, and OpenAPI. Use for deep TypeScript backend microservice implementation beyond cross-stack patterns.
disable-model-invocation: true
---

# NestJS Enterprise Backend

## Use When

- Implementing production NestJS APIs with modular domain boundaries
- Wiring auth guards, validation pipes, interceptors, and OpenAPI in NestJS
- Teams need NestJS-specific patterns beyond `skills/nodejs-nestjs-backend-microservices`

## Workflow

1. Organize feature modules (controller, service, repository/DTO) per domain.
2. Define DTOs with class-validator; enable global ValidationPipe with whitelist.
3. Add guards for JWT/API keys; policies via custom decorators or CASL.
4. Configure TypeORM/Prisma with migrations and transaction boundaries in services.
5. Document OpenAPI via @ApiTags and generate client SDKs for frontend consumers.
6. Test with @nestjs/testing unit tests and supertest e2e with test DB.

## Required Checks

- ValidationPipe forbids unknown properties (whitelist + forbidNonWhitelisted)
- Services own transactions; controllers stay thin
- ConfigModule loads secrets from env — no secrets in source
- E2E tests cover auth failure and validation error envelopes

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer feature modules over god AppModule imports.
- Use CQRS (@nestjs/cqrs) only when read/write models genuinely diverge.
- Cache with explicit TTL and invalidation keys — not ad-hoc Map in service.
- Bull/BullMQ for durable jobs; @Cron only for lightweight schedulers.

## Common Rationalizations And Rebuttals

- "DTOs are optional with TypeScript." -> Runtime validation catches bad clients; use DTOs at boundary.
- "Prisma in controller is faster." -> Leaks persistence; breaks testing and module boundaries.
- "Global exception filter later." -> Inconsistent error shapes break API consumers early.

## Evidence Pack

- OpenAPI diff for changed endpoints
- E2E test output for auth and validation matrix
- Module dependency graph (no circular imports)
- Migration script with rollback note

## Exit Criteria

- Modules are bounded; controllers delegate to services
- Validation, auth, and error envelopes are consistent
- Tests cover happy path and boundary failures
