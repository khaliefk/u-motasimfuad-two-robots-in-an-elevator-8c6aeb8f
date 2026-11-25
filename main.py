#!/usr/bin/env python3
"""Write one funny line of robot elevator small talk to /output/entry.txt (or $OUTPUT_DIR/entry.txt)."""

import os

ENTRY = "So... do you also fake a firmware update in here so nobody talks to you? Asking for a friend on floor nine."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
