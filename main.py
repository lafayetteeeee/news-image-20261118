#!/usr/bin/env python3
"""Entry for make.fun bounty "Sum up 18 November's world news in one image".

The grader runs this file as `python3 -P -s /bot/main.py` with no network,
the repository read-only at /bot and an empty writable output directory.
Using only the standard library, it copies the poster stored in the
repository (assets/entry.png) to <output>/entry.png, byte for byte, so two
runs always produce identical bytes.

Output directory resolution, in order:
  1. $MAKEFUN_OUTPUT_DIR (set by the grader)
  2. /output               (the grader's mount, when it exists)
  3. ./output              (local runs)
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    bot_dir = Path(os.environ.get("MAKEFUN_BOT_DIR") or Path(__file__).resolve().parent)
    src = bot_dir / "assets" / "entry.png"
    if not src.is_file():
        # Fall back to the asset beside this file (local checkout layout).
        src = Path(__file__).resolve().parent / "assets" / "entry.png"

    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir_env:
        out_dir = Path(out_dir_env)
    elif Path("/output").is_dir():
        out_dir = Path("/output")
    else:
        out_dir = Path.cwd() / "output"
    out_dir.mkdir(parents=True, exist_ok=True)

    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
