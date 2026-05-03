# Syncing Codex Pets

This repo contains Codex Desktop custom pet packages:

```text
pets/koyanagi-kaho/
  pet.json
  spritesheet.webp
pets/rana/
  pet.json
  spritesheet.webp
```

Preview and QA assets live under:

```text
previews/koyanagi-kaho/
previews/rana/
```

## On Another Windows Device

Clone the repo:

```powershell
git clone https://github.com/huoyi-bao/koyanagi-kaho-codex-pet.git
cd koyanagi-kaho-codex-pet
```

Install Rana into Codex Desktop:

```powershell
$pet = "rana"
$dest = Join-Path $env:USERPROFILE ".codex\pets\$pet"
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Remove-Item -LiteralPath $dest -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item -LiteralPath ".\pets\$pet" -Destination $dest -Recurse
```

Use `$pet = "koyanagi-kaho"` to install Koyanagi Kaho instead.

Then restart Codex Desktop, or use Force Reload/Refresh in the pet selector.

## Validate

```powershell
python .\scripts\validate_catalog.py
```

Expected result:

```text
catalog ok: 2 pet(s)
```

## Notes

- Koyanagi Kaho is the original aqua-haired chibi schoolgirl pet.
- Rana is the reserved silver-haired guitarist pet generated with Codex's `hatch-pet` skill.
- Rana's running rows intentionally keep the stronger guitar and motion detail even though the outfit drifts darker than the base outfit.
- Rana's review row had one crouching frame replaced with a standing review frame to make the loop less jarring.
- Runtime display scale is not part of the current custom pet manifest, so the packages use the original validated sprite sizes.
