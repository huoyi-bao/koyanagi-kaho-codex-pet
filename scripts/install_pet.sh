#!/usr/bin/env bash
set -euo pipefail

pet_id="${1:-}"
if [[ -z "$pet_id" ]]; then
  echo "Usage: $0 <pet-id>"
  exit 2
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src="$repo_root/pets/$pet_id"
dest="${CODEX_HOME:-$HOME/.codex}/pets/$pet_id"

if [[ ! -d "$src" ]]; then
  echo "Unknown pet: $pet_id"
  exit 1
fi

mkdir -p "$(dirname "$dest")"
rm -rf "$dest"
cp -R "$src" "$dest"
echo "Installed $pet_id to $dest"
