---
name: ai-llm-integration-in-fullstack-apps
description: Integrate LLM features safely with prompt governance, guardrails, observability, and cost controls in fullstack apps.
disable-model-invocation: true
---

# Ai Llm Integration In Fullstack Apps

## Use When

- Product adds AI-assisted features
- Need safe and measurable AI behavior

## Workflow

1. Define prompt templates and versioning
2. Implement input/output guardrails
3. Add tracing for latency, cost, and quality
4. Handle fallback when model unavailable
5. Review data residency and PII policies

## Required Checks

- Prompt injection risks mitigated
- Cost budgets and rate limits configured
- Human escalation path for high-risk outputs
- Evaluation set tracks quality regressions

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
