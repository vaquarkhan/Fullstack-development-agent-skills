# Microservice Patterns Checklist

Use this checklist when introducing distributed architecture patterns.

## Transaction And Consistency

- [ ] Saga steps and compensations are explicitly modeled
- [ ] Event publishing uses outbox or equivalent anti-dual-write strategy
- [ ] Idempotency keys are enforced for retried operations

## Reliability

- [ ] Timeout, retry, and circuit-breaker budgets are defined
- [ ] Dead-letter and replay paths exist for asynchronous failures
- [ ] Correlation IDs propagate across all service boundaries

## Traffic And Security

- [ ] API gateway policies enforce auth and input validation
- [ ] Service-to-service identity and authorization are documented
- [ ] Rate limiting protects critical dependencies

## Operability

- [ ] Dashboards and alerts cover each critical dependency
- [ ] Rollback and incident runbooks are versioned and owned
- [ ] Canary and progressive rollout strategies are tested
