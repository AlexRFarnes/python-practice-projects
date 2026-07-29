"""File-organizing logic: pure functions that decide where files should move to.

None of these functions touch the filesystem beyond reading metadata (name,
extension, mtime) — they don't move/copy anything themselves. That's `organize.py`'s
job, mirroring the pure-logic/IO split used in word_counter.py and Project 1.
"""

from pathlib import Path


def group_by_extension(paths: list[Path]) -> dict[str, list[Path]]:
    """Group `paths` into a dict keyed by file extension (without the dot).

    Files with no extension should land in some sensible bucket (your call what
    to call it, e.g. "no_extension").
    """
    raise NotImplementedError


def group_by_date(paths: list[Path]) -> dict[str, list[Path]]:
    """Group `paths` into a dict keyed by a date string derived from each file's
    last-modified time (think `Path.stat().st_mtime`), e.g. "2026-07".
    """
    raise NotImplementedError


def plan_moves(paths: list[Path], dest_root: Path, group_by: str) -> list[tuple[Path, Path]]:
    """Return a list of (source_path, destination_path) pairs describing the move.

    `group_by` will be either "extension" or "date" — use the matching grouping
    function above to decide each file's destination subfolder under `dest_root`.
    This function should not move anything; it just plans.
    """
    raise NotImplementedError
