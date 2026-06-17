# Routing And Lifecycle Guide

How to route work through the repository for consistent fullstack delivery.

## Lifecycle (10 commands)

| Command | Purpose |
| --- | --- |
| `/spec` | Outcomes, contracts, risk boundaries |
| `/plan` | Sequenced implementation slices |
| `/build` | Contract-disciplined implementation |
| `/validate` | Quality, security, operational safety |
| `/review` | Frontend, reliability, security lenses |
| `/ship` | Staged rollout, rollback triggers |
| `/migrate` | Zero-downtime schema and platform changes |
| `/harden` | Security, reliability, performance |
| `/incident` | Triage and runbook execution |
| `/optimize` | Performance, cost, capacity |

Command docs: `.cursor/commands/` and `.claude/commands/`.

## Two-Layer Routing

### Layer 1: Core skills (`skills/`)

Cross-stack patterns — use for delivery workflow and architecture decisions:

| Work type | Start with |
| --- | --- |
| New feature (UI + API) | `fullstack-product-specification` |
| React / Next.js UI | `react-nextjs-frontend-architecture` |
| Node.js services | `nodejs-nestjs-backend-microservices` |
| Java services (overview) | `java-spring-boot-microservices` |
| API contracts | `api-contract-first-development` |
| Auth / permissions | `authentication-and-authorization-fullstack` |
| Database migrations | `database-migrations-zero-downtime` |
| Release / observability | `fullstack-observability-and-release-engineering` |
| Incidents | `incident-triage-and-oncall-runbooks` |
| AI features (generic) | `ai-llm-integration-in-fullstack-apps` |

Full routing table: `skills/using-fullstack-agent-skills/SKILL.md`.

### Layer 2: Skill packs (`skill-packs/`)

Stack-specific implementation — use when coding in a specific framework:

| Stack | Path | Examples |
| --- | --- | --- |
| Spring Boot + Spring AI | `skill-packs/java/spring-boot/` | `spring-ai-integration`, `mcp-server`, `java-agent-core` |
| Quarkus / Micronaut | `skill-packs/java/quarkus/`, `micronaut/` | K8s native, reactive APIs |
| Jakarta EE / Hibernate / Vaadin | `skill-packs/java/jakarta-ee/`, `hibernate/`, `vaadin/` | Regulated enterprise, ORM, Java UI |
| Python | `skill-packs/python/` | FastAPI, Django |
| Go / PHP / Ruby | `skill-packs/go/`, `php/`, `ruby/` | Gin, Laravel, Rails |
| TypeScript NestJS | `skill-packs/typescript/nestjs/` | Enterprise modules, DTOs |
| .NET | `skill-packs/dotnet/` | Minimal APIs, EF Core |
| Rust / Kotlin | `skill-packs/rust/`, `kotlin/` | Axum, Ktor, Kotlin Spring |
| Flutter | `skill-packs/flutter/` | Mobile client architecture |
| Data | `skill-packs/data/` | MongoDB, Elasticsearch |
| AI SDKs | `skill-packs/ai/` | LangChain, Vercel AI SDK |

Each pack skill includes `examples/` (good vs bad) and `templates/`.

## Preset Selection

Pick the closest preset from `presets/` before `/build`:

- `react-nextjs-frontend`, `angular-frontend`, `vue-nuxt-frontend`
- `nodejs-microservices`, `java-spring-boot-microservices`, `dotnet-aspnet-core-microservices`
- `aws-fullstack-development`, `azure-fullstack-development`, `gcp-fullstack-development`
- `kubernetes-fullstack-platform`, `vercel-nextjs-jamstack`

## Starter Pack Selection

| Goal | Starter pack |
| --- | --- |
| Fast MVP | `fullstack-mvp-starter.yaml` |
| SaaS multi-tenant | `saas-multi-tenant-starter.yaml` |
| Payments | `payments-and-subscriptions-starter.yaml` |
| Microservices migration | `microservices-architecture-modernization-starter.yaml` |
| Platform reliability | `platform-reliability-starter.yaml` |
| GitOps CI/CD | `gitops-cicd-starter.yaml` |

## Routing Benchmark

Run `python scripts/run-skill-routing-benchmark.py` to verify lifecycle commands and skill paths exist. Scenarios in `evals/skill-routing-benchmark.md`.
