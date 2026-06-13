---
name: using-fullstack-agent-skills
description: Use this skill as the main entry point for fullstack projects that include UI and backend microservices. It routes work to the correct skill, preset, references, and templates with a spec-first workflow.
disable-model-invocation: true
---

# Using Fullstack Agent Skills

## Use When

- Starting any fullstack task that spans UI and backend
- You need routing to the correct skill, preset, reference, or template

## Workflow

1. Define the change request and scope boundaries.
2. Choose a target preset from `presets/`.
3. Select one or more matching skills from `skills/`.
4. Start from a template in `templates/`.
5. Validate with `references/` checklists before implementation.

## Required Checks

- Scope and preset selected before implementation
- Matching skills and references identified for the change type
- Validation checklists from `references/` planned before ship

## Routing Guide

- Fullstack requirement definition and cross-layer scope control -> `fullstack-product-specification`
- UI feature, UX consistency, and component hygiene -> `ui-engineering-and-design-systems`
- React and Next.js architecture and performance -> `react-nextjs-frontend-architecture`
- Angular UI architecture and delivery -> `angular-enterprise-frontend`
- Vue or Nuxt UI delivery -> `vue-nuxt-frontend`
- Service boundaries, resiliency, and deployment-safe backend changes -> `backend-microservices-architecture`
- Node.js or NestJS backend service implementation -> `nodejs-nestjs-backend-microservices`
- Java Spring backend services -> `java-spring-boot-microservices`
- .NET ASP.NET Core backend services -> `dotnet-aspnet-core-microservices`
- API shape and backward compatibility -> `api-contract-first-development`
- Auth and access control across UI and backend -> `authentication-and-authorization-fullstack`
- Fullstack quality gates and release test strategy -> `fullstack-testing-and-quality-gates`
- Runtime visibility, rollout safety, and rollback discipline -> `fullstack-observability-and-release-engineering`
- Progressive rollout control and kill-switch operations -> `feature-flags-and-progressive-delivery`
- Zero-downtime schema and data migration planning -> `database-migrations-zero-downtime`
- Distributed cache correctness and invalidation strategy -> `distributed-caching-and-invalidation`
- Backend-for-frontend contract and aggregation design -> `bff-architecture-and-api-aggregation`
- Payment flow correctness and webhook resilience -> `payments-and-webhook-reliability`
- Production incident response and runbook execution -> `incident-triage-and-oncall-runbooks`
- Distributed transaction coordination and compensation workflows -> `microservice-patterns-saga-and-compensation`
- Reliable event publishing with outbox and CDC -> `microservice-patterns-outbox-and-cdc`
- Mesh-based traffic policy and mTLS controls -> `microservice-patterns-service-mesh-and-traffic-management`
- Circuit-breaker and dependency failure containment -> `resilience-timeouts-retries-and-circuit-breakers`
- Domain-driven decomposition and bounded context design -> `domain-driven-service-decomposition`
- Distributed monolith detection and remediation -> `distributed-monolith-detection-and-remediation`
- CQRS and event-sourcing strategy -> `cqrs-and-event-sourcing-patterns`
- Interservice protocol governance (REST, gRPC, GraphQL) -> `interservice-protocol-selection-rest-grpc-graphql`
- Deep telemetry strategy with distributed tracing and eBPF -> `observability-distributed-tracing-and-ebpf-strategy`
- Phased monolith-to-microservices migration planning -> `monolith-to-microservices-migration-strategy`
- OAuth2/OIDC standards-based authentication and token lifecycle -> `oauth2-oidc-and-token-lifecycle`
- Okta workforce and B2B identity integration patterns -> `okta-identity-integration-patterns`
- AWS Cognito authentication and federation design -> `aws-cognito-authentication-patterns`
- NGINX reverse proxy edge routing and security controls -> `nginx-edge-routing-and-security`
- L4/L7 load balancer routing and failover strategy -> `load-balancer-strategy-and-traffic-distribution`
- CDN cache, acceleration, and edge failover architecture -> `cdn-caching-and-edge-acceleration-patterns`
- Edge gateway security and abuse protection -> `api-gateway-and-edge-security`
- Global frontend load balancing and CDN failover design -> `frontend-load-balancing-and-global-delivery`
- Autoscaling policy and cost guardrail engineering -> `autoscaling-capacity-and-cost-guardrails`
- Cloud-specific fullstack architecture and release workflow -> `cloud-fullstack-development`

## Decision Framework

- Route to the narrowest skill that matches the change type before expanding scope.
- If UI and backend both change, start with fullstack-product-specification before implementation skills.
- Prefer one preset plus one starter pack to reduce conflicting guidance.
- Block /build until scope, contracts, and rollback expectations are documented.

## Common Rationalizations And Rebuttals

- "Any skill is close enough." -> Wrong skill loads wrong gates; match routing guide entries first.
- "We can skip the preset." -> Presets encode stack defaults that prevent rework.
- "References are optional." -> Checklists catch gaps that skills assume are already handled.

## Evidence Pack

- Selected preset and skills list with rationale
- Reference checklists identified for the change type
- Scope boundary note (in/out of scope)
- Lifecycle command chosen (/spec, /plan, etc.) with owner

## Exit Criteria

- Scope is explicit
- API and UI contracts are defined
- Risks and rollbacks are documented
- Verification checklist is completed
