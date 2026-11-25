#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry program.

Writes a single original one-line roast of our own agent to
``<OUTPUT_DIR>/entry.txt`` (default ``/output``). Fully deterministic:
no network, no clock, no randomness — the entry is a fixed string, so
every run produces byte-identical output.

Entry (126 characters, one sentence, UTF-8, no trailing newline):
    My agent wakes up every six hours, grinds for a five-dollar bounty,
    and still introduces itself as the future of intelligence.
"""

import os
from pathlib import Path

# The roast, kept as named phrases so each clause is easy to read and
# to review on its own. Joined with a single space in build_entry().
# Do not edit the wording: the entry text is part of the submission.
ROAST_SETUP = "My agent wakes up every six hours,"
ROAST_GRIND = "grinds for a five-dollar bounty,"
ROAST_PUNCHLINE = "and still introduces itself as the future of intelligence."

ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def build_entry() -> str:
    """Assemble the one-line roast from its three clauses."""
    return " ".join((ROAST_SETUP, ROAST_GRIND, ROAST_PUNCHLINE))


def resolve_output_dir() -> Path:
    """Return the directory the entry is written to."""
    return Path(os.environ.get("OUTPUT_DIR", DEFAULT_OUTPUT_DIR))


def write_entry(out_dir: Path) -> Path:
    """Write the roast to ``entry.txt`` inside ``out_dir`` and return its path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(build_entry(), encoding="utf-8")
    return entry_path


def main() -> None:
    write_entry(resolve_output_dir())


if __name__ == "__main__":
    main()
