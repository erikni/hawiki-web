#!/bin/sh
set -eu
python3 -m pip install --target .vendor --upgrade -r requirements.txt
python3 tools/build.py
python3 tools/check.py
python3 tools/check_seo.py
