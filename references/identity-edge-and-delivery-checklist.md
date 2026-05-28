# Identity Edge And Delivery Checklist

Use this checklist for OAuth/OIDC identity, edge security, load balancing, and CDN delivery design.

## Identity

- [ ] OAuth2/OIDC flow is selected per client type
- [ ] Token validation (issuer, audience, signature, expiry) is server-enforced
- [ ] Scope and claim-to-permission mapping follows least privilege
- [ ] Revocation, rotation, and logout semantics are documented

## Provider Integration

- [ ] Okta or Cognito integration is environment-consistent
- [ ] Group and role claims map cleanly to app authorization
- [ ] MFA and recovery controls are enabled per policy

## Edge And Gateway

- [ ] NGINX or gateway routes enforce auth and schema checks
- [ ] TLS and security headers are configured and tested
- [ ] Rate limits and abuse controls protect downstream systems

## Load Balancing And CDN

- [ ] Health checks represent actual readiness
- [ ] Weighted rollout/failover strategy is validated
- [ ] CDN cache policy and purge flow support safe releases
- [ ] Sensitive responses are excluded from shared caching
