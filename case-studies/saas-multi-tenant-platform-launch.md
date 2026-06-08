# Case Study: SaaS Multi-Tenant Platform Launch

## Context

A B2B SaaS team must launch tenant-aware modules without cross-tenant data leakage.

## Applied Assets

- Starter pack: `starter-packs/saas-multi-tenant-starter.yaml`
- Skills: authentication-and-authorization-fullstack, bff-architecture-and-api-aggregation
- Checklist: `references/fullstack-auth-security-checklist.md`

## Delivery Sequence

1. `/spec` define tenant model, claims, and API contracts.
2. `/plan` split auth, BFF, and service extraction slices.
3. `/build` implement tenant-scoped authorization and BFF aggregation.
4. `/validate` run negative auth tests and contract compatibility checks.
5. `/review` use security-threat-reviewer persona.
6. `/ship` with feature flags and canary rollout.

## Outcome Metrics

- Zero cross-tenant access in security test suite
- Independent deploy for auth and domain services
- Rollback completed under 15 minutes in drill
