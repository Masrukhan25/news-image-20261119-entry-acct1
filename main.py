#!/usr/bin/env python3
"""Copy the bundled entry.png to the output directory.

The image is the entry itself (drawn by compose.py in the build session);
this program only places it where the harness expects it.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Confirm the copied file really is a PNG before reporting success.
    with open(dst, "rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            raise RuntimeError("entry.png is not a valid PNG")
    if os.path.getsize(dst) == 0:
        raise RuntimeError("entry.png was copied empty")
    print(f"copied {src} -> {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
