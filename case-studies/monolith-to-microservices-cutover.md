# Case Study: Monolith To Microservices Cutover

## Context

A legacy monolith blocks release velocity and must be modernized with low downtime risk.

## Applied Assets

- Starter pack: `starter-packs/microservices-architecture-modernization-starter.yaml`
- Skills: monolith-to-microservices-migration-strategy, distributed-monolith-detection-and-remediation
- Checklist: `references/microservices-architecture-patterns-checklist.md`

## Delivery Sequence

1. Identify coupling hotspots and extraction candidates.
2. Introduce strangler facade and anti-corruption layers.
3. Migrate traffic in phased slices with dual-run validation.
4. Retire monolith paths only after parity evidence.

## Outcome Metrics

- Release independence improved for two priority domains
- Coupling index reduced across synchronous call depth
- Rollback drill passed for each migration slice
