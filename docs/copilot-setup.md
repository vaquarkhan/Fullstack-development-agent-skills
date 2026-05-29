# GitHub Copilot Setup

1. Install skills into your repo or user profile using `scripts/install.ps1 -Tool copilot` or `scripts/install.sh --tool copilot`.
2. Ensure `.github/copilot-instructions.md` is present at the repository root.
3. Reference `AGENTS.md` and `skills-index.md` in Copilot Chat for routing.
4. Use lifecycle commands from `.cursor/commands/` as prompt templates (spec, plan, build, validate, review, ship, migrate, harden, incident, optimize).
5. Pick a preset from `presets/` and a starter pack from `starter-packs/` before starting feature work.
