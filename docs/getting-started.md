# Getting Started

## Install

```bash
git clone https://github.com/vaquarkhan/Fullstack-development-agent-skills.git
```

Or install into a project:

```bash
./scripts/install.sh all /path/to/project
# Windows: .\scripts\install.ps1 -Tool all -Target C:\path\to\project
```

## Repository Layout

| Layer | Path | Count | When to use |
| --- | --- | --- | --- |
| Core skills | `skills/` | 72 | Cross-stack workflows (spec, ship, observability, patterns) |
| Skill packs | `skill-packs/` | 45 | Deep stack playbooks (Spring Boot, NestJS, .NET, Rust, etc.) |
| Presets | `presets/` | 15 | Stack-specific defaults |
| Starter packs | `starter-packs/` | 20 | Problem-area bundles |
| Examples | `examples/` | 10 | Architecture blueprints |

See `docs/fullstack-skills-catalog.md` for the complete inventory.

## First Workflow

1. Open `skills/using-fullstack-agent-skills/SKILL.md`
2. Choose one preset from `presets/`
3. Load matching skills from `skills/` or `skill-packs/`
4. Start from a template in `templates/` or examples in `skill-packs/*/examples/`
5. Validate with checklists in `references/`

## Lifecycle Commands

Use command docs in `.cursor/commands/` (or `.claude/commands/`):

1. `/spec` — scope, contracts, and risk assumptions
2. `/plan` — safe implementation slices
3. `/build` — implement with tests
4. `/validate` — quality, security, compatibility
5. `/review` — multi-persona review lenses
6. `/ship` — staged rollout and rollback
7. `/migrate` — schema and platform migrations
8. `/harden` — security and reliability hardening
9. `/incident` — production triage
10. `/optimize` — performance and cost

## Common Paths

### Frontend

- React / Next.js → `presets/react-nextjs-frontend/`
- Angular → `presets/angular-frontend/`
- Vue / Nuxt → `presets/vue-nuxt-frontend/`

### Backend

- Node.js / NestJS → `presets/nodejs-microservices/` + `skills/nodejs-nestjs-backend-microservices/`
- Java Spring Boot → `presets/java-spring-boot-microservices/` + `skill-packs/java/spring-boot/`
- Java Quarkus / Micronaut / Jakarta EE / Vaadin → `skill-packs/java/`
- .NET → `presets/dotnet-aspnet-core-microservices/`
- Python FastAPI / Django → `skill-packs/python/`
- Go Gin → `skill-packs/go/gin/`
- PHP Laravel / Ruby Rails → `skill-packs/php/`, `skill-packs/ruby/`

### Cloud

- AWS → `presets/aws-fullstack-development/` or `presets/aws-serverless-fullstack/`
- Azure → `presets/azure-fullstack-development/` or `presets/azure-serverless-fullstack/`
- GCP → `presets/gcp-fullstack-development/` or `presets/gcp-serverless-fullstack/`
- Kubernetes → `presets/kubernetes-fullstack-platform/`

## Validation

```bash
python scripts/validate-skills.py
python scripts/check-skill-boilerplate.py
python scripts/validate-assets.py
python scripts/validate-version-sync.py
python scripts/run-skill-routing-benchmark.py
```

## High-Value Add-Ons

- `skill-packs/README.md` — segregated Java, Python, Go, PHP, Ruby catalogs
- Starter packs in `starter-packs/`
- Reviewer personas in `agents/`
- Skill writing standards in `docs/skill-anatomy.md`
- Machine-readable index in `registry/assets.json`
- Install scripts: `scripts/install.sh`, `scripts/install.ps1`
