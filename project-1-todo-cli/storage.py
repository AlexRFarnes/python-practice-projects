"""Persistence layer: reading and writing the task list to a JSON file on disk."""

from json import dump, load
from pathlib import Path


def load_tasks(path: Path) -> list[dict]:
    """Read the JSON file at `path` and return its contents as a list of task dicts.

    If the file doesn't exist yet, this should return an empty list rather than
    raising an error (there's simply no tasks saved yet).
    """
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        return load(file)


def save_tasks(path: Path, tasks: list[dict]) -> None:
    """Write `tasks` to the JSON file at `path`, overwriting whatever was there before."""
    with path.open("w", encoding="utf-8") as file:
        dump(tasks, file)
