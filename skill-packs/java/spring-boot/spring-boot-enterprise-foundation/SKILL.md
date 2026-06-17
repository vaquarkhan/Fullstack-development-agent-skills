---
name: spring-boot-enterprise-foundation
description: Build enterprise Spring Boot backends and microservices with auto-configuration, production defaults, and Spring AI integration paths. Use as the entry skill when choosing Spring Boot over other JVM frameworks.
disable-model-invocation: true
---

# Spring Boot Enterprise Foundation

## Use When

- Starting or extending enterprise Java backends with Spring Boot
- Microservices need convention-over-configuration and fast team onboarding
- Spring AI or LLM features must integrate alongside REST and data layers

## Workflow

1. Confirm Spring Boot 3.x baseline, Java 17+, and Maven/Gradle parent BOM.
2. Structure layered modules: web, service, domain, persistence, config.
3. Rely on auto-configuration for datasource, security, actuator — override only with `@Configuration` when needed.
4. Load stack-specific skills from this pack (JPA, Flyway, security, Spring AI, MCP).
5. Add Actuator health, metrics, and structured logging before production deploy.

## Required Checks

- Constructor injection throughout; no field `@Autowired` on new code
- Spring Boot BOM manages dependency versions — no manual version drift on core starters
- Actuator `/actuator/health` includes readiness for database and message brokers
- Profiles (`dev`, `staging`, `prod`) externalize secrets and connection strings

## Decision Framework

- Prefer Spring Boot when team knows Spring ecosystem, need Spring AI, or largest community support.
- Use `spring-ai-integration` skill for LLM/RAG; `mcp-server` for agent tool exposure.
- Use `layered-architecture` + `spring-data-jpa` + `flyway-migrations` for typical CRUD APIs.
- Defer custom auto-config until defaults fail — document why each override exists.

## Common Rationalizations And Rebuttals

- "We need XML config for control." -> Java `@Configuration` and properties are sufficient; XML adds maintenance cost.
- "Auto-config is magic we cannot trust." -> Document excluded auto-config; use `@SpringBootTest` to prove behavior.
- "Spring Boot is too heavy for microservices." -> Properly scoped services with Actuator and native/Graal options remain competitive.

## Evidence Pack

- `pom.xml` or `build.gradle` showing Spring Boot parent/BOM
- Layer diagram: controller → service → repository
- Actuator health output with dependency checks
- List of loaded sub-skills from `skill-packs/java/spring-boot/` for this feature

## Exit Criteria

- Service boots with profile-specific config and passing smoke tests
- Team knows which specialized Spring Boot skills to load next
- Auto-configuration overrides are documented and minimal
