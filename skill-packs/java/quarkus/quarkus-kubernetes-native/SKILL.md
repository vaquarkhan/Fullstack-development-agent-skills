---
name: quarkus-kubernetes-native
description: Deploy container-first Quarkus applications on Kubernetes with fast startup, low memory, native images, and health probes. Use when Quarkus is chosen specifically for cloud/Kubernetes efficiency over Spring Boot.
disable-model-invocation: true
---

# Quarkus Kubernetes Native

## Use When

- Targeting Kubernetes with sub-second startup and minimal container memory
- Building container-first Java services with Quarkus extensions
- Native image (GraalVM) or JVM mode in distroless containers

## Workflow

1. Add `quarkus-kubernetes`, `quarkus-container-image-*`, and health extensions.
2. Configure `application.properties` for K8s service discovery and config maps/secrets.
3. Expose `/q/health/live` and `/q/health/ready` with dependency checks.
4. Build with `-Dquarkus.package.jar.type=uber-jar` (JVM) or `-Dnative` profile.
5. Deploy with resource limits derived from native vs JVM benchmarks.

## Required Checks

- Liveness vs readiness probes hit correct Quarkus health endpoints
- Config injected via env vars or K8s secrets — not baked into image
- Native build runs in CI or release pipeline with documented JDK/Graal version
- Horizontal Pod Autoscaler metrics tied to CPU or custom Micrometer metrics

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer Quarkus over Spring Boot when cold start and memory dominate cost (serverless K8s, high churn).
- Start JVM mode in dev; gate native builds on release tags or nightly CI.
- Use Quarkus Dev Services locally; Testcontainers in CI for parity.
- Combine with `quarkus-cloud-native-apis` for REST and persistence patterns.

## Common Rationalizations And Rebuttals

- "Native build is optional forever." -> Production memory/startup targets often require native; test early.
- "Same Docker image as Spring." -> Quarkus fast-jar and native layouts differ; follow Quarkus guides.
- "Health checks are optional on K8s." -> Without readiness, traffic hits starting pods.

## Evidence Pack

- Dockerfile or `quarkus-container-image` build config
- K8s manifest with probe paths and resource requests/limits
- Startup time and memory comparison (JVM vs native)
- HPA or scaling test notes

## Exit Criteria

- Service passes K8s readiness under dependency failure simulation
- Container image size and startup meet SLO targets
- Config and secrets management documented for each environment
