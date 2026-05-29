# Example: SaaS Multi-Tenant BFF

## Architecture

- Tenant-aware BFF aggregates domain services
- Auth service issues scoped tokens with tenant claims
- Domain services enforce server-side authorization

## Skills Used

- bff-architecture-and-api-aggregation
- authentication-and-authorization-fullstack
- oauth2-oidc-and-token-lifecycle

## Validation Focus

- Cross-tenant negative tests
- BFF partial-failure behavior
- Token scope enforcement at each boundary
