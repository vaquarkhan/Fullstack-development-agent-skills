# Skill Packs

Segregated, stack-specific agent skills organized by language and framework.

Use **`skills/`** for cross-cutting fullstack workflow skills (spec, ship, observability, identity, cloud).  
Use **`skill-packs/`** for deep, stack-specific implementation playbooks.

## Catalog

| Pack | Path | Skills | Focus |
| --- | --- | --- | --- |
| Java Spring Boot | `skill-packs/java/spring-boot/` | 22 | Enterprise backend, Spring AI, MCP, JPA, security |
| Java Quarkus | `skill-packs/java/quarkus/` | 2 | Kubernetes-native, fast startup, native image |
| Java Micronaut | `skill-packs/java/micronaut/` | 2 | Compile-time DI, reactive microservices |
| Java Jakarta EE | `skill-packs/java/jakarta-ee/` | 1 | Standards-based enterprise (JAX-RS, CDI, JPA) |
| Java Hibernate | `skill-packs/java/hibernate/` | 1 | ORM modeling, fetch plans, caching |
| Java Vaadin | `skill-packs/java/vaadin/` | 1 | Full-stack Java UI (no client-side JS) |
| Python FastAPI | `skill-packs/python/fastapi/` | 1 | Async APIs, Pydantic, OpenAPI |
| Python Django | `skill-packs/python/django/` | 1 | DRF, Celery, enterprise patterns |
| Go Gin | `skill-packs/go/gin/` | 1 | REST microservices, clean architecture |
| PHP Laravel | `skill-packs/php/laravel/` | 1 | API platform, Sanctum, queues |
| Ruby Rails | `skill-packs/ruby/rails/` | 1 | API-only Rails, Sidekiq, policies |
| TypeScript NestJS | `skill-packs/typescript/nestjs/` | 1 | Enterprise NestJS modules, guards, OpenAPI |
| .NET Minimal APIs | `skill-packs/dotnet/aspnetcore/` | 1 | ASP.NET Core minimal endpoints, filters |
| EF Core | `skill-packs/dotnet/efcore/` | 1 | Migrations, configurations, query performance |
| Rust Axum | `skill-packs/rust/axum/` | 1 | Tokio microservices, Tower middleware |
| Kotlin Ktor | `skill-packs/kotlin/ktor/` | 1 | Coroutine-first JVM APIs |
| Kotlin Spring | `skill-packs/kotlin/spring/` | 1 | Idiomatic Kotlin on Spring Boot |
| Flutter | `skill-packs/flutter/` | 1 | Mobile architecture, offline sync |
| MongoDB | `skill-packs/data/mongodb/` | 1 | Document modeling, indexes, tenancy |
| Elasticsearch | `skill-packs/data/elasticsearch/` | 1 | Search indexes, sync, secure queries |
| LangChain | `skill-packs/ai/langchain/` | 1 | Python agent orchestration, tools |
| Vercel AI SDK | `skill-packs/ai/vercel-ai-sdk/` | 1 | Next.js streaming AI, tool calling |

**Total: 45 skills** across 22 packs.

## Spring Boot pack credits

The Spring Boot pack adapts skills from [spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) by @rrezartprebreza (MIT), extended with `java-agent-core` and gateway/reactive skills.

## Install

Copy a pack folder into your project agent skills directory:

```bash
# Claude Code / Cursor
cp -r skill-packs/typescript/nestjs/nestjs-enterprise-backend .cursor/skills/
cp -r skill-packs/dotnet/aspnetcore/aspnetcore-minimal-apis .claude/skills/

# Or install entire Spring Boot pack
cp -r skill-packs/java/spring-boot/* .claude/skills/
```

## Validation

All skill packs follow the same schema as core `skills/` and are validated by:

```bash
python scripts/validate-skills.py
python scripts/check-skill-boilerplate.py
```
