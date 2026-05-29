---
name: frontend-security-csp-and-xss-hardening
description: Harden frontend applications against XSS, clickjacking, and supply-chain risks with CSP, sanitization, and secure rendering practices.
disable-model-invocation: true
---

# Frontend Security Csp And Xss Hardening

## Use When

- Internet-facing UI with rich user content
- Security review flagged XSS or CSP gaps

## Workflow

1. Define CSP policy per environment with nonce or hash strategy
2. Sanitize untrusted HTML and URL inputs
3. Restrict inline scripts and dangerous DOM APIs
4. Audit third-party scripts and dependencies
5. Validate security headers at edge and app layers

## Required Checks

- CSP violations monitored with actionable alerts
- Dangerous HTML rendering paths are eliminated or sanitized
- Clickjacking protections enabled
- Dependency vulnerability scan in CI

## Decision Framework

- Default deny for script sources unless explicitly approved
- Never trust client-side sanitization alone for persisted content
- Use Subresource Integrity for external assets when possible
- Separate admin and user rendering paths

## Common Rationalizations And Rebuttals

- "CSP is too strict for our app." -> Start with report-only mode and tighten iteratively.
- "innerHTML is fine for speed." -> It is a common XSS source; use safe alternatives.
- "Security headers are edge-only." -> App and CDN layers must align.

## Evidence Pack

- CSP report summary and remediation log
- Security test evidence for XSS payloads
- Header validation output in staging and prod
- Third-party script inventory with owners

## Exit Criteria

- Frontend attack surface is materially reduced
- Security regressions are caught before release
