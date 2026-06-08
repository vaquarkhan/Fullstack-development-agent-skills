# Fullstack Development Agent Skills

Production-grade UI, backend microservice, and cloud fullstack skills for AI agents.

This repository is structured as an open skill registry:

- each capability lives in a directory containing a `SKILL.md`
- each `SKILL.md` starts with YAML frontmatter (`name`, `description`)
- workflow support material lives in `references/`, `templates/`, and `presets/`

## What Makes This Collection Distinct

- Fullstack-first workflows that tie UI architecture, backend contracts, auth, and release safety together
- Reviewer personas specialized for frontend quality, backend reliability, and threat-focused security reviews
- Starter packs for MVP delivery, enterprise modernization, and reliability hardening
- Built-in lifecycle command routing (`/spec`, `/plan`, `/build`, `/validate`, `/review`, `/ship`, `/migrate`, `/harden`, `/incident`, `/optimize`) for consistent execution
- **72** workflow skills, **15** stack presets, **20** starter packs — see [`skills-index.md`](skills-index.md) and [`registry/assets.json`](registry/assets.json)
- Multi-agent adapter surfaces for `Cursor`, `Claude`, `Gemini`, `Kiro`, `OpenCode`, `Windsurf`, `Copilot`, and generic `AGENTS.md` consumers

## Quick Start

1. Load `skills/using-fullstack-agent-skills/SKILL.md`
2. Pick one preset from `presets/` based on your stack
3. Use one workflow skill from `skills/`
4. Validate with checklists in `references/`

## Skill Pack

All skills live under `skills/<name>/SKILL.md` with decision frameworks, evidence packs, and exit criteria. Browse the full catalog in [`skills-index.md`](skills-index.md).

Categories include: product specification, UI/UX and design systems, React/Next.js/Angular/Vue, backend microservices (Node, Java, .NET), API contracts, auth, testing, observability, payments, incidents, microservice patterns (saga, outbox, mesh, CQRS), identity and edge (OAuth, Okta, Cognito, NGINX, CDN, API gateway), cloud and serverless (AWS, Azure, GCP, Kubernetes, Terraform, Vercel), UI production (CSP, WCAG, GraphQL BFF, realtime), and platform operations (Postgres, Redis, Kafka, GDPR, GitOps, chaos, load testing, AI/LLM, multi-tenant, DR, cost optimization, mobile, E2E).

## Presets

- `react-nextjs-frontend`, `fullstack-typescript-monorepo`, `angular-frontend`, `vue-nuxt-frontend`
- `nodejs-microservices`, `java-spring-boot-microservices`, `dotnet-aspnet-core-microservices`
- `aws-fullstack-development`, `azure-fullstack-development`, `gcp-fullstack-development`
- `aws-serverless-fullstack`, `azure-serverless-fullstack`, `gcp-serverless-fullstack`
- `vercel-nextjs-jamstack`, `kubernetes-fullstack-platform`

## Starter Packs

Twenty YAML bundles under `starter-packs/` — MVP, enterprise modernization, SaaS multi-tenant, payments, incidents, microservices, identity/edge, UI excellence, per-cloud serverless, multi-cloud platform, data/events, compliance, AI features, mobile, chaos/SRE, and GitOps CI/CD.

## Project Structure

```text
fullstack-development-agent-skills/
├── .cursor/commands/
├── .claude/commands/
├── .gemini/commands/
├── .kiro/steering/
├── .opencode/
├── .github/workflows/
├── .github/copilot-instructions.md
├── agents/
├── registry/
├── scripts/
├── skills/
├── presets/
├── starter-packs/
├── references/
├── templates/
├── docs/
└── skills-index.md
```

## Fullstack Delivery Lifecycle

- `/spec` define business outcome, UI states, API contracts, and non-functional requirements
- `/plan` split work into frontend, backend, data, and release-safe slices
- `/build` implement incrementally with contract and compatibility discipline
- `/validate` run lint, tests, and checklist-driven verification
- `/review` evaluate architecture, security, performance, and operability risks
- `/ship` roll out with staged deployment, observability checks, and rollback readiness
- `/migrate` plan zero-downtime schema, API, and platform migrations
- `/harden` apply security, reliability, and performance hardening
- `/incident` triage production issues with runbook discipline
- `/optimize` improve performance, cost, and capacity

## Bootstrap and Validation

```bash
./bootstrap.sh          # or bootstrap.ps1 on Windows
python scripts/validate-skills.py
python scripts/validate-assets.py
python scripts/sync-registry.py      # refresh registry after adding assets
python scripts/sync-skills-index.py  # refresh skills-index.md
```

## Contributing

Contributions should be specific, verifiable, and workflow-focused.

Use `docs/skill-anatomy.md` for required skill structure and quality gates.

## IDE Plugins

| IDE | Link |
| --- | --- |
| VS Code / Cursor / Windsurf | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ViquarKhan.fullstack-development-agent-skills) |
| IntelliJ / PyCharm / WebStorm | [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/32167-fullstack-development-agent-skills) |

## Install Scripts

- `scripts/install.sh <tool|all> <target-path>`
- `scripts/install.ps1 -Tool <tool|all> -Target <target-path>`

Supported tools: `cursor`, `claude`, `gemini`, `kiro`, `opencode`, `windsurf`, `copilot`, `codex`, `generic`, `all`.
