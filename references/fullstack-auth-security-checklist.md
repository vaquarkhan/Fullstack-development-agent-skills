# Fullstack Auth And Security Checklist

Use this checklist when implementing or reviewing authentication and authorization changes.

## Identity And Session

- [ ] Identity model covers users, tenants, roles, and claims
- [ ] Session strategy is documented with threat model assumptions
- [ ] Token expiry and refresh behavior is deterministic
- [ ] Session revocation and logout behavior are validated

## Frontend Security

- [ ] Sensitive tokens are not exposed to unsafe browser storage patterns
- [ ] Route and component guards hide unauthorized actions
- [ ] CSRF protections exist for cookie-based auth
- [ ] Security-related error messages do not leak internals

## Backend Security

- [ ] Authorization checks are server-side source of truth
- [ ] Endpoint guards validate role and permission claims
- [ ] Input validation is enforced at trust boundaries
- [ ] Rate limits exist for brute-force sensitive paths

## Audit And Monitoring

- [ ] Authentication failures are logged with useful context
- [ ] Privileged actions emit audit events
- [ ] Alerting exists for suspicious auth patterns

## Release Safety

- [ ] Backward compatibility exists during auth rollout
- [ ] Feature flags or staged release controls are in place
- [ ] Rollback plan is documented and rehearsed
