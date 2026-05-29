#!/usr/bin/env python3
"""Validate SKILL.md files under skills/ for required structure."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

REQUIRED_SECTIONS = [
    "## Use When",
    "## Workflow",
    "## Required Checks",
    "## Decision Framework",
    "## Common Rationalizations And Rebuttals",
    "## Evidence Pack",
    "## Exit Criteria",
]

FRONTMATTER_RE = re.compile(
    r"^---\s*\nname:\s*([^\n]+)\n.*?description:\s*([^\n]+)\n.*?---",
    re.DOTALL,
)


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    folder_name = path.parent.name

    if not FRONTMATTER_RE.search(text):
        errors.append("missing or invalid YAML frontmatter (name, description)")

    match = FRONTMATTER_RE.search(text)
    if match:
        name = match.group(1).strip()
        if name != folder_name:
            errors.append(f"frontmatter name '{name}' does not match folder '{folder_name}'")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing section: {section}")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("skills/ directory not found", file=sys.stderr)
        return 1

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print("no skills found", file=sys.stderr)
        return 1

    failed = 0
    for skill_path in skill_files:
        issues = validate_skill(skill_path)
        if issues:
            failed += 1
            print(f"FAIL {skill_path.relative_to(ROOT)}")
            for issue in issues:
                print(f"  - {issue}")

    if failed:
        print(f"\n{failed} skill(s) failed validation")
        return 1

    print(f"OK: {len(skill_files)} skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
