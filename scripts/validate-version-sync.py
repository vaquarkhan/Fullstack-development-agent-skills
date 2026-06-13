#!/usr/bin/env python3
"""Check version consistency across registry and plugin manifests."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry" / "assets.json"
CLAUDE_PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
CHANGELOG = ROOT / "CHANGELOG.md"
VSCODE_PACKAGE = ROOT / "vscode-extension" / "package.json"
JETBRAINS_BUILD = ROOT / "jetbrains-plugin" / "build.gradle.kts"


def read_registry_version() -> str:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    version = data.get("version")
    if not version:
        raise ValueError("registry/assets.json missing version")
    return str(version)


def read_claude_plugin_version() -> str:
    data = json.loads(CLAUDE_PLUGIN.read_text(encoding="utf-8"))
    version = data.get("version")
    if not version:
        raise ValueError(".claude-plugin/plugin.json missing version")
    return str(version)


def read_changelog_top_version() -> str | None:
    if not CHANGELOG.exists():
        return None
    match = re.search(r"^## ([0-9]+\.[0-9]+\.[0-9]+)\s*$", CHANGELOG.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1) if match else None


def read_vscode_version() -> str | None:
    if not VSCODE_PACKAGE.exists():
        return None
    return str(json.loads(VSCODE_PACKAGE.read_text(encoding="utf-8")).get("version", ""))


def read_jetbrains_version() -> str | None:
    if not JETBRAINS_BUILD.exists():
        return None
    match = re.search(r'^version\s*=\s*"([^"]+)"', JETBRAINS_BUILD.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1) if match else None


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not REGISTRY.exists():
        print("registry/assets.json not found", file=sys.stderr)
        return 1

    registry_version = read_registry_version()

    if CLAUDE_PLUGIN.exists():
        claude_version = read_claude_plugin_version()
        if claude_version != registry_version:
            errors.append(
                f".claude-plugin/plugin.json version {claude_version} != registry {registry_version}"
            )
    else:
        warnings.append(".claude-plugin/plugin.json not found")

    changelog_version = read_changelog_top_version()
    if changelog_version and changelog_version != registry_version:
        errors.append(
            f"CHANGELOG top version {changelog_version} != registry {registry_version}"
        )

    vscode_version = read_vscode_version()
    if vscode_version and vscode_version != registry_version:
        warnings.append(
            f"vscode-extension/package.json version {vscode_version} differs from registry {registry_version}"
        )

    jetbrains_version = read_jetbrains_version()
    if jetbrains_version and jetbrains_version != registry_version:
        warnings.append(
            f"jetbrains-plugin/build.gradle.kts version {jetbrains_version} differs from registry {registry_version}"
        )

    for warning in warnings:
        print(f"WARN: {warning}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: registry version {registry_version} is consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
