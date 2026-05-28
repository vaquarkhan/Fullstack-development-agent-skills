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

## Exit Criteria

- Feature can be disabled without redeploy
- Rollout can be audited from metrics and logs
