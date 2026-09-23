#!/bin/bash
set -e
git clone https://github.com/DenisVargaeu/allcalc.git
cd allcalc
python -m pip install -r requirements.txt
python -m build
python -m pip install .