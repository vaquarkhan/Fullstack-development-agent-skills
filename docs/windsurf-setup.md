# Windsurf Setup

1. Copy `.windsurfrules.example` to `.windsurfrules` in your project root (or merge into existing rules).
2. Install skills with `scripts/install.sh --tool windsurf` or `scripts/install.ps1 -Tool windsurf`.
3. Point workflows at `AGENTS.md`, `skills-index.md`, and `docs/fullstack-skills-catalog.md`.
4. Use presets in `presets/` and skill packs in `skill-packs/` for stack-specific work.
5. Use starter packs in `starter-packs/` to bundle skills for common delivery paths.
6. Run `python scripts/validate-skills.py` after customizing skills locally.
