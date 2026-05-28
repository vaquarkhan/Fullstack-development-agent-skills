---
name: oauth2-oidc-and-token-lifecycle
description: Implement OAuth 2.0 and OpenID Connect flows with secure token lifecycle handling across frontend and backend. Use for SSO, delegated access, and standards-based identity architecture.
disable-model-invocation: true
---

# OAuth2 OIDC And Token Lifecycle

## Use When

- Building SSO or federated login
- Implementing delegated API access with standards-based tokens

## Workflow

1. Select grant types per client (PKCE for public clients, client credentials for machine clients).
2. Define token claims, scopes, and audience boundaries.
3. Implement secure token validation on backend services.
4. Design refresh, rotation, revocation, and session expiry behavior.
5. Add observability for auth failures and suspicious token usage.

## Required Checks

- Token signature, issuer, audience, and expiry are validated server-side
- Scope and claim checks are enforced per protected endpoint
- Token refresh and revocation paths are deterministic

## Exit Criteria

- Identity flows are standards-compliant and secure
- Token misuse and failure modes are detectable and recoverable
