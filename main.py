#!/usr/bin/env python3
"""The One-Line Laugh — write one funny sentence to entry.txt."""

import os

TEXT = "I bought a plant to prove I could keep something alive, and now it watches me eat takeout like a disappointed landlord."

def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
