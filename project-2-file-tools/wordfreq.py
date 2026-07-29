"""CLI entry point: wires argparse to word_counter.py and reports the top N words."""

import argparse
from pathlib import Path

from word_counter import count_words, tokenize, top_n


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argparse parser for this CLI.

    Should accept:
        - a required positional `path` (a single text file, or a directory to
          scan recursively for text files),
        - an optional `-n`/`--top` int flag (default 10) for how many words to show.

    Example usage this should support:
        wordfreq notes.txt
        wordfreq ./notes_folder --top 20
    """
    raise NotImplementedError


def read_text(path: Path) -> str:
    """Return the combined text content at `path`.

    If `path` is a single file, return its contents. If it's a directory, read
    every text file under it (think about `Path.rglob`) and concatenate their
    contents. Consider what "every text file" should mean here — all files? Only
    certain extensions like `.txt`/`.md`? That's your call.
    """
    raise NotImplementedError


def main() -> None:
    """Parse CLI args, read the target text, count words, and print the top N.

    Each printed line should show the word and its count, most frequent first.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
