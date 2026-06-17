---
name: quarkus-cloud-native-apis
description: Build cloud-native REST and reactive APIs with Quarkus, GraalVM native images, and Kubernetes-ready health probes. Use for Java microservices targeting fast startup and low memory footprint.
disable-model-invocation: true
---

# Quarkus Cloud Native APIs

## Use When

- Building Java APIs with Quarkus instead of Spring Boot
- Native image compilation or Kubernetes-first deployment is required
- Sub-second startup and low memory footprint are goals

## Workflow

1. Define REST resources with JAX-RS or RESTEasy Reactive.
2. Use CDI (@ApplicationScoped) for services; avoid static singletons.
3. Configure datasource, Flyway/Liquibase, and health/liveness probes.
4. Add OpenTelemetry and Micrometer metrics via Quarkus extensions.
5. Build and test JVM mode first, then native profile in CI.

## Required Checks

- /q/health/live and /q/health/ready configured with dependency checks
- Panache or repository layer does not leak entities in REST responses
- Native build profile tested in CI or documented as manual gate
- Config externalized via application.properties and env vars

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer RESTEasy Reactive for high-concurrency I/O-bound endpoints.
- Use Panache active record only for simple CRUD; repository pattern for complex domains.
- Enable native image only after JVM-mode test suite is green.
- Use SmallRye Fault Tolerance for timeout, retry, and circuit breaker.

## Common Rationalizations And Rebuttals

- "Quarkus is just Spring Boot lite." -> CDI and extension model differ; follow Quarkus idioms.
- "Native build later." -> Native-incompatible reflection fails late; test native profile early.
- "Panache everywhere." -> Complex queries need repositories or projections.

## Evidence Pack

- Quarkus extension list and rationale
- Health probe output under dependency failure
- JVM vs native startup/memory comparison (if native enabled)
- OpenTelemetry trace sample through REST → service → DB

## Exit Criteria

- API runs in JVM mode with passing tests and health checks
- Cloud deployment manifests include probe paths and resource limits
- Observability and config follow twelve-factor expectations
