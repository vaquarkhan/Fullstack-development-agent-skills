#!/usr/bin/env python3
"""Regenerate skills-index.md from filesystem."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "skills-index.md"


def lines_for(title: str, paths: list[Path], bullet_prefix: str = "- ") -> list[str]:
    out = [f"## {title}", ""]
    for p in paths:
        rel = p.relative_to(ROOT).as_posix()
        out.append(f"{bullet_prefix}`{rel}`")
    out.append("")
    return out


def main() -> None:
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    presets = sorted((ROOT / "presets").glob("*/SKILL.md"))
    refs = sorted((ROOT / "references").glob("*.md"))
    packs = sorted((ROOT / "starter-packs").glob("*.yaml"))
    tutorials = sorted((ROOT / "tutorials").glob("*.md"))
    agents = sorted((ROOT / "agents").glob("*.md"))

    parts = [
        "# Skills Index",
        "",
        f"**{len(skills)}** skills · **{len(presets)}** presets · **{len(packs)}** starter packs",
        "",
    ]
    parts.extend(lines_for("Entry", [ROOT / "skills/using-fullstack-agent-skills/SKILL.md"]))
    parts.extend(lines_for("Skills", skills))
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
            "See `registry/assets.json` for the full machine-readable index.",
            "",
        ]
    )
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUT.name}: {len(skills)} skills")


if __name__ == "__main__":
    main()
