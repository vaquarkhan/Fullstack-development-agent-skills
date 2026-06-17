# Claude Setup

## Install

```bash
scripts/install.sh claude /path/to/project
```

## What Gets Installed

- `.claude/commands/` — lifecycle commands
- `CLAUDE.md` — project entry point
- `skills/` (72 core) and `skill-packs/` (34 stack packs)
- Presets, references, templates, starter packs

## Recommended Entry

1. `CLAUDE.md`
2. `skills/using-fullstack-agent-skills/SKILL.md`
3. `docs/fullstack-skills-catalog.md` for stack-specific routing

For Java/Spring Boot work, load packs from `skill-packs/java/spring-boot/`.
