#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    errors: list[str] = []

    for pet in catalog.get("pets", []):
        pet_id = pet["id"]
        manifest_path = ROOT / pet["manifestPath"]
        spritesheet_path = ROOT / pet["spritesheetPath"]
        contact_sheet_path = ROOT / pet["preview"]["contactSheet"]

        for path in [manifest_path, spritesheet_path, contact_sheet_path]:
            if not path.is_file():
                errors.append(f"{pet_id}: missing {path.relative_to(ROOT)}")

        if manifest_path.is_file():
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if manifest.get("id") != pet_id:
                errors.append(f"{pet_id}: manifest id mismatch")
            if manifest.get("spritesheetPath") != "spritesheet.webp":
                errors.append(f"{pet_id}: manifest spritesheetPath should be spritesheet.webp")

        expected_sha = pet.get("sha256", {}).get("spritesheet")
        if expected_sha and spritesheet_path.is_file():
            actual_sha = sha256(spritesheet_path)
            if actual_sha != expected_sha:
                errors.append(f"{pet_id}: spritesheet sha256 mismatch")

        preview = pet.get("preview", {})
        for preview_kind in ["gifs", "videos"]:
            for preview_path in preview.get(preview_kind, []):
                path = ROOT / preview_path
                if not path.is_file():
                    errors.append(f"{pet_id}: missing {path.relative_to(ROOT)}")

    if errors:
        print("\n".join(errors))
        raise SystemExit(1)

    print(f"catalog ok: {len(catalog.get('pets', []))} pet(s)")


if __name__ == "__main__":
    main()
