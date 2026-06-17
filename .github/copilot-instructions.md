# Fullstack Development Agent Skills — Copilot Instructions

This repository is an open skill registry for production-grade fullstack delivery.

## Repository Overview

- **117 skills** — 72 core in `skills/` + 45 stack packs in `skill-packs/`
- **15 presets** — stack-specific defaults in `presets/`
- **20 starter packs** — problem-area bundles in `starter-packs/`
- **10 examples** — architecture blueprints in `examples/`
- **10 lifecycle commands** — `/spec`, `/plan`, `/build`, `/validate`, `/review`, `/ship`, `/migrate`, `/harden`, `/incident`, `/optimize`

## Start Here

1. Read `skills/using-fullstack-agent-skills/SKILL.md`
2. Pick a preset from `presets/` matching the stack
3. For deep framework work, load skills from `skill-packs/`
4. Follow lifecycle commands in `.cursor/commands/` or `.claude/commands/`

## Key Directories

| Path | Purpose |
| --- | --- |
| `skills/` | Cross-stack workflow skills |
| `skill-packs/` | Java, Python, Go, PHP, Ruby framework playbooks |
| `presets/` | Platform defaults |
| `starter-packs/` | Use-case bundles |
| `references/` | Operational checklists |
| `registry/assets.json` | Machine-readable index |
| `docs/fullstack-skills-catalog.md` | Complete inventory |

## Skill Writing

Follow `docs/skill-anatomy.md`. Validate with:

```bash
python scripts/validate-skills.py
python scripts/check-skill-boilerplate.py
```

## Routing

- Cross-stack decisions → `skills/`
- Spring Boot, FastAPI, Gin, etc. → `skill-packs/`
- See `docs/routing-and-lifecycle.md`
