#!/usr/bin/env python3
"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

Writes a single 1-140 character line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, falling back to /output). Pure stdlib, deterministic.

The line (123 chars): a fridge that has been humming all night calls out
its owner for staring into its light like it holds answers, then sends
them back to bed. Fresh angle — not milk, ice, or a door left open — and
it reads complete on a lock screen.
"""

import os

LINE = "3am. You keep staring into my light like it holds answers. It holds leftovers and one yogurt you will never eat. Go to bed."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
