# Frontend Scaling And Edge Security Checklist

Use this checklist for global frontend delivery and edge hardening.

## Delivery And Scale

- [ ] Global load balancing strategy is defined
- [ ] CDN caching and invalidation policy is documented
- [ ] Regional failover behavior is tested

## Security

- [ ] WAF and anti-abuse controls are enabled at edge
- [ ] API gateway auth and schema validation are enforced
- [ ] Sensitive headers and cookies are protected and scoped

## Performance And Operations

- [ ] Core Web Vitals and latency SLOs are tracked by region
- [ ] Autoscaling limits and cost guardrails are in place
- [ ] Rollback plan includes cache purge and route fallback steps

## Provenance

- Sources: OWASP Top 10, CDN and edge security guidance
- Last reviewed: 2026-06
