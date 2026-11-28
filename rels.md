# AllCalc v4.6.0

## What's New

### New Features
- **Electric Charge Calculator (`modules/elect.py`)**: Added option **3 — Electric charge calculator** (`ecc`) inside the Electricity module to solve for:
  - **Electric Charge (`Q`)** in coulombs (`Q = I × t`)
  - **Current (`I`)** in amperes (`I = Q / t`)
  - **Time (`t`)** in seconds (`t = Q / I`)

### Localization
- Added full translations for the electric charge calculator (`el.charge.elect`, `charge.elect`, `time.elect`, `charge.is.elect`, `time.is.elect` — **99 keys** total) across all supported languages:
  - English (`en.json`)
  - Slovak (`sk.json`)
  - German (`de.json`)
  - French (`fr.json`)
- Updated `modules/language/transalte_tags.txt` with the new translation keys.

### Maintenance
- **Version Bump**: Updated version to `4.6.0`.

## Installation

### Via pip
```bash
pip install allcalc
```

### Via install script (Linux only)
```bash
curl -fsSL https://raw.githubusercontent.com/DenisVargaeu/allcalc/refs/heads/main/install.sh | bash
```
