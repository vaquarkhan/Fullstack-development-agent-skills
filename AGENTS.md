# Fullstack Agent Skills

Open skill registry for fullstack delivery — **117 skills** (72 core + 45 stack packs), 15 presets, 20 starter packs.

## Start Here

1. Read `skills/using-fullstack-agent-skills/SKILL.md`
2. Select one preset from `presets/` (stack defaults)
3. For deep implementation work, load skills from `skill-packs/` (Java, Python, Go, PHP, Ruby)
4. Follow lifecycle commands in `.cursor/commands/` or `.claude/commands/`
5. Choose a starter pack from `starter-packs/` for problem-area bundles

## Core Lifecycle

- `/spec` define scope and contracts
- `/plan` create safe implementation slices
- `/build` implement frontend and backend changes
- `/validate` prove quality and compatibility
- `/review` run frontend, reliability, and security lenses
- `/ship` release with staged rollout and rollback triggers
- `/migrate` zero-downtime schema and platform migrations
- `/harden` security, reliability, and performance hardening
- `/incident` triage and runbook execution
- `/optimize` performance, cost, and capacity

## Key Directories

| Directory | Purpose |
| --- | --- |
| `skills/` | 72 cross-stack workflow skills (spec, ship, cloud, identity, patterns) |
| `skill-packs/` | 45 stack-specific skills (Spring Boot, NestJS, .NET, Rust, Flutter, AI SDKs, etc.) |
| `presets/` | 15 platform presets (React, Node, Java, AWS, Azure, GCP, K8s) |
| `starter-packs/` | 20 YAML bundles by use case (SaaS, payments, GitOps, chaos) |
| `references/` | 14 operational checklists with provenance footers |
| `examples/` | 10 architecture blueprints (README-only design packs) |
| `agents/` | 6 reviewer personas |
| `registry/assets.json` | Machine-readable index (v0.4.0) |
| `skills-index.md` | Human-readable catalog |
| `docs/fullstack-skills-catalog.md` | Full inventory and roadmap |

## Validation

```bash
python scripts/validate-skills.py
python scripts/check-skill-boilerplate.py
python scripts/validate-assets.py
python scripts/run-skill-routing-benchmark.py
```
