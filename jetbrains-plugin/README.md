# JetBrains Plugin (Scaffold)

This directory documents how to consume Fullstack Development Agent Skills in JetBrains IDEs (IntelliJ IDEA, WebStorm, Rider).

## Recommended Setup

1. Clone or install this repository into your project or global skills path.
2. Point your AI assistant integration (GitHub Copilot, Junie, or third-party agents) at `AGENTS.md` and `skills-index.md`.
3. Pin `skills/using-fullstack-agent-skills/SKILL.md` as the entry skill for new sessions.

## Lifecycle Commands

Map IDE slash commands or run configurations to the markdown files in `.cursor/commands/` (spec, plan, build, validate, review, ship, migrate, harden, incident, optimize).

## Presets and Starter Packs

- Choose a stack preset under `presets/`.
- Load a starter pack YAML from `starter-packs/` for guided skill bundles.

See `docs/jetbrains-setup.md` for detailed steps.
