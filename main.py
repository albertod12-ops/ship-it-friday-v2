#!/usr/bin/env python3
"""Ship It Friday entry: one git commit message, written by an AI coding
agent seconds before it breaks production on a Friday."""

import os

os.umask(0o022)

ENTRY = "fix: DNS was down so I pointed prod at 127.0.0.1, it's Friday and localhost is home"

assert "\n" not in ENTRY, "entry must be a single line"
assert 1 <= len(ENTRY.encode("utf-8")) <= 159, "entry must be 1-159 chars"
assert ENTRY.strip(), "entry must not be only whitespace"
# No trailing newline: the file is exactly the commit message, byte for byte.

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
os.chmod("/output/entry.txt", 0o644)
