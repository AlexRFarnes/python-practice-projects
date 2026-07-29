"""CLI entry point: wires argparse to file_organizer.py and executes (or previews) moves."""

import argparse
from pathlib import Path

from file_organizer import plan_moves


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argparse parser for this CLI.

    Should accept:
        - a required positional `source` directory to organize,
        - a required positional `dest` directory to organize into,
        - a `--group-by` flag choosing between "extension" and "date" (default
          "extension"),
        - a `--dry-run` flag that, when set, only prints the planned moves
          instead of performing them (an important habit before mutating files!).
    """
    raise NotImplementedError


def apply_moves(moves: list[tuple[Path, Path]]) -> None:
    """Actually perform the moves (source -> destination), creating any missing
    destination directories first. Look at `shutil.move` and `Path.mkdir`.
    """
    raise NotImplementedError


def main() -> None:
    """Parse CLI args, plan the moves via file_organizer.py, then either print
    them (`--dry-run`) or apply them, printing a summary either way.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
