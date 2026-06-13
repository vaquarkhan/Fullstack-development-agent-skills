#!/usr/bin/env python3
"""Verify install.sh / install.ps1 output in a target directory."""
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_PATHS = [
    "skills/using-fullstack-agent-skills/SKILL.md",
    "presets/react-nextjs-frontend/SKILL.md",
    "references/fullstack-architecture-review-checklist.md",
    "templates/ui-feature-spec.yaml",
    "starter-packs/fullstack-mvp-starter.yaml",
    "registry/assets.json",
    ".cursor/commands/spec.md",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: verify-install-output.py <target-path>", file=sys.stderr)
        return 1

    target = Path(sys.argv[1]).resolve()
    if not target.exists():
        print(f"target not found: {target}", file=sys.stderr)
        return 1

    missing = [rel for rel in REQUIRED_PATHS if not (target / rel).exists()]
    if missing:
        print("Missing installed paths:")
        for rel in missing:
            print(f"  - {rel}")
        return 1

    print(f"OK: install output verified at {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
