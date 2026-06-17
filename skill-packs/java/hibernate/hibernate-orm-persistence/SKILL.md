---
name: hibernate-orm-persistence
description: Model and query relational data with Hibernate ORM — entities, associations, fetch plans, caching, and HQL/Criteria. Use for Java persistence beyond basic Spring Data JPA defaults or in Jakarta EE applications.
disable-model-invocation: true
---

# Hibernate ORM Persistence

## Use When

- Complex entity graphs, inheritance, or custom SQL require full Hibernate control
- N+1 queries, fetch joins, or second-level cache tuning are needed
- Working with Hibernate directly (Jakarta EE) or via Spring Data JPA with native Hibernate features

## Workflow

1. Model entities with clear aggregate roots; prefer `FetchType.LAZY` associations.
2. Define equals/hashCode on business keys — not database IDs for transient entities.
3. Use `@NamedQuery`, JPQL, or Criteria API; native SQL only when justified.
4. Tune fetch plans: `@EntityGraph`, join fetch, or DTO projections for read paths.
5. Enable query logging in dev; verify query count in tests for list endpoints.

## Required Checks

- No `EAGER` collections on high-cardinality associations without explicit justification
- `@Version` optimistic locking on concurrent update entities
- Batch size (`@BatchSize` or `hibernate.default_batch_fetch_size`) for collection fetching
- Second-level cache only with explicit invalidation strategy

## Decision Framework

- Prefer Spring Data repositories for simple CRUD; drop to Hibernate API for complex queries.
- Use `@SqlResultSetMapping` or Blaze Persistence for heavy reporting queries.
- Prefer `merge` vs `persist` semantics consciously in service layer.
- Schema changes via Flyway/Liquibase — Hibernate `ddl-auto=validate` in production.

## Common Rationalizations And Rebuttals

- "EAGER loading prevents LazyInitializationException." -> Fix session boundaries and fetch plans; EAGER causes cartesian product queries.
- "Hibernate generates schema in prod." -> Use migrations; ddl-auto validate only.
- "Lombok @Data on entities is fine." -> Breaks entity equality and can trigger unnecessary updates.

## Evidence Pack

- Entity relationship diagram with fetch types annotated
- Query count assertion for critical list/read endpoints
- Migration scripts aligned with entity model
- N+1 fix evidence (before/after query logs)

## Exit Criteria

- Entity model matches domain boundaries without session leaks
- List and detail queries meet performance budgets
- Production uses validated schema, not auto-ddl
