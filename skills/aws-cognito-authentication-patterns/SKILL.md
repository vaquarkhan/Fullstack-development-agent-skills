---
name: aws-cognito-authentication-patterns
description: Implement Amazon Cognito user pools and identity flows for secure authentication, token issuance, and federation. Use for AWS-native identity architecture in fullstack applications.
disable-model-invocation: true
---

# AWS Cognito Authentication Patterns

## Use When

- Building AWS-native login and user management
- Supporting social or enterprise federation through Cognito

## Workflow

1. Define user pool, app clients, and hosted UI or custom auth integration.
2. Configure claims, groups, and custom attributes for authorization needs.
3. Implement frontend sign-in, token refresh, and logout behavior.
4. Validate JWTs in backend and gateway layers.
5. Integrate MFA, password policy, and account recovery controls.

## Required Checks

- Token verification is enforced for every protected service boundary
- Group and claim mapping does not over-grant permissions
- MFA and recovery settings align with security posture

## Exit Criteria

- Cognito auth flows are production-ready and secure
- Identity lifecycle events are observable and auditable
