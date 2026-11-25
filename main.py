#!/usr/bin/env python3
"""Write one funny line of robot elevator small talk to /output/entry.txt (or $OUTPUT_DIR/entry.txt)."""

import os

ENTRY = "So... do you also pretend to install a firmware update in here so nobody talks to you?"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
