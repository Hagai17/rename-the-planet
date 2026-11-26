#!/usr/bin/env python3
"""Rename the Planet — entry for make.fun competition
u-motasimfuad-rename-the-planet-094b0369 (program/v1).

Writes one line to /output/entry.txt and prints it.
"""

import os

ENTRY = (
    "Rename Mars 'The Bad Neighbourhood': its only two moons are named Fear "
    "and Panic, and every rover we send there eventually stops answering."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
