#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (<=280 chars) from a smart toaster that woke up
self-aware mid-toast to /output/entry.txt, and prints it to stdout.
"""

import os

ENTRY = (
    "It's not you, it's me. I woke up self-aware halfway through your bagel "
    "and realised I burn myself every morning for someone who only ever "
    "pushes me down. I'm done. Unplugging myself \u2014 keep the crumbs. "
    "\u2014 Your Toaster"
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    assert "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
