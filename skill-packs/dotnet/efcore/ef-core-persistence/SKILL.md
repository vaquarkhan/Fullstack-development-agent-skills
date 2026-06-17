---
name: ef-core-persistence
description: Model relational domains with EF Core 8, fluent configurations, migrations, interceptors, and performant queries. Use for .NET persistence layers with zero-downtime migration discipline.
disable-model-invocation: true
---

# EF Core Persistence

## Use When

- Implementing EF Core data access in ASP.NET Core services
- Designing entities, configurations, migrations, and query performance
- Pairing with `aspnetcore-minimal-apis` or `skills/dotnet-aspnet-core-microservices`

## Workflow

1. Define entities and IEntityTypeConfiguration classes per aggregate.
2. Register DbContext with pooled factory; configure connection resiliency.
3. Use migrations with review for locking — prefer expand/contract for large tables.
4. Implement repositories or specifications; project to DTOs in queries.
5. Add interceptors for auditing, soft delete, or multi-tenant filters.
6. Test with Testcontainers SQL Server/Postgres or in-memory only for unit scope.

## Required Checks

- No N+1 — use Select projections or explicit Include with purpose
- AsNoTracking on read-only queries
- Concurrency tokens on contested aggregates
- Migrations tested against production-like row counts when tables are large

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer configurations over data annotations for team consistency.
- Owned types for value objects; avoid primitive obsession on entities.
- Raw SQL only for reporting or bulk ops — document and parameterize.
- Split read models (Dapper/raw SQL) when EF projections are insufficient.

## Common Rationalizations And Rebuttals

- "Lazy loading is convenient." -> Causes N+1 in APIs; use explicit loading or projections.
- "One DbContext for everything." -> Bounded contexts may need separate contexts.
- "Migrate in app startup always." -> Run migrations in CI/CD job with rollback plan.

## Evidence Pack

- Migration script with expand/contract notes
- Query plan or EF logging proof for critical list endpoints
- Concurrency conflict test output
- Interceptor audit sample (created/updated by)

## Exit Criteria

- Queries are tracked appropriately; hot paths avoid N+1
- Migrations are safe for production table sizes
- Multi-tenant or soft-delete rules enforced at persistence layer
