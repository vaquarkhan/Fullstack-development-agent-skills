package com.vaquarkhan.fullstackskills

object SkillsConstants {
    const val REPO_URL = "https://github.com/vaquarkhan/Fullstack-development-agent-skills"
    const val PLUGIN_NAME = "Fullstack Agent Skills"

    val CORE_SKILLS = listOf(
        "skills/using-fullstack-agent-skills",
        "skills/fullstack-product-specification",
        "skills/react-nextjs-frontend-architecture",
        "skills/nodejs-nestjs-backend-microservices",
        "skills/authentication-and-authorization-fullstack",
        "skills/fullstack-testing-and-quality-gates",
        "skills/fullstack-observability-and-release-engineering",
        "skills/feature-flags-and-progressive-delivery",
        "skills/database-migrations-zero-downtime",
        "skills/bff-architecture-and-api-aggregation"
    )

    val ADAPTER_PATHS = listOf(
        ".cursor/commands",
        ".claude/commands",
        ".gemini/commands",
        ".kiro/steering",
        ".opencode",
        "AGENTS.md",
        "CLAUDE.md"
    )

    val MCP_PATHS = listOf("mcp")

    val PRESETS = mapOf(
        "React / Next.js Frontend" to "presets/react-nextjs-frontend",
        "Fullstack TypeScript Monorepo" to "presets/fullstack-typescript-monorepo",
        "Angular Frontend" to "presets/angular-frontend",
        "Vue / Nuxt Frontend" to "presets/vue-nuxt-frontend",
        "Node.js Microservices" to "presets/nodejs-microservices",
        "Java Spring Boot Microservices" to "presets/java-spring-boot-microservices",
        ".NET / ASP.NET Core Microservices" to "presets/dotnet-aspnet-core-microservices",
        "AWS Fullstack Development" to "presets/aws-fullstack-development",
        "Azure Fullstack Development" to "presets/azure-fullstack-development",
        "GCP Fullstack Development" to "presets/gcp-fullstack-development",
        "AWS Serverless Fullstack" to "presets/aws-serverless-fullstack",
        "Azure Serverless Fullstack" to "presets/azure-serverless-fullstack",
        "GCP Serverless Fullstack" to "presets/gcp-serverless-fullstack",
        "Kubernetes Fullstack Platform" to "presets/kubernetes-fullstack-platform",
        "Vercel / Jamstack" to "presets/vercel-nextjs-jamstack"
    )

    val STARTER_PACKS = mapOf(
        "Fullstack MVP Starter" to "starter-packs/fullstack-mvp-starter.yaml",
        "Enterprise Modernization" to "starter-packs/enterprise-modernization-starter.yaml",
        "Platform Reliability" to "starter-packs/platform-reliability-starter.yaml",
        "SaaS Multi-Tenant" to "starter-packs/saas-multi-tenant-starter.yaml",
        "Payments & Subscriptions" to "starter-packs/payments-and-subscriptions-starter.yaml",
        "Incident Hardening & SLO" to "starter-packs/incident-hardening-and-slo-starter.yaml",
        "Microservice Patterns & Edge Security" to "starter-packs/microservice-patterns-and-edge-security-starter.yaml",
        "Microservices Architecture Modernization" to "starter-packs/microservices-architecture-modernization-starter.yaml",
        "Identity, Edge & Global Delivery" to "starter-packs/identity-edge-and-global-delivery-starter.yaml"
    )
}
