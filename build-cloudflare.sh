#!/bin/sh
set -eu
python3 -m pip install --target .vendor --upgrade -r requirements.txt
python3 tools/build_all.py
python3 -m py_compile tools/*.py
python3 tools/check.py
python3 tools/check_seo.py
node tests/worker-routing.mjs
