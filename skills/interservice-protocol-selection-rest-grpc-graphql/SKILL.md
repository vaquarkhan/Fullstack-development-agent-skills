---
name: interservice-protocol-selection-rest-grpc-graphql
description: Select and govern REST, gRPC, and GraphQL communication patterns by latency, coupling, and consumer needs. Use when defining or refactoring service communication strategy.
disable-model-invocation: true
---

# Interservice Protocol Selection REST gRPC GraphQL

## Use When

- Service APIs need protocol standardization
- Existing protocol mix causes complexity or performance problems

## Workflow

1. Classify interactions by sync/async, payload size, and fan-out.
2. Choose protocol per use case with explicit rationale.
3. Define schema contracts, error models, and compatibility rules.
4. Implement observability and resiliency controls per protocol.
5. Validate developer ergonomics and operational overhead.

## Required Checks

- Protocol choice aligns with latency and operability targets
- Schema governance includes backward compatibility policy
- Gateway translation overhead is understood and bounded

## Exit Criteria

- Protocol usage is intentional, documented, and maintainable
- Service communication failures are easier to debug and control
