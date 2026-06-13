#!/usr/bin/env python3
"""Require provenance footers on reference checklists."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCES_DIR = ROOT / "references"

REQUIRED_MARKERS = (
    "## Provenance",
    "- Sources:",
    "- Last reviewed:",
)


def main() -> int:
    if not REFERENCES_DIR.exists():
        print("references/ not found", file=sys.stderr)
        return 1

    failed = 0
    for path in sorted(REFERENCES_DIR.glob("*-checklist.md")):
        text = path.read_text(encoding="utf-8")
        missing = [marker for marker in REQUIRED_MARKERS if marker not in text]
        if missing:
            failed += 1
            print(f"FAIL {path.relative_to(ROOT)}")
            for marker in missing:
                print(f"  - missing: {marker}")

    if failed:
        print(f"\n{failed} checklist(s) missing provenance")
        return 1

    print(f"OK: {len(list(REFERENCES_DIR.glob('*-checklist.md')))} checklists have provenance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
