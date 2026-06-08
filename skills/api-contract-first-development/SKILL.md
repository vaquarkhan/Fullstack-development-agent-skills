---
name: api-contract-first-development
description: Define API contracts before implementation to reduce integration errors and preserve backward compatibility. Use when designing or updating REST, GraphQL, or event-driven interfaces between UI and backend services.
disable-model-invocation: true
---

# API Contract-First Development

## Use When

- Designing or changing REST, GraphQL, or event contracts between UI and services
- Backward compatibility or versioning decisions are required

## Workflow

1. Capture consumer needs and edge cases.
2. Draft contract schema and examples.
3. Define versioning and compatibility guarantees.
4. Implement provider and consumer validation.
5. Release with deprecation timeline when needed.

## Required Checks

- Include required and optional fields explicitly
- Define error envelope and status mapping
- Publish examples for happy and failure paths
- Avoid breaking changes without a migration path
- Contract tests run in CI
- Existing consumers remain compatible
- Deprecations are documented and announced

## Decision Framework

- Start with clear scope and ownership boundaries.
- Prefer incremental, testable slices over broad rewrites.
- Define compatibility and rollback expectations before release.
- Require evidence for reliability and operability outcomes.

## Common Rationalizations And Rebuttals

- "We can fill gaps after merge." -> Critical gaps are harder and riskier to fix in production.
- "This change is too small for process." -> Small changes still need clear validation criteria.
- "Docs can wait." -> Missing context increases future delivery and incident cost.

## Evidence Pack

- Scope and acceptance criteria with owner
- Test or validation evidence for changed behavior
- Compatibility and rollback notes
- Operational visibility requirements for production impact

## Exit Criteria

- Workflow decisions are documented and implementation-ready
- Validation evidence exists for quality, reliability, and compatibility
- Operational readiness and rollback expectations are explicit

