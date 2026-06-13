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

MAX_DESCRIPTION_LENGTH = 1024
MIN_SECTION_NONEMPTY_LINES = 2
MIN_SECTION_BODY_CHARS = 40

FRONTMATTER_BLOCK_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
DESCRIPTION_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)
SECTION_HEADING_RE = re.compile(r"^(## .+)$", re.MULTILINE)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_BLOCK_RE.match(text)
    if not match:
        return {}, text

    block = match.group(1)
    body = text[match.end() :]
    fields: dict[str, str] = {}

    name_match = NAME_RE.search(block)
    if name_match:
        fields["name"] = name_match.group(1).strip()

    description_match = DESCRIPTION_RE.search(block)
    if description_match:
        fields["description"] = description_match.group(1).strip()

    return fields, body


def find_duplicate_headings(text: str) -> list[str]:
    counts: dict[str, int] = {}
    for heading in SECTION_HEADING_RE.findall(text):
        counts[heading] = counts.get(heading, 0) + 1
    return [f"duplicate heading ({count}x): {heading}" for heading, count in counts.items() if count > 1]


def check_section_order(text: str) -> list[str]:
    positions: list[tuple[int, str]] = []
    for section in REQUIRED_SECTIONS:
        index = text.find(section)
        if index >= 0:
            positions.append((index, section))

    errors: list[str] = []
    for left, right in zip(positions, positions[1:]):
        if left[0] >= right[0]:
            errors.append(
                f"section order violation: {left[1]} must appear before {right[1]}"
            )
    return errors


def extract_section_bodies(text: str) -> dict[str, str]:
    matches = list(SECTION_HEADING_RE.finditer(text))
    bodies: dict[str, str] = {}

    for index, match in enumerate(matches):
        heading = match.group(1)
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        bodies[heading] = text[start:end]

    return bodies


def check_section_bodies(text: str) -> list[str]:
    bodies = extract_section_bodies(text)
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
        body = bodies.get(section, "")
        stripped = body.strip()
        if section not in bodies:
            continue

        nonempty_lines = [line for line in stripped.splitlines() if line.strip()]
        if len(nonempty_lines) < MIN_SECTION_NONEMPTY_LINES:
            errors.append(
                f"section too short ({len(nonempty_lines)} nonempty lines): {section}"
            )
        elif len(stripped) < MIN_SECTION_BODY_CHARS:
            errors.append(
                f"section body too small ({len(stripped)} chars): {section}"
            )

    return errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    folder_name = path.parent.name
    frontmatter, _body = parse_frontmatter(text)

    if not frontmatter.get("name") or not frontmatter.get("description"):
        errors.append("missing or invalid YAML frontmatter (name, description)")
    else:
        if frontmatter["name"] != folder_name:
            errors.append(
                f"frontmatter name '{frontmatter['name']}' does not match folder '{folder_name}'"
            )

        description = frontmatter["description"]
        if len(description) > MAX_DESCRIPTION_LENGTH:
            errors.append(
                f"description exceeds {MAX_DESCRIPTION_LENGTH} chars ({len(description)})"
            )

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing section: {section}")

    errors.extend(find_duplicate_headings(text))
    errors.extend(check_section_order(text))
    errors.extend(check_section_bodies(text))

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
