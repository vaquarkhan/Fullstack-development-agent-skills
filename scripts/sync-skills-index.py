#!/usr/bin/env python3
"""Regenerate skills-index.md from filesystem."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "skills-index.md"
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from skill_discovery import discover_skill_files, rel_skill_path  # noqa: E402


def lines_for(title: str, paths: list[Path], bullet_prefix: str = "- ") -> list[str]:
    out = [f"## {title}", ""]
    for p in paths:
        rel = rel_skill_path(p)
        out.append(f"{bullet_prefix}`{rel}`")
    out.append("")
    return out


def main() -> None:
    all_skills = discover_skill_files()
    core_skills = [p for p in all_skills if "skill-packs" not in rel_skill_path(p)]
    pack_skills = [p for p in all_skills if "skill-packs" in rel_skill_path(p)]
    presets = sorted((ROOT / "presets").glob("*/SKILL.md"))
    refs = sorted((ROOT / "references").glob("*.md"))
    packs = sorted((ROOT / "starter-packs").glob("*.yaml"))
    tutorials = sorted((ROOT / "tutorials").glob("*.md"))
    agents = sorted((ROOT / "agents").glob("*.md"))

    parts = [
        "# Skills Index",
        "",
        f"**{len(all_skills)}** total skills ({len(core_skills)} core + {len(pack_skills)} packs) · "
        f"**{len(presets)}** presets · **{len(packs)}** starter packs",
        "",
    ]
    parts.extend(lines_for("Entry", [ROOT / "skills/using-fullstack-agent-skills/SKILL.md"]))
    parts.extend(lines_for("Core Skills", core_skills))
    parts.extend(lines_for("Skill Packs (by stack)", pack_skills))
    parts.extend(lines_for("Presets", presets))
    parts.extend(lines_for("References", refs))
    parts.extend(lines_for("Starter Packs", packs))
    parts.extend(lines_for("Review Agents", agents))
    parts.extend(lines_for("Tutorials", tutorials))
    parts.extend(
        [
            "## Lifecycle Commands",
            "",
            "- `.cursor/commands/spec.md`",
            "- `.cursor/commands/plan.md`",
            "- `.cursor/commands/build.md`",
            "- `.cursor/commands/validate.md`",
            "- `.cursor/commands/review.md`",
            "- `.cursor/commands/ship.md`",
            "- `.cursor/commands/migrate.md`",
            "- `.cursor/commands/harden.md`",
            "- `.cursor/commands/incident.md`",
            "- `.cursor/commands/optimize.md`",
            "",
            "See `skill-packs/README.md` for segregated Java, Python, Go, PHP, and Ruby packs.",
            "See `registry/assets.json` for the full machine-readable index.",
            "",
        ]
    )
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUT.name}: {len(all_skills)} skills indexed")


if __name__ == "__main__":
    main()
