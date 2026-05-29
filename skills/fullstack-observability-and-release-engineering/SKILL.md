---
name: fullstack-observability-and-release-engineering
description: Operate fullstack systems with practical observability, release safety controls, incident readiness, and rollback discipline. Use when preparing production rollouts or improving service reliability.
disable-model-invocation: true
---

# Fullstack Observability And Release Engineering

## Use When

- Shipping high-risk fullstack changes
- Improving production readiness and incident recovery
- Standardizing release and rollback practices

## Workflow

1. Define service level indicators and objectives for user-critical paths.
2. Instrument frontend and backend for logs, metrics, traces, and business events.
3. Build dashboards and alerts tied to customer impact, not infrastructure noise.
4. Design rollout strategy (feature flags, canary, shadow, phased traffic shift).
5. Define rollback triggers, ownership, and communication protocol.
6. Run post-release verification and document lessons learned.

## Observability Baseline

- Correlation ID propagation from browser to backend service graph
- Error classification by user-facing severity and recoverability
- Latency percentiles per endpoint and key page interactions
- Queue depth and retry metrics for asynchronous pipelines
- Alert routes and escalation paths for on-call responders

## Required Checks

- Feature flags have default fallback and kill switch
- Database changes are backward compatible with previous app version
- Health checks and readiness probes are accurate under dependency failure
- Rollback plan includes data integrity considerations

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

- Teams can detect, triage, and recover from regressions quickly
- Rollouts are measurable, reversible, and low-risk
- Operational ownership is explicit for runtime behavior
