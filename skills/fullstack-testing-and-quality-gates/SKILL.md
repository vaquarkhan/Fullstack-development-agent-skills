---
name: fullstack-testing-and-quality-gates
description: Define and enforce layered test strategy and quality gates for fullstack systems, including UI behavior, API contracts, integration paths, and release readiness criteria.
disable-model-invocation: true
---

# Fullstack Testing And Quality Gates

## Use When

- New fullstack features are being delivered
- Teams need predictable pre-merge and pre-release gates
- Regressions occur between frontend and backend integration points

## Workflow

1. Map risk by feature area, user path, and service dependency.
2. Define layered tests: unit, component, contract, integration, and end-to-end.
3. Prioritize deterministic tests for core flows and flaky-test elimination.
4. Build CI gates for linting, type checks, tests, coverage thresholds, and security checks.
5. Add release smoke tests for production-like environments.
6. Capture evidence and failure triage guidance in pull request templates.

## Test Coverage Model

- Unit tests for domain rules and utility logic
- Component tests for UI state transitions and accessibility behavior
- Contract tests for request and response compatibility
- Integration tests for API, database, and queue boundaries
- End-to-end tests for critical business journeys only

## Required Checks

- Contract changes include backward compatibility or migration note
- Coverage thresholds exist for changed modules
- Flaky tests are quarantined with an owner and remediation date
- CI failures include actionable logs and reproduction steps

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

- Critical fullstack flows are covered with maintainable tests
- CI and release gates block unsafe changes
- Teams have clear evidence for merge and release decisions
