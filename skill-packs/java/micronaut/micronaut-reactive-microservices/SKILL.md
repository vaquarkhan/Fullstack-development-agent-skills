---
name: micronaut-reactive-microservices
description: Build reactive Micronaut microservices with compile-time DI, non-blocking I/O, and GraalVM-ready APIs. Use for low-latency Java services with Netty and Project Reactor.
disable-model-invocation: true
---

# Micronaut Reactive Microservices

## Use When

- Building reactive Java microservices with Micronaut
- Compile-time dependency injection and fast startup are priorities
- Non-blocking integration with databases, HTTP clients, or messaging

## Workflow

1. Define @Controller endpoints returning Mono/Flux for I/O-bound work.
2. Use @Singleton services with constructor injection (compile-time validated).
3. Configure Netty server, connection pools, and reactive data access.
4. Add Micronaut Security, validation, and OpenAPI where needed.
5. Verify with @MicronautTest and Testcontainers for integration paths.

## Required Checks

- Blocking calls not on event loop thread (use schedulers or blocking executor)
- HTTP client timeouts and retry policies configured explicitly
- Secrets via environment; no credentials in application.yml committed to git
- GraalVM native hints or build args documented if targeting native

## Decision Framework

- Prefer reactive end-to-end for high fan-out I/O; use blocking MVC style only when team lacks reactive expertise.
- Use Micronaut Data for repository abstraction; avoid leaking entities in API responses.
- Use declarative HTTP clients (@Client) with explicit read timeouts.
- Enable distributed tracing via Micronaut Tracing + OpenTelemetry.

## Common Rationalizations And Rebuttals

- "Blocking JDBC is fine on reactive threads." -> Blocks Netty event loop; offload or use reactive drivers.
- "Micronaut works like Spring." -> Annotation processors and config differ; follow Micronaut docs.
- "We can add timeouts later." -> Missing timeouts cause hung requests under load.

## Evidence Pack

- Thread/event-loop safety review for blocking calls
- Client timeout and circuit breaker configuration
- Integration test output with Testcontainers
- Trace showing non-blocking request path

## Exit Criteria

- Reactive endpoints handle load without event-loop blocking
- Services start quickly with compile-time DI validation at build time
- Security, config, and observability baselines are met
