# Using Fullstack Agent Skills

## Goal

Adopt the repository as a repeatable delivery system for UI + backend + release work.

## Steps

1. Load `skills/using-fullstack-agent-skills/SKILL.md`.
2. Pick one starter pack from `starter-packs/`.
3. Run lifecycle commands in order: `/spec` -> `/plan` -> `/build` -> `/validate` -> `/review` -> `/ship`.
4. Validate with references and reviewer personas in `agents/`.

## Install

```bash
scripts/install.sh all /path/to/your-project
```

Windows:

```powershell
scripts/install.ps1 -Tool all -Target C:\path\to\your-project
```

## Evidence Before Ship

- Contract compatibility note
- Test evidence for critical journeys
- Rollback trigger and owner documented
