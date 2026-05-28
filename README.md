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
- Built-in lifecycle command routing (`/spec`, `/plan`, `/build`, `/validate`, `/review`, `/ship`) for consistent execution

## Quick Start

1. Load `skills/using-fullstack-agent-skills/SKILL.md`
2. Pick one preset from `presets/` based on your stack
3. Use one workflow skill from `skills/`
4. Validate with checklists in `references/`

## Skill Pack

- `using-fullstack-agent-skills`
- `fullstack-product-specification`
- `ui-engineering-and-design-systems`
- `react-nextjs-frontend-architecture`
- `angular-enterprise-frontend`
- `vue-nuxt-frontend`
- `backend-microservices-architecture`
- `nodejs-nestjs-backend-microservices`
- `java-spring-boot-microservices`
- `dotnet-aspnet-core-microservices`
- `api-contract-first-development`
- `authentication-and-authorization-fullstack`
- `fullstack-testing-and-quality-gates`
- `fullstack-observability-and-release-engineering`
- `feature-flags-and-progressive-delivery`
- `database-migrations-zero-downtime`
- `distributed-caching-and-invalidation`
- `bff-architecture-and-api-aggregation`
- `payments-and-webhook-reliability`
- `incident-triage-and-oncall-runbooks`
- `cloud-fullstack-development`

## Presets

- `react-nextjs-frontend`
- `fullstack-typescript-monorepo`
- `angular-frontend`
- `vue-nuxt-frontend`
- `nodejs-microservices`
- `java-spring-boot-microservices`
- `dotnet-aspnet-core-microservices`
- `aws-fullstack-development`
- `azure-fullstack-development`
- `gcp-fullstack-development`

## Project Structure

```text
fullstack-development-agent-skills/
├── .cursor/commands/
├── .github/workflows/
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

## Contributing

Contributions should be specific, verifiable, and workflow-focused.

Use `docs/skill-anatomy.md` for required skill structure and quality gates.

## Install Scripts

- `scripts/install.sh <tool|all> <target-path>`
- `scripts/install.ps1 -Tool <tool|all> -Target <target-path>`
