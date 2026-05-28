---
name: domain-driven-service-decomposition
description: Decompose systems into service boundaries using domain-driven design, bounded contexts, and team ownership constraints. Use when splitting monoliths or correcting poor service boundaries.
disable-model-invocation: true
---

# Domain Driven Service Decomposition

## Use When

- Service boundaries are unclear or causing coupling
- Teams are planning monolith-to-microservice migration

## Workflow

1. Identify domains, subdomains, and bounded contexts.
2. Map business capabilities to ownership-aligned services.
3. Define context boundaries, contracts, and data ownership.
4. Validate boundaries against team cognitive load and release autonomy.
5. Plan incremental extraction slices with anti-corruption layers.

## Required Checks

- Service boundary avoids shared write ownership
- Cross-context communication contracts are explicit
- Team ownership model supports independent deployment

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

- Service map is implementable and evolvable
- Decomposition roadmap includes measurable migration milestones
