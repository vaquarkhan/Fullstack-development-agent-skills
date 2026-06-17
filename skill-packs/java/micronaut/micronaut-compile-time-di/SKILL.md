---
name: micronaut-compile-time-di
description: Build Micronaut microservices with compile-time dependency injection, zero runtime reflection, and GraalVM-ready APIs. Use when avoiding runtime reflection overhead and annotation processing at build time is preferred.
disable-model-invocation: true
---

# Micronaut Compile Time DI

## Use When

- Micronaut chosen for compile-time DI instead of Spring runtime reflection
- Microservices need fast startup with explicit dependency graphs validated at build
- GraalVM native image or low-overhead JVM deployment is a goal

## Workflow

1. Define `@Singleton` beans with constructor injection; let Micronaut generate wiring at compile time.
2. Use `@Controller` / `@Get` for HTTP; `@Client` for declarative HTTP clients.
3. Configure `application.yml`; use `@Requires` for conditional beans.
4. Run `mvn clean compile` — fix annotation processor errors before runtime.
5. Validate with `@MicronautTest` and native-image profile if targeting Graal.

## Required Checks

- No runtime component scanning surprises — dependencies visible in generated metadata
- `@Introspected` or records for Graal when using native image
- HTTP clients declare read timeouts and error handlers
- Build fails on circular dependency or missing bean at compile time (fix, do not suppress)

## Examples And Templates

See `examples/` for side-by-side good vs bad patterns agents commonly get wrong.
See `templates/` for copy-paste starters aligned with this skill.

## Decision Framework

- Prefer Micronaut when team wants Spring-like ergonomics with AOT-friendly DI.
- Pair with `micronaut-reactive-microservices` for WebFlux/Netty reactive endpoints.
- Use annotation processors (`micronaut-inject-java`) in IDE and CI consistently.
- Avoid mixing Spring beans in same app unless using micronaut-spring bridge deliberately.

## Common Rationalizations And Rebuttals

- "Compile-time DI is the same as Spring." -> Micronaut validates graph at build; different troubleshooting path.
- "Reflection at runtime is fine." -> Defeats Micronaut's startup and native-image advantages.
- "Skip annotation processor in IDE." -> Drift between IDE and CI causes missing bean errors.

## Evidence Pack

- Generated `$BeanDefinition` or build log showing processed beans
- Compile-time failure fix documentation (if any circular deps resolved)
- Startup benchmark vs equivalent Spring Boot service (optional)
- Native build success log or explicit JVM-only decision record

## Exit Criteria

- Application wiring validated at compile time with green build
- No accidental runtime reflection for core DI paths
- Team understands Micronaut annotation processor workflow
