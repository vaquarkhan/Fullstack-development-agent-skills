# Windsurf Setup

1. Copy `.windsurfrules.example` to `.windsurfrules` in your project root (or merge into existing rules).
2. Install skills with `scripts/install.sh --tool windsurf` or `scripts/install.ps1 -Tool windsurf`.
3. Point workflows at `AGENTS.md` and `skills-index.md`.
4. Use starter packs in `starter-packs/` to bundle skills for common delivery paths.
5. Run `python scripts/validate-skills.py` after customizing skills locally.
