---
name: kotlin-spring-boot
description: Build Spring Boot services in idiomatic Kotlin with coroutines, data classes, extension functions, and Spring AI integration. Use when JVM teams prefer Kotlin over Java for Spring microservices.
disable-model-invocation: true
---

# Kotlin Spring Boot

## Use When

- Building Spring Boot microservices in Kotlin (not Java)
- Using suspend controllers, coroutines with WebFlux or MVC + coroutines
- Pairing with `skill-packs/java/spring-boot/` skills for Spring ecosystem depth

## Workflow

1. Use Kotlin data classes for DTOs with jakarta.validation annotations.
2. Prefer constructor injection and `val` immutability in services.
3. Enable coroutines for I/O-bound service methods where supported.
4. Configure Jackson Kotlin module or kotlinx.serialization consistently.
5. Reuse Spring Boot patterns: Actuator, ProblemDetail, Testcontainers.
6. Test with @WebMvcTest and coroutine test utilities (runTest).

## Required Checks

- No platform types (String!) in public API models
- Null-safety enforced at boundaries — avoid Map<String, Any?>
- Spring Security Kotlin DSL or Java config — document chosen style
- Detekt/ktlint in CI for consistent style

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Share patterns with Java Spring Boot pack — differ only in Kotlin idioms.
- Use extension functions for mapping, not inheritance-heavy hierarchies.
- Flow API for streaming when paired with WebFlux or SSE endpoints.
- Spring AI ChatClient works identically — prefer Kotlin data classes for prompts.

## Common Rationalizations And Rebuttals

- "Java patterns pasted to Kotlin are fine." -> Use data classes, sealed errors, and coroutines idiomatically.
- "!! operator saves time." -> Model nullability explicitly at API boundary.
- "Skip Detekt." -> Kotlin style drift makes reviews harder at scale.

## Evidence Pack

- Detekt/ktlint CI output
- Coroutine controller integration test results
- DTO schema diff for API changes
- Comparison note linking to relevant Java Spring Boot skill

## Exit Criteria

- Kotlin idioms used throughout service and API layers
- Spring Boot operational baselines (health, metrics, security) met
- Tests cover suspend endpoints and validation failures
