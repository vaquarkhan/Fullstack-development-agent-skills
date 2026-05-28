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

## Exit Criteria

- User impact is mitigated or resolved
- Follow-up remediation actions are tracked with owners
