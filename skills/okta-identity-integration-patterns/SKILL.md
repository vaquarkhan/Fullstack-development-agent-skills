---
name: okta-identity-integration-patterns
description: Integrate Okta for enterprise identity workflows including OIDC login, group claims, and policy-based access controls. Use when implementing workforce or B2B identity scenarios.
disable-model-invocation: true
---

# Okta Identity Integration Patterns

## Use When

- Enterprise SSO is required
- Role or group-based access must map from identity provider claims

## Workflow

1. Configure Okta app integrations for frontend and backend clients.
2. Map groups, roles, and claims to application authorization model.
3. Implement OIDC login, callback, and logout flows.
4. Enforce token and session validation in API gateway and services.
5. Add break-glass and operational procedures for identity outages.

## Required Checks

- Group and role mappings are least-privilege by default
- AuthN/AuthZ behavior remains consistent across environments
- Audit logs include identity, action, and policy decision

## Exit Criteria

- Okta integration is secure, observable, and operable
- Enterprise access scenarios work without privilege escalation gaps
