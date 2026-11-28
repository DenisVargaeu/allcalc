# AllCalc v4.5.0

## What's New

### New Features
- **Electric Power Calculator (`modules/elect.py`)**: Added option **2 — Electric power calculator** inside the Electricity module to solve for:
  - **Current (`I`)** from voltage and power (`I = P / U`)
  - **Voltage (`U`)** from current and power (`U = P / I`)
  - **Power (`P`)** from current and voltage (`P = I × U`)

### Localization & Polish
- Added translations for the electric power calculator (`el.power.elect`, `power.elect`, `power.is.elect`) across all supported languages:
  - English (`en.json`)
  - Slovak (`sk.json`)
  - German (`de.json`)
  - French (`fr.json`)
- Refined grammar and phrasing for electricity module prompts and outputs across all 4 languages.
- Updated `modules/language/transalte_tags.txt` with the new keys.

### Maintenance
- **Version Bump**: Updated version to `4.5.0`.

## Installation

### Via pip
```bash
pip install allcalc
```

### Via install script (Linux only)
```bash
curl -fsSL https://raw.githubusercontent.com/DenisVargaeu/allcalc/refs/heads/main/install.sh | bash
```
