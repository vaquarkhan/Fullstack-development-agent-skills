---
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

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

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
