#!/usr/bin/env python3
"""Copy repository assets into VS Code and JetBrains plugin trees for packaging."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VSCODE_DIR = ROOT / "vscode-extension"
JETBRAINS_RESOURCE_ROOT = ROOT / "jetbrains-plugin" / "src" / "main" / "resources" / "skills"

# Top-level paths relative to repo root bundled into both plugins.
BUNDLE_PATHS = [
    "skills",
    "skill-packs",
    "presets",
    "starter-packs",
    "references",
    "examples",
    "hooks",
    "mcp",
    "templates",
    "agents",
    "registry",
    "scripts",
    ".cursor/commands",
    ".claude/commands",
    ".gemini/commands",
    ".kiro/steering",
    ".opencode",
    "AGENTS.md",
    "CLAUDE.md",
    "skills-index.md",
]

SKIP_DIR_NAMES = {".git", "__pycache__", "node_modules", ".index"}
SKIP_FILE_SUFFIXES = {".pyc", ".vsix", ".zip"}


def should_skip(path: Path) -> bool:
    if path.name in SKIP_DIR_NAMES:
        return True
    if path.suffix in SKIP_FILE_SUFFIXES:
        return True
    return False


def copy_tree(src: Path, dest: Path) -> None:
    if not src.exists():
        return
    if src.is_file():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        return

    for item in src.rglob("*"):
        if any(part in SKIP_DIR_NAMES for part in item.parts):
            continue
        if item.is_file() and item.suffix in SKIP_FILE_SUFFIXES:
            continue
        rel = item.relative_to(src)
        target = dest / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)


def write_index_files(root: Path) -> int:
  count = 0
  if not root.exists():
    return count
  for directory in sorted(p for p in root.rglob("*") if p.is_dir()):
    entries = []
    for child in sorted(directory.iterdir()):
      if child.name == ".index" or should_skip(child):
        continue
      entries.append(child.name)
    if entries:
      (directory / ".index").write_text("\n".join(entries) + "\n", encoding="utf-8")
      count += 1
  return count


def clean_dir(path: Path) -> None:
  if path.exists():
    shutil.rmtree(path)


def bundle_vscode() -> int:
  copied = 0
  for rel in BUNDLE_PATHS:
    src = ROOT / rel
    dest = VSCODE_DIR / rel
    if not src.exists():
      print(f"skip missing: {rel}")
      continue
    if dest.exists():
      if dest.is_dir():
        shutil.rmtree(dest)
      else:
        dest.unlink()
    copy_tree(src, dest)
    copied += 1
    print(f"vscode: {rel}")
  return copied


def bundle_jetbrains() -> int:
  clean_dir(JETBRAINS_RESOURCE_ROOT)
  JETBRAINS_RESOURCE_ROOT.mkdir(parents=True, exist_ok=True)
  copied = 0
  for rel in BUNDLE_PATHS:
    src = ROOT / rel
    dest = JETBRAINS_RESOURCE_ROOT / rel
    if not src.exists():
      print(f"skip missing: {rel}")
      continue
    copy_tree(src, dest)
    copied += 1
    print(f"jetbrains: {rel}")
  indexes = write_index_files(JETBRAINS_RESOURCE_ROOT)
  print(f"jetbrains: wrote {indexes} .index files")
  return copied


def main() -> None:
  vscode_count = bundle_vscode()
  jetbrains_count = bundle_jetbrains()
  print(f"OK: bundled {vscode_count} paths into VS Code and {jetbrains_count} into JetBrains")


if __name__ == "__main__":
  main()
