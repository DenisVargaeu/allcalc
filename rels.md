# AllCalc v4.2.8

## What's New

### New Features
- **Percentage Module (`modules/percentage.py`)**: Added option **2 — Unknown percentage** to calculate what percentage a given part is of a whole.
- **Common Divisors Module (`modules/cd.py`)**: Added a new module for finding common divisors and the greatest common divisor (GCD) of two numbers, imported in `app.py`.
- **Linux Install Script (`install.sh`)**: Added a one-line installation script for Linux (`curl -fsSL ... | bash`) along with `requirements.txt` (`rich`, `simpleeval`) and updated `README.md` with installation instructions.

### Tooling & Maintenance
- **Release Manager (`dist.py`)**: Added an automated release script to handle version updates, package builds, Git commits/tags, PyPI uploads, and GitHub Releases.
- **Version Bump**: Updated version to `4.2.8` across `pyproject.toml`, `app.py`, and `README.md`.
- **Gitignore**: Added `update.sh` and `.kdenlive-mcp` to `.gitignore`.

## Installation

### Via pip
```bash
pip install allcalc
```

### Via install script (Linux only)
```bash
curl -fsSL https://raw.githubusercontent.com/DenisVargaeu/allcalc/refs/heads/main/install.sh | bash
```
