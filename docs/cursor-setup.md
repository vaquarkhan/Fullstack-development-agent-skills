# Cursor Setup

## Install

```bash
scripts/install.sh cursor /path/to/project
```

Windows:

```powershell
scripts/install.ps1 -Tool cursor -Target C:\path\to\project
```

## What Gets Installed

- `.cursor/commands/` — 10 lifecycle commands
- `skills/` — 72 core workflow skills
- `skill-packs/` — 34 stack-specific skills (optional; install per stack)
- Presets, starter packs, references, templates

## Recommended First Run

1. Open `skills/using-fullstack-agent-skills/SKILL.md`
2. Run `/spec` then `/plan`
3. Pick one preset from `presets/`
4. For framework work, load skills from `skill-packs/` (e.g. `skill-packs/java/spring-boot/`)
5. Pick one starter pack from `starter-packs/`

See `docs/fullstack-skills-catalog.md` for the complete inventory.
