# Fullstack Development Agent Skills

[![VS Code Marketplace](https://img.shields.io/visual-studio-marketplace/v/ViquarKhan.fullstack-development-agent-skills?label=VS%20Code&color=blue)](https://marketplace.visualstudio.com/items?itemName=ViquarKhan.fullstack-development-agent-skills)
[![JetBrains Plugin](https://img.shields.io/badge/JetBrains-Marketplace-orange)](https://plugins.jetbrains.com/plugin/32167-fullstack-development-agent-skills)
[![Website](https://img.shields.io/badge/Website-Live-green)](https://vaquarkhan.github.io/Fullstack-development-agent-skills/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Production-grade workflow skills for AI coding agents. The open skill registry that gives AI agents the operating procedures to **spec, plan, build, validate, review, and ship** fullstack applications with engineering discipline.

## At a Glance

| Asset | Count | Description |
|-------|-------|-------------|
| **Skills** | 72 | Structured SKILL.md playbooks with decision frameworks and evidence gates |
| **Presets** | 15 | Stack-specific defaults for instant onboarding |
| **Starter Packs** | 20 | Opinionated YAML bundles for common scenarios |
| **Agent Adapters** | 8 | Cursor, Claude, Gemini, Kiro, OpenCode, Windsurf, Copilot, Codex |
| **References** | 16 | Operational readiness checklists |
| **Tutorials** | 12 | Guided adoption walkthroughs |
| **Examples** | 7 | Architecture-oriented runnable scaffolds |
| **MCP Templates** | 8 | Model Context Protocol configurations |
| **Case Studies** | 3 | End-to-end delivery scenarios |
| **Review Agents** | 6 | Specialized reviewer personas |

## Quick Start

```bash
# Clone
git clone https://github.com/vaquarkhan/Fullstack-development-agent-skills.git
cd Fullstack-development-agent-skills

# Install for your AI tool
./scripts/install.sh cursor /path/to/project

# Or install for all supported tools
./scripts/install.sh all /path/to/project

# Windows (PowerShell)
.\scripts\install.ps1 -Tool cursor -Target C:\project
```

**Supported tools:** `cursor`, `claude`, `gemini`, `kiro`, `opencode`, `windsurf`, `copilot`, `codex`, `generic`, `all`

## IDE Plugins

Install directly from your IDE marketplace:

| IDE | Install Link | Supported Editors |
|-----|-------------|-------------------|
| **VS Code** | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ViquarKhan.fullstack-development-agent-skills) | VS Code, Cursor, Windsurf, VSCodium |
| **JetBrains** | [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/32167-fullstack-development-agent-skills) | IntelliJ, PyCharm, WebStorm, DataGrip, GoLand, Rider |

## Fullstack Delivery Lifecycle

Ten commands route every task through a consistent delivery pipeline:

| Command | Purpose |
|---------|---------|
| `/spec` | Define business outcome, UI states, API contracts, and NFRs |
| `/plan` | Split into frontend, backend, data, and release-safe slices |
| `/build` | Implement with contract and compatibility discipline |
| `/validate` | Run lint, tests, and checklist-driven verification |
| `/review` | Evaluate architecture, security, performance, operability |
| `/ship` | Staged rollout, observability checks, rollback readiness |
| `/migrate` | Zero-downtime schema, API, and platform migrations |
| `/harden` | Security, reliability, and performance hardening |
| `/incident` | Triage production issues with runbook discipline |
| `/optimize` | Improve performance, cost, and capacity |

## Skills Catalog (72)

### UI & Frontend Architecture
- `react-nextjs-frontend-architecture` — React/Next.js App Router, RSC, streaming
- `angular-enterprise-frontend` — Angular signals, standalone components, enterprise patterns
- `vue-nuxt-frontend` — Vue 3 Composition API, Nuxt 3, Pinia
- `ui-engineering-and-design-systems` — Component libraries, tokens, Storybook
- `nextjs-app-router-and-streaming-ui` — App Router, streaming, suspense boundaries
- `design-system-governance-and-tokens` — Token management, theme propagation
- `frontend-security-csp-and-xss-hardening` — CSP policies, XSS prevention
- `web-accessibility-wcag-compliance` — WCAG 2.1 AA/AAA compliance
- `graphql-client-and-bff-integration` — Apollo, urql, BFF patterns
- `realtime-ui-websockets-and-sse` — WebSocket, SSE, live updates
- `internationalization-and-localization` — i18n, l10n, RTL support

### Backend & Microservices
- `backend-microservices-architecture` — Service design, boundaries, communication
- `nodejs-nestjs-backend-microservices` — NestJS, Express, event-driven
- `java-spring-boot-microservices` — Spring Cloud, reactive, Kafka
- `dotnet-aspnet-core-microservices` — Minimal APIs, MediatR, EF Core
- `api-contract-first-development` — OpenAPI, contract testing, versioning
- `bff-architecture-and-api-aggregation` — Backend-for-frontend, aggregation layer
- `interservice-protocol-selection-rest-grpc-graphql` — REST vs gRPC vs GraphQL

### Microservice Patterns
- `microservice-patterns-saga-and-compensation` — Distributed transactions
- `microservice-patterns-outbox-and-cdc` — Transactional outbox, change data capture
- `microservice-patterns-service-mesh-and-traffic-management` — Istio, Linkerd, traffic control
- `cqrs-and-event-sourcing-patterns` — Command/query separation, event stores
- `domain-driven-service-decomposition` — Bounded contexts, aggregates
- `distributed-monolith-detection-and-remediation` — Coupling detection, decoupling
- `monolith-to-microservices-migration-strategy` — Strangler fig, incremental extraction
- `resilience-timeouts-retries-and-circuit-breakers` — Bulkhead, retry, circuit breaker
- `kafka-event-backbone-patterns` — Kafka topics, consumers, exactly-once

### Identity & Security
- `authentication-and-authorization-fullstack` — AuthN/AuthZ patterns
- `oauth2-oidc-and-token-lifecycle` — Token refresh, rotation, revocation
- `okta-identity-integration-patterns` — Okta SDK, SSO, MFA
- `aws-cognito-authentication-patterns` — User pools, identity pools
- `secrets-vault-and-key-rotation` — HashiCorp Vault, AWS Secrets Manager
- `compliance-gdpr-and-data-privacy-fullstack` — GDPR, CCPA, data minimization

### Edge & Delivery
- `nginx-edge-routing-and-security` — Reverse proxy, rate limiting, WAF
- `load-balancer-strategy-and-traffic-distribution` — ALB/NLB, weighted routing
- `cdn-caching-and-edge-acceleration-patterns` — CloudFront, Fastly, edge caching
- `api-gateway-and-edge-security` — API Gateway, throttling, auth at edge
- `frontend-load-balancing-and-global-delivery` — Global CDN, multi-region
- `autoscaling-capacity-and-cost-guardrails` — HPA, KEDA, cost alerts

### Cloud & Serverless
- `cloud-fullstack-development` — Cloud-native architecture patterns
- `aws-serverless-fullstack-architecture` — Lambda, API Gateway, DynamoDB, CDK
- `azure-serverless-fullstack-architecture` — Functions, APIM, Cosmos DB, Bicep
- `gcp-serverless-fullstack-architecture` — Cloud Run, Pub/Sub, Firestore
- `serverless-event-driven-and-workflow-orchestration` — Step Functions, Durable Functions
- `kubernetes-fullstack-platform-engineering` — Helm, ArgoCD, platform eng
- `terraform-fullstack-infrastructure-as-code` — Modules, state, drift detection
- `vercel-edge-and-jamstack-delivery` — Edge functions, ISR, CDN-first
- `cloud-cost-optimization` — FinOps, right-sizing, reserved capacity
- `multi-cloud-disaster-recovery` — Active-passive, active-active DR

### Data & Storage
- `database-migrations-zero-downtime` — Online DDL, expand-contract
- `distributed-caching-and-invalidation` — Cache-aside, write-through, TTL
- `postgres-and-relational-data-modeling` — Schema design, indexing, partitioning
- `redis-caching-and-session-store-patterns` — Redis clusters, pub/sub, streams
- `multi-tenant-data-isolation-patterns` — Row-level, schema-level, DB-level

### Operations & Reliability
- `fullstack-observability-and-release-engineering` — Metrics, logs, traces, SLOs
- `observability-distributed-tracing-and-ebpf-strategy` — OpenTelemetry, eBPF
- `feature-flags-and-progressive-delivery` — LaunchDarkly, Unleash, canary
- `incident-triage-and-oncall-runbooks` — PagerDuty, runbooks, postmortems
- `cicd-gitops-and-progressive-deployment` — GitHub Actions, ArgoCD, Flux
- `chaos-engineering-and-failure-injection` — Chaos Monkey, Litmus, GameDay
- `performance-and-load-testing-fullstack` — k6, Gatling, load profiles

### Payments & Integration
- `payments-and-webhook-reliability` — Stripe, idempotency, reconciliation
- `email-and-notification-delivery` — SES, SendGrid, push notifications
- `file-storage-and-media-delivery` — S3, presigned URLs, CDN delivery
- `search-and-discovery-experience` — Elasticsearch, Algolia, faceted search
- `mobile-api-and-offline-sync-patterns` — Offline-first, conflict resolution
- `react-native-fullstack-integration` — React Native + backend integration

### Testing & Quality
- `fullstack-testing-and-quality-gates` — Unit, integration, E2E strategy
- `fullstack-product-specification` — PRD, acceptance criteria, contracts
- `e2e-testing-playwright-cypress` — Playwright, Cypress, visual regression

### AI & Advanced
- `ai-llm-integration-in-fullstack-apps` — LLM APIs, RAG, embeddings, guardrails
- `using-fullstack-agent-skills` — Meta-skill for navigating this registry

## Presets (15)

Stack-specific defaults that configure skills for your technology:

| Preset | Stack |
|--------|-------|
| `react-nextjs-frontend` | React 18+, Next.js App Router, Tailwind |
| `fullstack-typescript-monorepo` | Turborepo, shared types, pnpm workspaces |
| `angular-frontend` | Angular 17+, signals, standalone |
| `vue-nuxt-frontend` | Vue 3, Nuxt 3, Pinia, VueUse |
| `nodejs-microservices` | NestJS, Express, Fastify, DDD |
| `java-spring-boot-microservices` | Spring Cloud, reactive, Kafka |
| `dotnet-aspnet-core-microservices` | .NET 8, Minimal APIs, MediatR |
| `aws-fullstack-development` | AWS CDK, Lambda, CloudFront |
| `azure-fullstack-development` | Bicep, Functions, Static Web Apps |
| `gcp-fullstack-development` | Cloud Run, Pub/Sub, Firebase |
| `aws-serverless-fullstack` | SAM, DynamoDB, Cognito |
| `azure-serverless-fullstack` | Durable Functions, Cosmos DB |
| `gcp-serverless-fullstack` | Cloud Functions, Firestore |
| `kubernetes-fullstack-platform` | Helm, ArgoCD, Istio |
| `vercel-nextjs-jamstack` | Vercel Edge, ISR, KV |

## Starter Packs (20)

Opinionated YAML bundles that combine skills + presets + references for common scenarios:

- `fullstack-mvp-starter` — Ship a product in weeks
- `enterprise-modernization-starter` — Legacy to modern migration
- `saas-multi-tenant-starter` — Multi-tenant SaaS platform
- `payments-and-subscriptions-starter` — Billing, webhooks, reconciliation
- `platform-reliability-starter` — SLOs, incident response, chaos
- `incident-hardening-and-slo-starter` — On-call, runbooks, error budgets
- `microservice-patterns-and-edge-security-starter` — Service mesh + edge
- `microservices-architecture-modernization-starter` — Monolith decomposition
- `identity-edge-and-global-delivery-starter` — Auth + CDN + global routing
- `ui-production-excellence-starter` — Design systems, a11y, performance
- `aws-serverless-fullstack-starter` — AWS Lambda + DynamoDB + CloudFront
- `azure-serverless-fullstack-starter` — Azure Functions + Cosmos DB
- `gcp-serverless-fullstack-starter` — Cloud Run + Firestore + Pub/Sub
- `multi-cloud-fullstack-platform-starter` — Hybrid cloud patterns
- `data-platform-and-events-starter` — Kafka, CDC, event sourcing
- `compliance-privacy-starter` — GDPR, CCPA, audit trails
- `ai-features-starter` — LLM integration, RAG, embeddings
- `mobile-fullstack-starter` — React Native + backend APIs
- `chaos-sre-starter` — Chaos engineering, SRE practices
- `gitops-cicd-starter` — GitHub Actions, ArgoCD, progressive delivery

## Multi-Agent Adapters

Works with every major AI coding assistant:

| Agent | Adapter Path | Format |
|-------|-------------|--------|
| Cursor | `.cursor/commands/` | Markdown command files |
| Claude | `.claude/commands/` + `CLAUDE.md` | Command files + project doc |
| Gemini | `.gemini/commands/` | Markdown command files |
| Kiro | `.kiro/steering/` | Steering workflow files |
| OpenCode | `.opencode/` | Config + docs |
| Windsurf | `.windsurfrules.example` | Rules file |
| Copilot | `.github/copilot-instructions.md` | Instructions file |
| Codex/Generic | `AGENTS.md` | Universal agent doc |

## Review Agents

Specialized reviewer personas in `agents/`:

- `backend-reliability-reviewer` — Circuit breakers, retry storms, data integrity
- `frontend-quality-reviewer` — Accessibility, performance, UX consistency
- `security-threat-reviewer` — OWASP, injection, auth bypass, supply chain
- Plus 3 additional domain reviewers

## Architecture Examples

| Example | Architecture |
|---------|-------------|
| React + Next.js + NestJS Monorepo | Full TypeScript monorepo with shared contracts |
| SaaS Multi-Tenant BFF | Tenant isolation, API aggregation, auth flows |
| Payments Webhook Platform | Reliable processing, retries, reconciliation |
| AWS Edge Fullstack Delivery | Lambda@Edge + CloudFront + S3 |
| AWS Lambda API + CloudFront SPA | Serverless API + SPA distribution |
| Azure APIM + Functions + Static Web App | Azure-native fullstack |
| GCP Cloud Run + Pub/Sub + Next.js | Event-driven GCP fullstack |

## Case Studies

- **SaaS Multi-Tenant Platform Launch** — End-to-end multi-tenant delivery
- **Payments Subscription Reliability** — Webhook processing and billing
- **Monolith to Microservices Cutover** — Staged migration with dual-run validation

## Project Structure

```
fullstack-development-agent-skills/
├── skills/                    # 72 workflow skill playbooks
├── presets/                   # 15 stack-specific configurations
├── starter-packs/             # 20 opinionated YAML bundles
├── references/                # 16 operational checklists
├── tutorials/                 # 12 guided walkthroughs
├── examples/                  # 7 architecture scaffolds
├── case-studies/              # 3 delivery scenarios
├── agents/                    # 6 reviewer personas
├── mcp/                       # 8 MCP template configs
├── templates/                 # 3 YAML templates (specs, contracts)
├── docs/                      # 11 setup and anatomy guides
├── hooks/                     # Session start, release guard
├── scripts/                   # Install scripts (sh + ps1)
├── registry/assets.json       # Machine-readable index
├── skills-index.md            # Human-readable catalog
├── .cursor/commands/          # Cursor adapter
├── .claude/commands/          # Claude adapter
├── .gemini/commands/          # Gemini adapter
├── .kiro/steering/            # Kiro adapter
├── .opencode/                 # OpenCode adapter
├── .github/copilot-instructions.md  # Copilot adapter
├── AGENTS.md                  # Generic agent adapter
├── CLAUDE.md                  # Claude project doc
└── vscode-extension/          # VS Code extension source
```

## Operational Hooks

| Hook | Purpose |
|------|---------|
| `session-start` | Detects repo type, recommends preset + starter pack |
| `release-guard` | Validates observability, rollback, reconciliation evidence |
| `review-gate` | Checks tests, contracts, quality gates before merge |

## Bootstrap & Validation

```bash
# Quick setup
./bootstrap.sh                        # or bootstrap.ps1 on Windows

# Validate skill structure
python scripts/validate-skills.py
python scripts/validate-assets.py

# Refresh registry and index
python scripts/sync-registry.py
python scripts/sync-skills-index.py
```

## MCP Templates

Pre-configured Model Context Protocol server configurations:

- `github.json` — GitHub API integration
- `aws.json` — AWS service integration
- `azure.json` — Azure service integration
- `gcp.json` — GCP service integration

## Documentation

| Doc | Purpose |
|-----|---------|
| [Getting Started](docs/getting-started.md) | First-time setup |
| [Skill Anatomy](docs/skill-anatomy.md) | How skills are structured |
| [Routing & Lifecycle](docs/routing-and-lifecycle.md) | Command routing internals |
| [Cursor Setup](docs/cursor-setup.md) | Cursor-specific configuration |
| [Claude Setup](docs/claude-setup.md) | Claude-specific configuration |
| [Codex Setup](docs/codex-setup.md) | Codex-specific configuration |
| [Plugin Publishing](docs/plugin-publishing.md) | How to publish IDE plugins |

## Contributing

Contributions should be specific, verifiable, and workflow-focused.

- Read [`docs/skill-anatomy.md`](docs/skill-anatomy.md) for required structure
- Each skill needs YAML frontmatter, decision frameworks, evidence gates, and exit criteria
- Run `python scripts/validate-skills.py` before submitting

## Links

- **Website:** https://vaquarkhan.github.io/Fullstack-development-agent-skills/
- **GitHub:** https://github.com/vaquarkhan/Fullstack-development-agent-skills
- **VS Code:** https://marketplace.visualstudio.com/items?itemName=ViquarKhan.fullstack-development-agent-skills
- **JetBrains:** https://plugins.jetbrains.com/plugin/32167-fullstack-development-agent-skills

## License

MIT
