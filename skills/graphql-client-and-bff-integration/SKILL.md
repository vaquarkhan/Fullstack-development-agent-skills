---
name: graphql-client-and-bff-integration
description: Integrate GraphQL clients and BFF layers with schema governance, caching, and error normalization for scalable UI data access.
disable-model-invocation: true
---

# Graphql Client And Bff Integration

## Use When

- UI needs flexible data fetching across services
- Multiple clients share similar aggregation needs

## Workflow

1. Define schema ownership and deprecation policy
2. Implement BFF resolvers with timeout and batching controls
3. Normalize errors for UI consumption
4. Add persisted queries or complexity limits where needed
5. Monitor resolver latency and failure hotspots

## Required Checks

- Schema changes are backward compatible or versioned
- N+1 query risks are controlled
- Auth enforced in BFF and underlying services
- Client cache invalidation strategy documented

## Decision Framework

- Use BFF to shield UI from microservice churn
- Limit query depth and cost to prevent abuse
- Prefer explicit operations over unbounded graph exploration
- Cache at BFF only when staleness tolerance is clear

## Common Rationalizations And Rebuttals

- "GraphQL removes need for API design." -> Schema governance is still required.
- "Client can call services directly." -> Coupling and security boundaries weaken.
- "No query limits needed internally." -> Expensive queries will appear under load.

## Evidence Pack

- Schema diff and compatibility note
- Load test for hot queries
- Auth negative tests at BFF boundary
- UI error-state screenshots or tests

## Exit Criteria

- GraphQL layer is secure and performant
- UI teams have stable contracts
