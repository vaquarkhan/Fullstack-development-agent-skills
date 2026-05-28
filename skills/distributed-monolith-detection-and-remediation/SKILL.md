---
name: distributed-monolith-detection-and-remediation
description: Detect distributed monolith anti-patterns and remediate with decoupling, contract stabilization, and ownership realignment. Use when microservices are tightly coupled and hard to change.
disable-model-invocation: true
---

# Distributed Monolith Detection And Remediation

## Use When

- Multiple services require lockstep releases
- Synchronous call chains frequently fail under load

## Workflow

1. Audit coupling hotspots: synchronous depth, shared schemas, release dependencies.
2. Identify anti-patterns (shared DB, chatty RPC, implicit contracts).
3. Define target decoupling strategy by dependency class.
4. Introduce contract versioning and async boundaries where needed.
5. Track dependency reduction and release independence metrics.

## Required Checks

- Lockstep deployment paths are identified and prioritized
- Shared database write paths have migration plan
- New boundaries reduce runtime blast radius

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

- Architectural coupling trends downward release-over-release
- Teams can ship high-priority services independently
