from pathlib import Path
from typing import NamedTuple

import pytest
from file_organizer import group_by_extension

# Write your own tests here for the functions in file_organizer.py.
# A few things worth thinking about testing once you get there:
#   - group_by_extension: what happens to a file with no extension at all?
#   - group_by_date: how will you control mtime in a test so it's deterministic?
#     (hint: you don't have to use real files on disk for the grouping functions.)
#   - plan_moves: does it produce the destination paths you expect for a small,
#     hand-built list of Path objects?


class CreatedPaths(NamedTuple):
    all: list[Path]
    dirs: list[Path]
    files: list[Path]


@pytest.fixture
def create_files(tmp_path: Path) -> CreatedPaths:
    relative_files = [
        "test/nested_test/sample.txt",
        "readme.md",
        "test/sample_2.txt",
        "test/nested_test/sample",
        ".bashrc.bak",
        "test/.env",
        "test/nested_test/.bashrc",
        "config.yml",
        "test/pyproject.toml",
    ]

    dirs = [tmp_path / "test", tmp_path / "test/nested_test"]
    files = []

    for relative_file in relative_files:
        file_path = tmp_path / relative_file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()
        files.append(file_path)

    return CreatedPaths(all=dirs + files, dirs=dirs, files=files)


def test_group_by_extension_basic(create_files):
    group = group_by_extension(create_files.all)
    assert "txt" in group
    assert "md" in group
    assert "bak" in group
    assert "toml" in group
    assert "yml" in group
    assert len(group["txt"]) == 2
    assert len(group["md"]) == 1
    assert len(group["toml"]) == 1
    assert len(group["bak"]) == 1
    assert len(group["yml"]) == 1


def test_group_by_extension_no_extension(create_files):
    group = group_by_extension(create_files.all)
    assert "no_extension" in group
    assert len(group["no_extension"]) == 1


def test_group_by_extension_dotfile(create_files):
    group = group_by_extension(create_files.all)
    assert "dotfile" in group
    assert len(group["dotfile"]) == 2


def test_group_by_extension_skips_directories(create_files):
    group = group_by_extension(create_files.all)
    test_dir = create_files.dirs[0]
    nested_dir = create_files.dirs[1]
    assert test_dir not in group["no_extension"]
    assert nested_dir not in group["no_extension"]
