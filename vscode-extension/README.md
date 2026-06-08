# Fullstack Development Agent Skills

Production-grade UI, backend microservice, and cloud fullstack skills for AI agents.

## Features

**53+ workflow skills** covering UI architecture, backend microservices, identity, edge delivery, and cloud infrastructure — all wired into a consistent delivery lifecycle.

### What's Included

| Asset | Count | Description |
|-------|-------|-------------|
| Skills | 53+ | Structured SKILL.md files with progressive disclosure |
| Presets | 15 | Stack-specific defaults (React, Angular, Vue, .NET, Java, Node, AWS, Azure, GCP) |
| Starter Packs | 14 | Opinionated bundles for MVP, SaaS, payments, reliability, microservices |
| Agent Adapters | 8 | Cursor, Claude, Gemini, Kiro, OpenCode, Windsurf, Copilot, Codex |
| Examples | 7 | End-to-end architecture scaffolds |
| Case Studies | 3 | Real-world delivery scenarios |
| Hooks | 4 | Session start, release guard, review gate |
| MCP Templates | 4 | GitHub, AWS, Azure, GCP integration |
| References | 14 | Operational checklists |

### Commands

Access via Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`):

| Command | Description |
|---------|-------------|
| `FS Skills: Install Full Toolkit` | Install complete toolkit into workspace |
| `FS Skills: Install Core Pack` | Install essential workflow skills |
| `FS Skills: Install Agent Adapters` | Install multi-agent configuration files |
| `FS Skills: Install Starter Pack` | Pick and install an opinionated starter bundle |
| `FS Skills: Install MCP Templates` | Install Model Context Protocol configs |
| `FS Skills: Install Examples` | Install architecture example scaffolds |
| `FS Skills: Install Platform Preset` | Pick and install a stack-specific preset |
| `FS Skills: Open Skills Index` | Browse the full skills catalog |
| `FS Skills: Run Session Hook` | Execute session-start detection hook |

### Supported Editors

- ✅ Visual Studio Code
- ✅ Cursor
- ✅ Windsurf
- ✅ VSCodium

### Delivery Lifecycle

The toolkit provides a consistent 6-command lifecycle:

```
/spec  → Define business outcome, UI states, API contracts, NFRs
/plan  → Split into frontend, backend, data, release-safe slices
/build → Implement with contract and compatibility discipline
/validate → Run lint, tests, and checklist-driven verification
/review → Evaluate architecture, security, performance risks
/ship  → Staged rollout, observability checks, rollback readiness
```

### Platform Presets

- React / Next.js Frontend
- Fullstack TypeScript Monorepo
- Angular Enterprise Frontend
- Vue / Nuxt Frontend
- Node.js Microservices
- Java Spring Boot Microservices
- .NET / ASP.NET Core Microservices
- AWS Fullstack & Serverless
- Azure Fullstack & Serverless
- GCP Fullstack & Serverless
- Kubernetes Fullstack Platform
- Vercel / Jamstack

### Starter Packs

- Fullstack MVP
- Enterprise Modernization
- Platform Reliability
- SaaS Multi-Tenant
- Payments & Subscriptions
- Incident Hardening & SLO
- Microservice Patterns & Edge Security
- Microservices Architecture Modernization
- Identity, Edge & Global Delivery

## Development

```bash
cd vscode-extension
npm install
npm run compile
npm run package
```

## Build & Publish

```bash
# Package the extension
npx vsce package

# Publish to marketplace
npx vsce publish
```

## Links

- [GitHub Repository](https://github.com/vaquarkhan/Fullstack-development-agent-skills)
- [Documentation](https://vaquarkhan.github.io/Fullstack-development-agent-skills/)
- [Issues](https://github.com/vaquarkhan/Fullstack-development-agent-skills/issues)

## License

MIT
