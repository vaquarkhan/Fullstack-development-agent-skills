---
name: api-contract-first-development
description: Define API contracts before implementation to reduce integration errors and preserve backward compatibility. Use when designing or updating REST, GraphQL, or event-driven interfaces between UI and backend services.
disable-model-invocation: true
---

# API Contract-First Development

## Workflow

1. Capture consumer needs and edge cases.
2. Draft contract schema and examples.
3. Define versioning and compatibility guarantees.
4. Implement provider and consumer validation.
5. Release with deprecation timeline when needed.

## Contract Rules

- Include required and optional fields explicitly
- Define error envelope and status mapping
- Publish examples for happy and failure paths
- Avoid breaking changes without a migration path

## Verification

- Contract tests run in CI
- Existing consumers remain compatible
- Deprecations are documented and announced
