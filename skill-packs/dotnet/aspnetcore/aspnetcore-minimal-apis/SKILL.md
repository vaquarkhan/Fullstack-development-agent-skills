---
name: aspnetcore-minimal-apis
description: Build ASP.NET Core minimal APIs with endpoint filters, JWT auth, OpenAPI, and clean handler delegation. Use for lightweight .NET microservices and BFF endpoints without MVC ceremony.
disable-model-invocation: true
---

# ASP.NET Core Minimal APIs

## Use When

- Building .NET 8+ minimal API services or BFF layers
- Teams want thin Program.cs with endpoint groups and filters
- Cross-stack skill `dotnet-aspnet-core-microservices` needs .NET-specific implementation depth

## Workflow

1. Register services in DI (DbContext, handlers, auth).
2. Group endpoints with MapGroup and route prefixes (/api/v1).
3. Use typed request records and IResult/Results for responses.
4. Add endpoint filters for validation, logging, and problem details.
5. Configure JWT bearer or Entra ID; apply RequireAuthorization per route.
6. Test with WebApplicationFactory and integration tests.

## Required Checks

- CancellationToken forwarded to all async I/O
- ProblemDetails for errors — consistent with RFC 9457
- OpenAPI documents auth schemes and error responses
- No .Result or .Wait() on async calls in request path

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer minimal APIs for small services; MVC/controllers when view-heavy or complex model binding.
- Use IMediator (MediatR) when handlers grow — keep MapPost one-liners as entry only.
- Health checks at /health; readiness includes DB ping.
- Use IOptions<T> for config — not static ConfigurationManager reads in handlers.

## Common Rationalizations And Rebuttals

- "Minimal APIs are only for demos." -> Production-ready with filters, auth, and testing patterns.
- "One file is fine." -> Split endpoint groups by domain as service grows.
- "Exception middleware is enough." -> Validate at boundary; return typed validation problems.

## Evidence Pack

- OpenAPI snapshot with security schemes
- Integration test output for authorized vs anonymous calls
- Endpoint filter unit test for validation failures
- Health/readiness probe configuration

## Exit Criteria

- Endpoints are typed, authorized, and documented
- Async and cancellation used throughout request path
- Error responses match API contract
