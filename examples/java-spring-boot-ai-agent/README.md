# Example: Java Spring Boot AI Agent Platform

## Architecture

- `order-api`: Spring Boot REST + Spring AI ChatClient
- `order-mcp`: MCP tool server exposing order operations to external agents
- `shared-domain`: DTOs and service contracts shared across modules

## Skill Packs Used

- `skill-packs/java/spring-boot/spring-boot-enterprise-foundation`
- `skill-packs/java/spring-boot/spring-ai-integration`
- `skill-packs/java/spring-boot/mcp-server`
- `skill-packs/java/spring-boot/java-agent-core`
- `skill-packs/java/spring-boot/layered-architecture`

## Validation Commands

```bash
./mvnw -pl order-api test
./mvnw -pl order-mcp test
./mvnw verify
```

## Success Criteria

- ChatClient uses GA Spring AI coordinates (`spring-ai-starter-model-*`)
- MCP stdio server keeps stdout clean (banner off, logs to file)
- Agent tool calls go through service layer with auth checks
