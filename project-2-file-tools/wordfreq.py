"""CLI entry point: wires argparse to word_counter.py and reports the top N words."""

import argparse
from pathlib import Path

from word_counter import count_words, tokenize, top_n  # noqa: F401


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

    parser = argparse.ArgumentParser(
        description="A CLI tool to count the words in text files \
            that shows the top N most frequent words"
    )

    parser.add_argument(
        "path", type=Path, help="path to a single text file or directory to scan."
    )

    parser.add_argument(
        "-r",
        dest="recursive",
        action="store_true",
        help="scan recursively the directory, if the path is a file it will be ignored",
    )

    parser.add_argument(
        "-n", "--top", type=int, default=10, help="number of top words to display"
    )

    return parser


def read_text(path: Path, recursive: bool = False) -> str:
    """Return the combined text content at `path`.

    If `path` is a single file, return its contents. If it's a directory, read
    every text file under it (think about `Path.rglob`) and concatenate their
    contents. Consider what "every text file" should mean here — all files? Only
    certain extensions like `.txt`/`.md`? That's your call.
    """
    if not path.exists():
        raise FileNotFoundError("The path does not exist")

    text = ""

    if path.is_file() and path.suffix == ".txt":
        text = path.read_text(encoding="utf-8")
    else:
        if recursive:
            text = "\n".join(
                [f.read_text(encoding="utf-8") for f in path.rglob("*.txt")]
            )
        else:
            text = "\n".join(
                [f.read_text(encoding="utf-8") for f in path.glob("*.txt")]
            )

    return text


def main() -> None:
    """Parse CLI args, read the target text, count words, and print the top N.

    Each printed line should show the word and its count, most frequent first.
    """
    parser = build_parser()

    args = parser.parse_args()

    text = ""

    try:
        text = read_text(args.path, args.recursive)
    except FileNotFoundError as ex:
        print(ex)

    print(text)


if __name__ == "__main__":
    main()
