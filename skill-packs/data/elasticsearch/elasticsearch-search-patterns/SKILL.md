---
name: elasticsearch-search-patterns
description: Implement Elasticsearch/OpenSearch indexing, mappings, analyzers, and secure search APIs with sync from primary databases. Use for full-text search, faceted browse, and observability log search in fullstack apps.
disable-model-invocation: true
---

# Elasticsearch Search Patterns

## Use When

- Adding full-text or faceted search to a fullstack product
- Syncing Postgres/Mongo data to Elasticsearch via CDC or outbox
- Building admin search UIs with filters, sorting, and pagination

## Workflow

1. Define index mappings explicitly — avoid dynamic mapping in production.
2. Choose analyzers per field (keyword vs text, subfields for sort/raw).
3. Implement bulk indexing with backoff; version indexes for reindex (alias swap).
4. Query with bool filters for tenant isolation; never trust client-side filters alone.
5. Expose search API with max result window and query complexity limits.
6. Monitor cluster health, shard sizing, and slow query logs.

## Required Checks

- tenantId (or equivalent) in every search filter
- Painless scripts reviewed — no unbounded script complexity
- Reindex playbook documented (alias cutover, rollback)
- User input sanitized — no leading wildcard queries on analyzed text

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Elasticsearch for search/browse; primary DB remains source of truth.
- Use ingest pipelines for denormalization; keep sync idempotent.
- OpenSearch compatible patterns when on AWS — document divergence if any.
- Consider managed (Elastic Cloud, OpenSearch Serverless) vs self-hosted ops cost.

## Common Rationalizations And Rebuttals

- "Dynamic mapping is fine early." -> Mapping explosions break sorting and aggregations later.
- "Search DB can skip auth." -> Tenant leaks via search are critical; filter in query.
- "Reindex live cluster in place." -> Use new index + alias swap for zero-downtime reindex.

## Evidence Pack

- Mapping JSON and analyzer rationale
- Bulk reindex runbook with alias swap steps
- Search API load test at target QPS
- Sample slow query log remediation

## Exit Criteria

- Indexes are versioned; reindex path is tested
- Search API enforces tenant scope and pagination limits
- Sync from primary store is idempotent and monitored
