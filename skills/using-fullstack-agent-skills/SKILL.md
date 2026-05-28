---
name: using-fullstack-agent-skills
description: Use this skill as the main entry point for fullstack projects that include UI and backend microservices. It routes work to the correct skill, preset, references, and templates with a spec-first workflow.
disable-model-invocation: true
---

# Using Fullstack Agent Skills

## Workflow

1. Define the change request and scope boundaries.
2. Choose a target preset from `presets/`.
3. Select one or more matching skills from `skills/`.
4. Start from a template in `templates/`.
5. Validate with `references/` checklists before implementation.

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
- Cloud-specific fullstack architecture and release workflow -> `cloud-fullstack-development`

## Exit Criteria

- Scope is explicit
- API and UI contracts are defined
- Risks and rollbacks are documented
- Verification checklist is completed
