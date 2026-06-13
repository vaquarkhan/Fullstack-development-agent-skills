#!/usr/bin/env python3
"""Static routing regression checks for evals/skill-routing-benchmark.md."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCHMARK = ROOT / "evals" / "skill-routing-benchmark.md"
ROUTING_SKILL = ROOT / "skills" / "using-fullstack-agent-skills" / "SKILL.md"
COMMANDS_DIR = ROOT / ".cursor" / "commands"

TABLE_ROW_RE = re.compile(r"^\|(.+)\|$")
COMMAND_RE = re.compile(r"`(/[a-z]+)`")
SKILL_RE = re.compile(r"`([a-z0-9-]+)`")


def parse_benchmark_rows(text: str) -> list[dict[str, list[str] | str]]:
    rows: list[dict[str, list[str] | str]] = []
    for line in text.splitlines():
        if not line.startswith("|") or "---" in line or "Scenario" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        command_match = COMMAND_RE.search(cells[1])
        if not command_match:
            continue
        command = command_match.group(1).lstrip("/")
        skills = SKILL_RE.findall(cells[2])
        rows.append({"scenario": cells[0], "command": command, "skills": skills})
    return rows


def main() -> int:
    if not BENCHMARK.exists():
        print("evals/skill-routing-benchmark.md not found", file=sys.stderr)
        return 1

    routing_text = ROUTING_SKILL.read_text(encoding="utf-8") if ROUTING_SKILL.exists() else ""
    rows = parse_benchmark_rows(BENCHMARK.read_text(encoding="utf-8"))
    if not rows:
        print("no benchmark scenarios parsed", file=sys.stderr)
        return 1

    failed = 0
    for row in rows:
        scenario = str(row["scenario"])
        command = str(row["command"])
        skills = list(row["skills"])

        command_path = COMMANDS_DIR / f"{command}.md"
        if not command_path.exists():
            failed += 1
            print(f"FAIL {scenario}: missing lifecycle command .cursor/commands/{command}.md")

        for skill in skills:
            skill_path = ROOT / "skills" / skill / "SKILL.md"
            if not skill_path.exists():
                failed += 1
                print(f"FAIL {scenario}: missing skill skills/{skill}/SKILL.md")
            elif skill not in routing_text:
                failed += 1
                print(f"FAIL {scenario}: skill '{skill}' not referenced in using-fullstack-agent-skills routing guide")

    if failed:
        print(f"\n{failed} routing benchmark check(s) failed")
        return 1

    print(f"OK: {len(rows)} routing benchmark scenarios validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
