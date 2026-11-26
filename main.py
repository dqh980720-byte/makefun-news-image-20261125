#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261125.

It writes the front page for Wednesday 25 November 2026 to the
grader's output folder. The image is bundled in this repository, so
the program needs no network and no randomness: every run copies the
same bytes to the same place, and two runs give identical output.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "frontpage.png"


def output_path() -> Path:
    """Where the grader expects the finished image."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(folder) / "entry.png"


def bundled_image() -> Path:
    """The front page that ships beside this program."""
    return Path(__file__).resolve().parent / IMAGE_NAME


def run() -> int:
    source = bundled_image()
    target = output_path()
    if not source.is_file():
        print(f"missing bundled image: {source}", file=sys.stderr)
        return 1
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
