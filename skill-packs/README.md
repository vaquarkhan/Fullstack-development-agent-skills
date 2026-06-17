# Skill Packs

Segregated, stack-specific agent skills organized by language and framework.

Use **`skills/`** for cross-cutting fullstack workflow skills (spec, ship, observability, identity, cloud).  
Use **`skill-packs/`** for deep, stack-specific implementation playbooks.

## Catalog

| Pack | Path | Skills | Focus |
| --- | --- | --- | --- |
| Java Spring Boot | `skill-packs/java/spring-boot/` | 20 | Spring AI, MCP servers, JPA, Flyway, security, testing, agent core |
| Java Quarkus | `skill-packs/java/quarkus/` | 1 | Cloud-native APIs, native image, Kubernetes |
| Java Micronaut | `skill-packs/java/micronaut/` | 1 | Reactive microservices, compile-time DI |
| Python FastAPI | `skill-packs/python/fastapi/` | 1 | Async APIs, Pydantic, OpenAPI |
| Python Django | `skill-packs/python/django/` | 1 | DRF, Celery, enterprise patterns |
| Go Gin | `skill-packs/go/gin/` | 1 | REST microservices, clean architecture |
| PHP Laravel | `skill-packs/php/laravel/` | 1 | API platform, Sanctum, queues |
| Ruby Rails | `skill-packs/ruby/rails/` | 1 | API-only Rails, Sidekiq, policies |

## Spring Boot pack credits

The Spring Boot pack adapts skills from [spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) by @rrezartprebreza (MIT), extended with `java-agent-core` and gateway/reactive skills.

## Install

Copy a pack folder into your project agent skills directory:

```bash
# Claude Code / Cursor
cp -r skill-packs/java/spring-boot/spring-ai-integration .claude/skills/
cp -r skill-packs/java/spring-boot/mcp-server .cursor/skills/

# Or install entire Spring Boot pack
cp -r skill-packs/java/spring-boot/* .claude/skills/
```

## Validation

All skill packs follow the same schema as core `skills/` and are validated by:

```bash
python scripts/validate-skills.py
python scripts/check-skill-boilerplate.py
```
