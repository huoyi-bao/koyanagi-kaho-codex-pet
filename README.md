# Rana Codex Pet

Fan-made animated guitarist pet for the Codex desktop app.

## Preview

![Rana contact sheet](previews/rana/contact-sheet.png)

## Install

Install manually:

```bash
mkdir -p ~/.codex/pets
cp -R pets/rana ~/.codex/pets/
```

On Windows PowerShell:

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\pets\rana"
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Remove-Item -LiteralPath $dest -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item -LiteralPath ".\pets\rana" -Destination $dest -Recurse
```

Then restart Codex Desktop or refresh the pet selector, and choose `Rana`.

## Files

```text
pets/rana/
  pet.json
  spritesheet.webp
previews/rana/
  contact-sheet.png
  review.json
  validation.json
catalog.json
scripts/
```

## Validate

```bash
python scripts/validate_catalog.py
```

Expected result:

```text
catalog ok: 1 pet(s)
```
