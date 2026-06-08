---
name: multi-cloud-disaster-recovery
description: Design disaster recovery across regions and clouds with RTO/RPO targets, failover drills, and data consistency controls.
disable-model-invocation: true
---

# Multi Cloud Disaster Recovery

## Use When

- Business continuity requirements are strict
- Regional outages must be survivable

## Workflow

1. Define RTO and RPO per critical journey
2. Document dependency inventory and failover order
3. Implement backup and restore automation
4. Run failover drills with measured outcomes
5. Maintain runbooks and communication templates

## Required Checks

- Failover drill meets RTO/RPO targets
- Data consistency validated after recovery
- DNS and traffic shift procedures tested
- Rollback from failed failover documented

## Decision Framework

- Prefer explicit contracts and compatibility rules before implementation.
- If dependency risk is high, require timeout, retry, and fallback strategy per call path.
- If async messaging is used, require idempotency, replay, and dead-letter handling.
- If traffic patterns are volatile, require load, failover, and scaling validation before ship.

## Common Rationalizations And Rebuttals

- "Retries will handle failures automatically." -> Unbounded retries can amplify outages; use budgets.
- "We can skip runbooks for now." -> Operational ambiguity delays incident recovery.
- "Contract changes are minor." -> Small breaking changes cause broad downstream regressions.

## Evidence Pack

- Contract compatibility note and migration strategy (if applicable)
- Failure-mode test evidence for dependency degradation and recovery
- Observability snapshot (latency, error, saturation, or queue health)
- Rollout and rollback steps with clear trigger thresholds

## Exit Criteria

- Workflow is production-ready with verified evidence
- Operational and security guardrails are in place
- Release and rollback expectations are documented
