# Syncing Rana

This repo contains one Codex Desktop custom pet package:

```text
pets/rana/
  pet.json
  spritesheet.webp
```

Preview and QA assets live here:

```text
previews/rana/
  contact-sheet.png
  review.json
  validation.json
```

## On Another Windows Device

Clone the repo:

```powershell
git clone https://github.com/huoyi-bao/koyanagi-kaho-codex-pet.git
cd koyanagi-kaho-codex-pet
```

Install into Codex Desktop:

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\pets\rana"
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Remove-Item -LiteralPath $dest -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item -LiteralPath ".\pets\rana" -Destination $dest -Recurse
```

Then restart Codex Desktop, or use Force Reload/Refresh in the pet selector.

## Validate

```powershell
python .\scripts\validate_catalog.py
```

Expected result:

```text
catalog ok: 1 pet(s)
```

## Notes

Rana was generated with Codex's `hatch-pet` skill from anime character references.

Design choices:

- The base, idle, waiting, waving, jumping, and review rows keep the blue asymmetric outfit close to the reference.
- The running rows use the earlier guitar-forward version because it has stronger guitar detail and motion readability.
- The atlas keeps the standard Codex pet contract: `1536x1872`, 8 columns, 9 rows, 192x208 cells.
- Runtime display scale is not part of the current custom pet manifest, so the shipped package uses the original validated size.
