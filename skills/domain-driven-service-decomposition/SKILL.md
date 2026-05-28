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

## Exit Criteria

- Service map is implementable and evolvable
- Decomposition roadmap includes measurable migration milestones
