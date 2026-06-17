#!/usr/bin/env python3
"""Shared skill discovery for core skills/ and segregated skill-packs/."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
PACKS_DIR = ROOT / "skill-packs"


def discover_skill_files() -> list[Path]:
    files: list[Path] = []
    if SKILLS_DIR.exists():
        files.extend(SKILLS_DIR.glob("*/SKILL.md"))
    if PACKS_DIR.exists():
        files.extend(PACKS_DIR.rglob("SKILL.md"))
    return sorted(set(files))


def skill_name_from_path(path: Path) -> str:
    return path.parent.name


def rel_skill_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()
