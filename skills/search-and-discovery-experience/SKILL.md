---
name: search-and-discovery-experience
description: Implement search and discovery UX with indexing pipelines, relevance tuning, and secure filtered queries.
disable-model-invocation: true
---

# Search And Discovery Experience

## Use When

- Users need fast content discovery
- Search relevance impacts conversion

## Workflow

1. Define index schema and update strategy
2. Implement incremental indexing on data changes
3. Add query filters for tenant and permissions
4. Tune ranking and fallback behavior
5. Monitor query latency and zero-result rate

## Required Checks

- Authorization enforced in search queries
- Index lag within acceptable SLO
- Relevance evaluated with representative queries
- Degraded mode exists when search is unavailable

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
