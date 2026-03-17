#!/bin/bash
# Generate agents index for agent-directory skill
# Usage: ./scripts/generate-agents-index.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}/.."

echo "Generating agents index..."
python3 scripts/generate-agents-index.py

echo ""
echo "Index generated at:"
echo "  skills/agent-directory/references/agents-index.yaml"
