# Fullstack Development Agent Skills

Production-grade UI, backend microservice, and cloud fullstack skills for AI agents.

## Features

**117 workflow skills** (72 core + 45 stack packs) covering UI architecture, backend microservices, identity, edge delivery, and cloud infrastructure — all wired into a consistent 10-command delivery lifecycle.

### What's Included

| Asset | Count | Description |
|-------|-------|-------------|
| Core skills | 72 | Cross-stack SKILL.md workflows in `skills/` |
| Skill packs | 45 | Stack-specific playbooks in `skill-packs/` (Java, NestJS, .NET, Rust, Flutter, AI, etc.) |
| Presets | 15 | Stack-specific defaults (React, Angular, Vue, .NET, Java, Node, AWS, Azure, GCP) |
| Starter Packs | 20 | Opinionated bundles for MVP, SaaS, payments, reliability, microservices |
| Agent Adapters | 8 | Cursor, Claude, Gemini, Kiro, OpenCode, Windsurf, Copilot, Codex |
| Examples | 10 | Architecture blueprints (README-only design packs) |
| Case Studies | 3 | Real-world delivery scenarios |
| Hooks | 4 | Session start, release guard, review gate |
| MCP Templates | 5 | GitHub, Postgres, AWS, Azure, GCP integration |
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
| `FS Skills: Install Examples` | Install architecture blueprints |
| `FS Skills: Install Platform Preset` | Pick and install a stack-specific preset |
| `FS Skills: Open Skills Index` | Browse the full skills catalog |
| `FS Skills: Run Session Hook` | Execute session-start detection hook |

### Supported Editors

- VS Code
- Cursor
- Windsurf
- VSCodium

### Delivery Lifecycle

The toolkit provides a consistent 10-command lifecycle:

```text
/spec     - Define business outcome, UI states, API contracts, NFRs
/plan     - Split into frontend, backend, data, release-safe slices
/build    - Implement with contract and compatibility discipline
/validate - Run lint, tests, and checklist-driven verification
/review   - Evaluate architecture, security, performance risks
/ship     - Staged rollout, observability checks, rollback readiness
/migrate  - Zero-downtime schema, API, platform migrations
/harden   - Security, reliability, performance hardening
/incident - Triage, runbooks, postmortems
/optimize - Performance, cost, capacity improvements
```

### Platform Presets

- React / Next.js Frontend
- Fullstack TypeScript Monorepo
- Angular Enterprise Frontend
- Vue / Nuxt Frontend
- Node.js Microservices
- Java Spring Boot Microservices
- .NET / ASP.NET Core Microservices
- AWS Fullstack and Serverless
- Azure Fullstack and Serverless
- GCP Fullstack and Serverless
- Kubernetes Fullstack Platform
- Vercel / Jamstack

### Skill Packs

Stack-specific skills with `examples/` and `templates/`:

- Java: Spring Boot (22), Quarkus, Micronaut, Jakarta EE, Hibernate, Vaadin
- TypeScript: NestJS enterprise
- .NET: Minimal APIs, EF Core
- Rust: Axum | Kotlin: Ktor, Spring
- Python: FastAPI, Django | Go: Gin | PHP: Laravel | Ruby: Rails
- Flutter mobile | Data: MongoDB, Elasticsearch
- AI: LangChain, Vercel AI SDK

See `skill-packs/README.md` and `docs/fullstack-skills-catalog.md`.

### Starter Packs

- Fullstack MVP
- Enterprise Modernization
- Platform Reliability
- SaaS Multi-Tenant
- Payments and Subscriptions
- Incident Hardening and SLO
- Microservice Patterns and Edge Security
- Microservices Architecture Modernization
- Identity, Edge and Global Delivery
- UI Production Excellence
- AWS / Azure / GCP Serverless
- Multi-Cloud Platform
- Data Platform and Events
- Compliance and Privacy
- AI Features
- Mobile Fullstack
- Chaos and SRE
- GitOps CI/CD

## Development

```bash
cd vscode-extension
npm install
npm run compile
npm run package
```

## Build and Publish

```bash
# Package the extension
npx vsce package

# Publish to marketplace
npx vsce publish
```

## Links

- [GitHub Repository](https://github.com/vaquarkhan/Fullstack-development-agent-skills)
- [Website](https://vaquarkhan.github.io/Fullstack-development-agent-skills/)
- [JetBrains Plugin](https://plugins.jetbrains.com/plugin/32167-fullstack-development-agent-skills)
- [Skills Catalog](https://github.com/vaquarkhan/Fullstack-development-agent-skills/blob/main/docs/fullstack-skills-catalog.md)
- [Issues](https://github.com/vaquarkhan/Fullstack-development-agent-skills/issues)

## License

MIT
