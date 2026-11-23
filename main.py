#!/usr/bin/env python3
"""Entry for make.fun "The One-Line Laugh".

Writes a single funny line (one sentence, 119 characters) to
/output/entry.txt. No network, no clock, no randomness: the output is
fully deterministic.
"""

import os
from pathlib import Path

LINE = "I bought a plant to prove I could keep something alive, and now it watches me eat takeout like a disappointed landlord."

OUTPUT_PATH = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
