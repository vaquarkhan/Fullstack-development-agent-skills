---
name: fastapi-async-backend
description: Build async Python APIs with FastAPI, Pydantic v2, SQLAlchemy 2 async, and OpenAPI-first contracts. Use for high-performance Python backend services and ML inference APIs.
disable-model-invocation: true
---

# FastAPI Async Backend

## Use When

- Building async Python REST APIs with FastAPI
- OpenAPI-first contracts with Pydantic validation are required
- ML inference or I/O-heavy Python services need low latency

## Workflow

1. Define Pydantic models for request/response schemas.
2. Implement async route handlers; use async DB sessions (SQLAlchemy 2 + asyncpg).
3. Generate OpenAPI spec; wire dependency injection for auth and DB.
4. Add structured logging, Prometheus metrics, and health endpoints.
5. Test with pytest-asyncio and httpx AsyncClient.

## Required Checks

- No blocking I/O in async def routes without run_in_executor
- Pydantic models versioned; breaking changes documented
- Secrets via environment; Settings class with validation
- DB migrations via Alembic with rollback notes

## Decision Framework

- Prefer async end-to-end when using asyncpg/httpx; use sync workers (gunicorn) for CPU-bound only routes.
- Use APIRouter modules per domain; avoid monolithic main.py.
- Background tasks for fire-and-forget; Celery/ARQ for durable async jobs.
- CORS, auth, and rate limits configured at app factory level.

## Common Rationalizations And Rebuttals

- "Sync ORM in async route is fine." -> Blocks event loop; use async session or sync worker pool.
- "Pydantic will validate in prod." -> Validate at boundary; return 422 with clear errors.
- "OpenAPI auto-gen is enough docs." -> Add examples and error response schemas explicitly.

## Evidence Pack

- OpenAPI diff for changed endpoints
- pytest-asyncio test output including auth and validation failures
- Alembic migration script with rollback note
- Sample structured log and metric for a request

## Exit Criteria

- Async routes pass tests without event-loop blocking
- OpenAPI spec matches implementation
- Auth, validation, and error envelopes are consistent
