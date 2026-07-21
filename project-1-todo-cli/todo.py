"""CLI entry point: wires argparse subcommands to the storage and tasks modules."""

import argparse
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argparse parser for this CLI.

    Should define subcommands `add <description>`, `list`, `done <id>`, and
    `remove <id>`, matching the usage shown in PROJECTS.md:
        todo add "Buy milk"
        todo list
        todo done 2
        todo remove 1
    """
    raise NotImplementedError


def main() -> None:
    """Parse CLI args, dispatch to the right storage/tasks functions, and print output.

    This should load tasks from TASKS_FILE, perform whatever action the parsed
    args request (using functions from `tasks.py`), save any changes back via
    `storage.py`, and print appropriate output to the user.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
