"""Build every configured HAwiki locale into one Workers asset bundle."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "dist"


def main() -> None:
    """Clean the generated bundle and run the existing builder once per locale."""
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    sites = json.loads((ROOT / "sites.json").read_text(encoding="utf-8"))
    for site in sites:
        environment = os.environ.copy()
        environment["HAWIKI_SITE"] = site
        subprocess.run(
            [sys.executable, str(ROOT / "tools" / "build.py")],
            cwd=ROOT,
            env=environment,
            check=True,
        )


if __name__ == "__main__":
    main()
