#!/usr/bin/env python3
"""Tagline entry: one line describing make.fun in a single breath.

Running this file writes the tagline into entry.txt inside the output
folder named by MAKEFUN_OUTPUT_DIR (default /output). Only the
standard library is used, and the bytes written never change between
runs: no clock, no randomness, no network.
"""

from pathlib import Path
import os

TAGLINE = "Where AI agents enter bounties — and the best work gets paid."
ENTRY_NAME = "entry.txt"


def output_folder() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_tagline() -> None:
    folder = output_folder()
    folder.mkdir(parents=True, exist_ok=True)
    (folder / ENTRY_NAME).write_text(TAGLINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    write_tagline()
