# Fullstack Skills Catalog

Complete inventory of skills, packs, presets, and planned expansions (v0.4.0).

## Summary

| Asset | Count | Location |
| --- | --- | --- |
| Core skills | 72 | `skills/` |
| Skill packs | 45 | `skill-packs/` |
| **Total skills** | **117** | — |
| Presets | 15 | `presets/` |
| Starter packs | 20 | `starter-packs/` |
| Examples (blueprints) | 10 | `examples/` |
| References | 14 | `references/` |
| Review agents | 6 | `agents/` |
| Lifecycle commands | 10 | `.cursor/commands/` |

Machine-readable index: `registry/assets.json`  
Human index: `skills-index.md`

## Core Skills by Domain (`skills/`)

### Entry and product

- `using-fullstack-agent-skills` — routing hub
- `fullstack-product-specification` — scope and contracts

### Frontend

- `react-nextjs-frontend-architecture`, `nextjs-app-router-and-streaming-ui`
- `angular-enterprise-frontend`, `vue-nuxt-frontend`
- `ui-engineering-and-design-systems`, `design-system-governance-and-tokens`
- `frontend-security-csp-and-xss-hardening`, `web-accessibility-wcag-compliance`
- `realtime-ui-websockets-and-sse`, `graphql-client-and-bff-integration`
- `search-and-discovery-experience`, `internationalization-and-localization`
- `react-native-fullstack-integration`, `mobile-api-and-offline-sync-patterns`

### Backend and APIs

- `nodejs-nestjs-backend-microservices`, `java-spring-boot-microservices`, `dotnet-aspnet-core-microservices`
- `backend-microservices-architecture`, `bff-architecture-and-api-aggregation`
- `api-contract-first-development`, `interservice-protocol-selection-rest-grpc-graphql`
- `domain-driven-service-decomposition`, `monolith-to-microservices-migration-strategy`
- `distributed-monolith-detection-and-remediation`

### Data and persistence

- `postgres-and-relational-data-modeling`, `database-migrations-zero-downtime`
- `redis-caching-and-session-store-patterns`, `distributed-caching-and-invalidation`
- `kafka-event-backbone-patterns`, `cqrs-and-event-sourcing-patterns`
- `multi-tenant-data-isolation-patterns`

### Identity and security

- `authentication-and-authorization-fullstack`, `oauth2-oidc-and-token-lifecycle`
- `okta-identity-integration-patterns`, `aws-cognito-authentication-patterns`
- `secrets-vault-and-key-rotation`, `compliance-gdpr-and-data-privacy-fullstack`

### Microservice patterns

- `microservice-patterns-saga-and-compensation`, `microservice-patterns-outbox-and-cdc`
- `microservice-patterns-service-mesh-and-traffic-management`
- `resilience-timeouts-retries-and-circuit-breakers`

### Edge, CDN, and delivery

- `api-gateway-and-edge-security`, `nginx-edge-routing-and-security`
- `cdn-caching-and-edge-acceleration-patterns`, `frontend-load-balancing-and-global-delivery`
- `load-balancer-strategy-and-traffic-distribution`, `vercel-edge-and-jamstack-delivery`

### Cloud and platform

- `cloud-fullstack-development`, `kubernetes-fullstack-platform-engineering`
- `aws-serverless-fullstack-architecture`, `azure-serverless-fullstack-architecture`, `gcp-serverless-fullstack-architecture`
- `serverless-event-driven-and-workflow-orchestration`, `terraform-fullstack-infrastructure-as-code`
- `multi-cloud-disaster-recovery`, `cloud-cost-optimization`, `autoscaling-capacity-and-cost-guardrails`

### Observability, release, and operations

- `fullstack-observability-and-release-engineering`, `observability-distributed-tracing-and-ebpf-strategy`
- `cicd-gitops-and-progressive-deployment`, `feature-flags-and-progressive-delivery`
- `incident-triage-and-oncall-runbooks`, `chaos-engineering-and-failure-injection`
- `performance-and-load-testing-fullstack`, `fullstack-testing-and-quality-gates`, `e2e-testing-playwright-cypress`

### Product features

- `payments-and-webhook-reliability`, `email-and-notification-delivery`
- `file-storage-and-media-delivery`, `ai-llm-integration-in-fullstack-apps`

## Skill Packs (`skill-packs/`)

### Java (29 skills)

| Pack | Skills | Path |
| --- | --- | --- |
| Spring Boot | 22 | `skill-packs/java/spring-boot/` |
| Quarkus | 2 | `skill-packs/java/quarkus/` |
| Micronaut | 2 | `skill-packs/java/micronaut/` |
| Jakarta EE | 1 | `skill-packs/java/jakarta-ee/` |
| Hibernate | 1 | `skill-packs/java/hibernate/` |
| Vaadin | 1 | `skill-packs/java/vaadin/` |

Spring Boot highlights: `spring-ai-integration`, `mcp-server`, `java-agent-core`, `spring-cloud-gateway-routing`, `spring-webflux-reactive`, `oauth2-resource-server`, `openapi-first`, `testing-pyramid`.

Credits: Spring Boot pack adapts [spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) (MIT).

### Python (2)

- `fastapi-async-backend` — `skill-packs/python/fastapi/`
- `django-enterprise-backend` — `skill-packs/python/django/`

### Go (1)

- `go-gin-rest-microservices` — `skill-packs/go/gin/`

### PHP (1)

- `laravel-api-platform` — `skill-packs/php/laravel/`

### Ruby (1)

- `rails-api-backend` — `skill-packs/ruby/rails/`

### TypeScript (1)

- `nestjs-enterprise-backend` — `skill-packs/typescript/nestjs/`

### .NET (2)

- `aspnetcore-minimal-apis` — `skill-packs/dotnet/aspnetcore/`
- `ef-core-persistence` — `skill-packs/dotnet/efcore/`

### Rust (1)

- `rust-axum-microservices` — `skill-packs/rust/axum/`

### Kotlin (2)

- `kotlin-ktor-apis` — `skill-packs/kotlin/ktor/`
- `kotlin-spring-boot` — `skill-packs/kotlin/spring/`

### Flutter (1)

- `flutter-fullstack-mobile` — `skill-packs/flutter/`

### Data (2)

- `mongodb-document-modeling` — `skill-packs/data/mongodb/`
- `elasticsearch-search-patterns` — `skill-packs/data/elasticsearch/`

### AI SDKs (2)

- `langchain-agent-orchestration` — `skill-packs/ai/langchain/`
- `vercel-ai-sdk-streaming` — `skill-packs/ai/vercel-ai-sdk/`

Each pack skill includes `examples/` (good vs bad) and `templates/`.

## Architecture Blueprints (`examples/`)

| Blueprint | Stack focus |
| --- | --- |
| react-nextjs-nestjs-monorepo | Next.js + NestJS monorepo |
| saas-multi-tenant-bff | Multi-tenant BFF |
| payments-webhook-platform | Billing + webhooks |
| aws-edge-fullstack-delivery | AWS edge delivery |
| aws-lambda-api-cloudfront-spa | Serverless SPA |
| azure-apim-functions-static-web-app | Azure serverless |
| gcp-cloud-run-pubsub-nextjs | GCP event-driven |
| java-spring-boot-ai-agent | Spring Boot + Spring AI + MCP |
| java-quarkus-kubernetes-native | Quarkus on K8s |
| java-vaadin-fullstack-admin | Vaadin + Spring Boot |

These are README-only design packs, not runnable scaffolds.

## Presets (15)

React/Next.js, Angular, Vue/Nuxt, TypeScript monorepo, Node.js, Java Spring Boot, .NET, AWS/Azure/GCP fullstack and serverless, Kubernetes, Vercel/Jamstack.

## Starter Packs (20)

MVP, enterprise modernization, SaaS, payments, reliability, microservices, identity/edge, UI excellence, per-cloud serverless, multi-cloud, data platform, compliance, AI features, mobile, chaos/SRE, GitOps CI/CD.

## Routing Quick Reference

| Task | Start here |
| --- | --- |
| Any new work | `skills/using-fullstack-agent-skills/SKILL.md` |
| Cross-stack delivery | `skills/` |
| Spring Boot implementation | `skill-packs/java/spring-boot/` |
| NestJS / .NET / Rust implementation | `skill-packs/typescript/`, `dotnet/`, `rust/` |
| Python API | `skill-packs/python/` |
| Mobile (Flutter) | `skill-packs/flutter/` |
| Document/search data | `skill-packs/data/` |
| AI SDKs (LangChain, Vercel AI) | `skill-packs/ai/` |
| Stack defaults | `presets/` |
| Problem bundles | `starter-packs/` |

See `docs/routing-and-lifecycle.md` for lifecycle commands and preset selection.

## Future Expansions

Possible next packs (not yet in repo):

| Area | Suggested pack |
| --- | --- |
| Rust | Actix-web alternative patterns |
| Mobile | React Native deep pack |
| Data | DynamoDB, Cassandra patterns |
| AI SDKs | OpenAI Assistants API, Anthropic SDK patterns |
| Backend | NestJS microservices mesh, .NET MAUI |

Contributions welcome — see `CONTRIBUTING.md` and `docs/skill-anatomy.md`.
