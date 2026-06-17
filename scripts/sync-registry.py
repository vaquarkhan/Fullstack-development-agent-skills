#!/usr/bin/env python3
"""Regenerate registry/assets.json from repository filesystem."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry" / "assets.json"
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from skill_discovery import discover_skill_files, rel_skill_path  # noqa: E402


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def collect() -> dict:
    skills = sorted(rel_skill_path(p) for p in discover_skill_files())
    skill_packs = sorted(
        rel_skill_path(p) for p in discover_skill_files() if "/skill-packs/" in rel_skill_path(p).replace("\\", "/")
    )
    presets = sorted(rel(p) for p in (ROOT / "presets").glob("*/SKILL.md"))
    starter_packs = sorted(rel(p) for p in (ROOT / "starter-packs").glob("*.yaml"))
    commands = sorted(rel(p) for p in (ROOT / ".cursor" / "commands").glob("*.md"))
    claude_commands = sorted(rel(p) for p in (ROOT / ".claude" / "commands").glob("*.md"))

    adapters = [
        "AGENTS.md",
        "CLAUDE.md",
        ".gemini/commands/README.md",
        ".kiro/steering/README.md",
        ".opencode/README.md",
        ".windsurfrules.example",
        ".github/copilot-instructions.md",
    ]
    adapters.extend(claude_commands)

    scripts = sorted(
        rel(p)
        for p in (ROOT / "scripts").glob("*")
        if p.is_file() and p.suffix in {".py", ".sh", ".ps1"} and not p.name.startswith("_")
    )
    if (ROOT / "bootstrap.sh").exists():
        scripts.append("bootstrap.sh")
    if (ROOT / "bootstrap.ps1").exists():
        scripts.append("bootstrap.ps1")
    scripts = sorted(set(scripts))

    tutorials = sorted(rel(p) for p in (ROOT / "tutorials").glob("*.md"))
    examples = sorted(rel(p) for p in (ROOT / "examples").rglob("README.md"))
    case_studies = sorted(rel(p) for p in (ROOT / "case-studies").glob("*.md"))
    docs = sorted(rel(p) for p in (ROOT / "docs").glob("*.md"))
    hooks = sorted(rel(p) for p in (ROOT / "hooks").glob("*") if p.is_file())
    mcp = sorted(rel(p) for p in (ROOT / "mcp").rglob("*") if p.is_file())
    agents = sorted(rel(p) for p in (ROOT / "agents").glob("*.md"))
    references = sorted(rel(p) for p in (ROOT / "references").glob("*.md"))

    vscode_ext = []
    ext_dir = ROOT / "vscode-extension"
    if ext_dir.exists():
        for name in ("package.json", "tsconfig.json", "src/extension.ts"):
            p = ext_dir / name
            if p.exists():
                vscode_ext.append(rel(p))

    plugins = []
    for p in (ROOT / ".claude-plugin").glob("*"):
        if p.is_file():
            plugins.append(rel(p))
    if (ROOT / "jetbrains-plugin" / "README.md").exists():
        plugins.append("jetbrains-plugin/README.md")

    evals = []
    eval_dir = ROOT / "evals"
    if eval_dir.exists():
        evals = sorted(rel(p) for p in eval_dir.rglob("*") if p.is_file())

    return {
        "version": "0.4.0",
        "description": "Machine-readable index for fullstack agent skill assets.",
        "entry": {"skill": "skills/using-fullstack-agent-skills/SKILL.md"},
        "counts": {
            "skills": len(skills),
            "coreSkills": len(skills) - len(skill_packs),
            "skillPacks": len(skill_packs),
            "presets": len(presets),
            "starterPacks": len(starter_packs),
            "commands": len(commands),
            "agents": len(agents),
        },
        "skills": skills,
        "skillPacks": skill_packs,
        "presets": presets,
        "starterPacks": starter_packs,
        "commands": commands,
        "agents": agents,
        "references": references,
        "adapters": adapters,
        "scripts": scripts,
        "tutorials": tutorials,
        "examples": examples,
        "caseStudies": case_studies,
        "docs": docs,
        "hooks": hooks,
        "mcp": mcp,
        "vscodeExtension": vscode_ext,
        "plugins": plugins,
        "evals": evals,
    }


def main() -> None:
    data = collect()
    REGISTRY.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {REGISTRY.relative_to(ROOT)} "
        f"v{data['version']}: {data['counts']['skills']} skills, "
        f"{data['counts']['presets']} presets, "
        f"{data['counts']['starterPacks']} starter packs"
    )


if __name__ == "__main__":
    main()
