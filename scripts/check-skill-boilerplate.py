#!/usr/bin/env python3
"""Flag skills that still use shared generic boilerplate blocks."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from skill_discovery import discover_skill_files  # noqa: E402

GENERIC_DECISION_MARKERS = (
    "Start with clear scope and ownership boundaries.",
    "Prefer incremental, testable slices over broad rewrites.",
)

GENERIC_RATIONALIZATION_MARKER = '"We can fill gaps after merge."'

GENERIC_EVIDENCE_MARKERS = (
    "Scope and acceptance criteria with owner",
    "Operational visibility requirements for production impact",
)


def uses_generic_boilerplate(text: str) -> bool:
    has_decision = all(marker in text for marker in GENERIC_DECISION_MARKERS)
    has_rationalization = GENERIC_RATIONALIZATION_MARKER in text
    has_evidence = all(marker in text for marker in GENERIC_EVIDENCE_MARKERS)
    return has_decision and has_rationalization and has_evidence


def main() -> int:
    if not (ROOT / "skills").exists() and not (ROOT / "skill-packs").exists():
        print("skills/ and skill-packs/ not found", file=sys.stderr)
        return 1

    flagged: list[str] = []
    for skill_path in discover_skill_files():
        text = skill_path.read_text(encoding="utf-8")
        if uses_generic_boilerplate(text):
            flagged.append(str(skill_path.relative_to(ROOT)))

    if flagged:
        print("Skills using generic boilerplate:")
        for path in flagged:
            print(f"  - {path}")
        print(f"\n{len(flagged)} skill(s) still use shared filler")
        return 1

    print("OK: no skills use generic boilerplate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
