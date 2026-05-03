# Syncing Koyanagi Kaho

This repo contains one Codex Desktop custom pet package:

```text
pets/koyanagi-kaho/
  pet.json
  spritesheet.webp
```

Preview and QA assets live here:

```text
previews/koyanagi-kaho/
  contact-sheet.png
  review.json
  validation.json
  gifs/
  videos/
```

## On Another Windows Device

Clone the repo:

```powershell
git clone https://github.com/huoyi-bao/koyanagi-kaho-codex-pet.git
cd koyanagi-kaho-codex-pet
```

Install into Codex Desktop:

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\pets\koyanagi-kaho"
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Remove-Item -LiteralPath $dest -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item -LiteralPath ".\pets\koyanagi-kaho" -Destination $dest -Recurse
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

## How This Pet Was Created

The pet was generated with Codex's `hatch-pet` skill. The workflow was:

1. Install and reload the `hatch-pet` skill.
2. Use the character reference images and the approved chibi standing base sprite as identity references.
3. Generate a canonical base sprite.
4. Generate the 9 Codex pet animation rows:
   `idle`, `running-right`, `running-left`, `waving`, `jumping`, `failed`, `waiting`, `running`, and `review`.
5. Generate `running-left` separately instead of mirroring `running-right`, because the character has a one-sided yellow hair ribbon.
6. Finalize with the `hatch-pet` scripts to extract frames, compose the 8x9 atlas, validate it, render previews, and package the pet.

Original creation request:

```text
$hatch-pet create a Codex desktop pet based on these character reference images.

Use the chibi standing base sprite as the main identity reference. The pet should be a small pixel-art-adjacent chibi desktop mascot, not polished anime key art.

Character traits:
short pale aqua-silver hair, bright yellow eyes, yellow-and-black side hair ribbon, loose white rolled-sleeve shirt, dark gray plaid pleated skirt, black thigh-high socks, brown loafers, yellow bracelet, cheerful energetic personality.

Important constraints:
keep her grounded, not floating; no checkerboard background; no shadows; no text; no UI props; keep the outfit and face consistent across all animation rows.
```

The local run folder used during creation was:

```text
%USERPROFILE%\.codex\hatch-pet-runs\aqua-ribbon
```

The generated package was originally installed locally as:

```text
%USERPROFILE%\.codex\pets\aqua-ribbon
```

It has since been renamed in this repo to:

```text
id: koyanagi-kaho
displayName: Koyanagi Kaho
```
