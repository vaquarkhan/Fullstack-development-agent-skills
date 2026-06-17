#!/usr/bin/env python3
"""Validate registry/assets.json against repository files."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry" / "assets.json"


def main() -> int:
    if not REGISTRY.exists():
        print("registry/assets.json not found", file=sys.stderr)
        return 1

    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    missing: list[str] = []

    def check_list(key: str) -> None:
        for rel in data.get(key, []):
            path = ROOT / rel.replace("/", "\\") if "\\" in str(ROOT) else ROOT / rel
            if not path.exists():
                missing.append(f"{key}: {rel}")

    for key in [
        "skills",
        "skillPacks",
        "presets",
        "starterPacks",
        "commands",
        "agents",
        "references",
        "adapters",
        "scripts",
        "tutorials",
        "examples",
        "caseStudies",
        "vscodeExtension",
        "docs",
        "hooks",
        "mcp",
        "plugins",
        "evals",
    ]:
        check_list(key)

    entry = data.get("entry", {}).get("skill")
    if entry and not (ROOT / entry).exists():
        missing.append(f"entry: {entry}")

    if missing:
        print("Missing registry paths:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"OK: registry {data.get('version', '?')} validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
