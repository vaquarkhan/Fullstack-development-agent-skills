---
name: incident-triage-and-oncall-runbooks
description: Triage and stabilize production incidents using structured runbooks, impact-first diagnosis, and clear rollback or mitigation decisions. Use when reliability events affect users or critical services.
disable-model-invocation: true
---

# Incident Triage And Oncall Runbooks

## Use When

- Service health degradation is detected
- User-impacting errors or latency spikes are active

## Workflow

1. Classify incident severity and blast radius.
2. Gather evidence from dashboards, logs, traces, and recent releases.
3. Decide mitigation path (rollback, feature flag disable, traffic shift, hotfix).
4. Communicate timeline, owner, and next update checkpoint.
5. Capture post-incident actions and preventive fixes.

## Required Checks

- Incident timeline and decision log are preserved
- Customer-impact metrics drive mitigation choice
- Clear handoff exists between responders and owners

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

- User impact is mitigated or resolved
- Follow-up remediation actions are tracked with owners
