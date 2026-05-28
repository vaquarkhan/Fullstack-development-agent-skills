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

## Exit Criteria

- Architectural coupling trends downward release-over-release
- Teams can ship high-priority services independently
