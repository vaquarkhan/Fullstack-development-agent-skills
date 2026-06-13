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

- Default flags to off/safe path; disabled state must match pre-change production behavior.
- Use cohort, percentage, and kill-switch flags with explicit rollout and rollback thresholds.
- Instrument flagged vs unflagged cohorts on error rate, latency, and business KPIs.
- Schedule flag retirement after stable full rollout to avoid debt and stale branches.

## Common Rationalizations And Rebuttals

- "Flags are only for experiments." -> Flags are production safety valves for risky fullstack releases.
- "We will remove the flag later." -> Unremoved flags multiply code paths and test matrices; set retirement date at creation.
- "100% rollout means delete checks." -> Keep kill switch until post-release verification window closes.

## Evidence Pack

- Flag lifecycle doc: owner, default, cohort rules, retirement date
- Rollout dashboard comparing flagged vs baseline metrics
- Kill-switch test proving disable without redeploy
- Removal PR or ticket scheduled after stability window

## Exit Criteria

- Feature can be disabled without redeploy
- Rollout can be audited from metrics and logs
