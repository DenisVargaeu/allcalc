# AllCalc v4.4.0

## What's New

### New Features
- **Electricity Calculator Module (`modules/elect.py`)**: Added a new electricity calculator accessible from the main menu as option **6**, featuring an **Ohm's Law** calculator to solve for:
  - **Voltage (`U`)** from resistance and current (`U = R × I`)
  - **Resistance (`R`)** from voltage and current (`R = U / I`)
  - **Current (`I`)** from voltage and resistance (`I = U / R`)
- **Main Menu Integration**: Wired option **6** into `app.py` and `modules/printmenu.py` with active-option highlighting.

### Localization
- Added full translations for the electricity module and menu entry (`14` new keys) across all supported languages:
  - English (`en.json`)
  - Slovak (`sk.json`)
  - German (`de.json`)
  - French (`fr.json`)
- Updated `modules/language/transalte_tags.txt` with the new translation keys.

### Maintenance
- **Version Bump**: Updated version to `4.4.0`.

## Installation

### Via pip
```bash
pip install allcalc
```

### Via install script (Linux only)
```bash
curl -fsSL https://raw.githubusercontent.com/DenisVargaeu/allcalc/refs/heads/main/install.sh | bash
```
