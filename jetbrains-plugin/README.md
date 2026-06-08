# Fullstack Development Agent Skills — JetBrains Plugin

Native plugin for IntelliJ-platform IDEs. Install the fullstack skill toolkit directly into your JetBrains workflow.

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
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ViquarKhan.fullstack-development-agent-skills)

## License

MIT
