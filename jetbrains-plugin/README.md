# Fullstack Development Agent Skills — JetBrains Plugin

Native plugin for IntelliJ-platform IDEs. Install the fullstack skill toolkit (117 skills: 72 core + 45 packs) directly into your JetBrains workflow.

## Supported IDEs

- IntelliJ IDEA
- PyCharm
- WebStorm
- DataGrip
- GoLand
- PhpStorm
- Rider
- CLion
- RubyMine

## Commands

Access via **Tools > Fullstack Agent Skills** menu:

| Command | Description |
|---------|-------------|
| Install Full Toolkit | Install all skills, presets, adapters, and templates |
| Install Core Skills | Install essential workflow skills |
| Install Platform Preset | Choose and install a stack-specific preset |
| Install Starter Pack | Choose and install a starter bundle |
| Install Agent Adapters | Install multi-agent configuration files |
| Install MCP Templates | Install Model Context Protocol configs |
| Run Session Hook | Execute session-start detection hook |

## Skill Packs

Stack-specific skills live in `skill-packs/`:

- Java: Spring Boot (22), Quarkus, Micronaut, Jakarta EE, Hibernate, Vaadin
- TypeScript: NestJS | .NET: Minimal APIs, EF Core | Rust: Axum
- Kotlin: Ktor, Spring | Python: FastAPI, Django | Go: Gin | PHP: Laravel | Ruby: Rails
- Flutter | Data: MongoDB, Elasticsearch | AI: LangChain, Vercel AI SDK

See `skill-packs/README.md` and `docs/fullstack-skills-catalog.md`.

## Build

```bash
cd jetbrains-plugin
./gradlew buildPlugin
```

The `.zip` plugin file will be in `build/distributions/`.

## Install from ZIP

1. Open your JetBrains IDE
2. **Settings > Plugins > ⚙️ > Install Plugin from Disk...**
3. Select the `.zip` file from `build/distributions/`

## Development

```bash
# Run in sandbox IDE for testing
./gradlew runIde

# Build plugin ZIP
./gradlew buildPlugin
```

## Links

- [GitHub Repository](https://github.com/vaquarkhan/Fullstack-development-agent-skills)
- [Website](https://vaquarkhan.github.io/Fullstack-development-agent-skills/)
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ViquarKhan.fullstack-development-agent-skills)
- [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/32167-fullstack-development-agent-skills)
- [Skills Catalog](https://github.com/vaquarkhan/Fullstack-development-agent-skills/blob/main/docs/fullstack-skills-catalog.md)

## License

MIT
