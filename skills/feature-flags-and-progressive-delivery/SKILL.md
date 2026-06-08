---
name: feature-flags-and-progressive-delivery
description: Deliver fullstack changes safely using feature flags, phased rollout, and kill-switch controls. Use for high-risk releases and incremental launches.
disable-model-invocation: true
---

# Feature Flags And Progressive Delivery

## Use When

- Launching behavior that affects critical user journeys
- Releasing features across multiple backend and frontend components

## Workflow

1. Define flag type and lifecycle owner.
2. Implement default-safe behavior for disabled state.
3. Add rollout plan (internal, beta cohort, percentage rollout, full rollout).
4. Track success and rollback metrics.
5. Remove stale flags after stable release.

## Required Checks

- Flag defaults preserve previous behavior
- Rollout and rollback criteria are explicit
- Telemetry segments flagged and unflagged users

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

- Feature can be disabled without redeploy
- Rollout can be audited from metrics and logs
