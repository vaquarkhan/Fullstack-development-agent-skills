---
name: nodejs-microservices
description: Apply backend service defaults for Node.js microservices including contract governance, resilience, and observability. Use when services are built with Node.js, TypeScript, HTTP APIs, queues, or event-driven boundaries.
disable-model-invocation: true
---

# Node.js Microservices Preset

## Defaults

- TypeScript for service code
- OpenAPI or equivalent contract source of truth
- Structured logging with request correlation IDs
- Timeouts and retries with bounded backoff
- Metrics and health endpoints in every service

## Recommended Pairings

- `backend-microservices-architecture`
- `api-contract-first-development`
