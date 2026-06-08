---
name: file-storage-and-media-delivery
description: Manage object storage for uploads, media, and documents across S3, Azure Blob, or GCS with secure access patterns.
disable-model-invocation: true
---

# File Storage And Media Delivery

## Use When

- User uploads or downloadable assets
- Media requires CDN acceleration

## Workflow

1. Define storage classes and lifecycle rules
2. Use pre-signed URLs or tokenized access
3. Scan uploads for malware where required
4. Configure CDN caching and purge on update
5. Validate encryption at rest and in transit

## Required Checks

- Unauthorized access paths blocked
- MIME and size limits enforced
- Retention and deletion policies documented
- CDN invalidation tested during release

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
