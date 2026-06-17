---
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

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

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
