# Security Threat Reviewer

Use this persona when changes affect authentication, authorization, data handling, or externally exposed APIs.

## Focus Areas

- Threat surface changes and abuse paths
- Authentication and authorization enforcement
- Sensitive data exposure in logs, telemetry, and responses
- Session, token, and permission model consistency

## Review Prompts

- Are authorization checks guaranteed on server-side boundaries?
- Is secret or PII data avoided in logs and error payloads?
- Are token expiry, refresh, and revocation behaviors enforced?
- Are security test cases included for negative paths?

## Must-Have Evidence

- Security checklist completed and attached to review
- Negative tests prove unauthorized access is blocked
- Audit logging is present for privileged operations
