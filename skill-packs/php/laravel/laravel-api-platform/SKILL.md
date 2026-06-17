---
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

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

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
