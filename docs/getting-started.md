# Getting Started

## Install

```bash
git clone https://github.com/vaquarkhan/Fullstack-development-agent-skills.git
```

## First Workflow

1. Open `skills/using-fullstack-agent-skills/SKILL.md`
2. Choose one preset from `presets/`
3. Start from a matching template in `templates/`
4. Validate with checklists in `references/`

## Lifecycle Commands

Use the command docs in `.cursor/commands/` to standardize agent execution:

1. `/spec` capture scope, contracts, and risk assumptions
2. `/plan` split work into safe implementation slices
3. `/build` implement frontend/backend changes with tests
4. `/validate` verify compatibility, quality, and security checks
5. `/review` run multi-persona review lenses
6. `/ship` release with staged rollout and rollback guardrails

## Common Paths

- React or Next.js UI -> `presets/react-nextjs-frontend/SKILL.md`
- Angular UI -> `presets/angular-frontend/SKILL.md`
- Vue or Nuxt UI -> `presets/vue-nuxt-frontend/SKILL.md`
- Node.js services -> `presets/nodejs-microservices/SKILL.md`
- Java Spring services -> `presets/java-spring-boot-microservices/SKILL.md`
- .NET services -> `presets/dotnet-aspnet-core-microservices/SKILL.md`
- AWS fullstack delivery -> `presets/aws-fullstack-development/SKILL.md`
- Azure fullstack delivery -> `presets/azure-fullstack-development/SKILL.md`
- GCP fullstack delivery -> `presets/gcp-fullstack-development/SKILL.md`

## Recommended Progression

1. Define UI or service scope
2. Lock API contract before coding
3. Implement in small verifiable slices
4. Verify reliability and accessibility

## High-Value Add-Ons

- Starter packs in `starter-packs/` for common delivery modes
- Reviewer personas in `agents/` for focused risk detection
- Skill writing standards in `docs/skill-anatomy.md`
- Machine-readable index in `registry/assets.json` for tooling integration
- Install scripts in `scripts/install.sh` and `scripts/install.ps1`
