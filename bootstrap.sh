#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-.}"
TOOL="${2:-all}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "Installing fullstack agent skills (${TOOL}) into ${TARGET}"
"${SCRIPT_DIR}/install.sh" "${TOOL}" "${TARGET}"
echo "Done. Start with skills/using-fullstack-agent-skills/SKILL.md"
