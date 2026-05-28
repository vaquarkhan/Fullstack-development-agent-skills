#!/usr/bin/env bash
set -euo pipefail

TOOL="${1:-all}"
TARGET="${2:-}"

if [[ -z "${TARGET}" ]]; then
  echo "Usage: scripts/install.sh <tool|all> <target-path>"
  exit 1
fi

mkdir -p "${TARGET}"

copy_if_exists() {
  local src="$1"
  local dst="$2"
  if [[ -e "${src}" ]]; then
    mkdir -p "$(dirname "${dst}")"
    cp -R "${src}" "${dst}"
  fi
}

case "${TOOL}" in
  cursor)
    copy_if_exists ".cursor" "${TARGET}/.cursor"
    copy_if_exists "skills" "${TARGET}/skills"
    ;;
  claude|copilot|codex|generic)
    copy_if_exists "skills" "${TARGET}/skills"
    copy_if_exists "presets" "${TARGET}/presets"
    copy_if_exists "references" "${TARGET}/references"
    copy_if_exists "templates" "${TARGET}/templates"
    copy_if_exists "starter-packs" "${TARGET}/starter-packs"
    ;;
  all)
    copy_if_exists ".cursor" "${TARGET}/.cursor"
    copy_if_exists "agents" "${TARGET}/agents"
    copy_if_exists "docs" "${TARGET}/docs"
    copy_if_exists "skills" "${TARGET}/skills"
    copy_if_exists "presets" "${TARGET}/presets"
    copy_if_exists "references" "${TARGET}/references"
    copy_if_exists "templates" "${TARGET}/templates"
    copy_if_exists "starter-packs" "${TARGET}/starter-packs"
    copy_if_exists "registry" "${TARGET}/registry"
    ;;
  *)
    echo "Unsupported tool: ${TOOL}"
    echo "Supported tools: cursor, claude, copilot, codex, generic, all"
    exit 1
    ;;
esac

echo "Installed '${TOOL}' assets into ${TARGET}"
