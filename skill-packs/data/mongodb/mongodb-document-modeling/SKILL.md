---
name: mongodb-document-modeling
description: Design MongoDB document schemas, indexes, aggregation pipelines, and multi-tenant patterns with operational safety. Use for document-store backends in fullstack applications.
disable-model-invocation: true
---

# MongoDB Document Modeling

## Use When

- Modeling domains in MongoDB (Atlas or self-hosted)
- Designing embed vs reference, indexes, and aggregation for app queries
- Pairing with Node, Java, Python, or Go services using MongoDB drivers

## Workflow

1. Map access patterns first — one document shape per dominant query pattern.
2. Choose embed vs reference; cap array growth; use bucketing for high-volume subdocs.
3. Define JSON Schema validation and compound indexes for hot queries.
4. Implement transactions only when cross-document invariants require them.
5. Plan sharding keys early if tenant scale warrants it.
6. Monitor slow queries and index hit rates in Atlas or profiler.

## Required Checks

- Every production query uses supporting index (explain plan reviewed)
- Tenant isolation enforced in query filter — not only application logic
- Unbounded arrays avoided or capped with archival strategy
- Write concern and read concern documented per use case

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Embed when data is read together and bounded; reference when shared or unbounded.
- Prefer aggregation pipeline for analytics; avoid $lookup storms without indexes.
- Change streams for CDC to search/cache — not polling entire collections.
- Use transactions sparingly; design atomic single-document updates when possible.

## Common Rationalizations And Rebuttals

- "Mongo is schema-less." -> Undocumented schema causes production drift; use validation.
- "Indexes slow writes." -> Missing indexes slow reads more; right-size indexes per query.
- "ObjectId everywhere." -> Use UUID strings for client-facing IDs when integrating APIs.

## Evidence Pack

- explain() output for top 5 queries
- Index list with rationale
- Schema validation rules
- Tenant isolation test cases

## Exit Criteria

- Hot queries are indexed and tenant-scoped
- Document shapes match access patterns without unbounded growth
- Operational monitoring for slow ops is configured
