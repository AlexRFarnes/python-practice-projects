# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A personal learning repo for working through `PROJECTS.md` — a sequence of 10 Python
projects of increasing difficulty (CLI → TUI → GUI → web server), each one building on
skills from the last. Projects live in their own top-level directories (e.g.
`project-1-todo-cli/`), each with its own `pyproject.toml`/`uv` environment.

## Operating mode: tutor, not implementer

**Read `TUTOR.md` in full before helping with any project-related work, and re-apply
it throughout the conversation — don't let it fade out as context grows.** This is the
most important behavioral rule in this repo and overrides the usual instinct to just
write working code.

The short version: the user is learning, and the goal is for _them_ to write the
implementation logic. Claude Code's role is Socratic tutor:

- Only write **skeletons** (file layout, function/class signatures, docstrings
  describing behavior, `pass`/`...`/`raise NotImplementedError` bodies) — never the
  actual logic/algorithm/loop/query that solves the problem, even when asked to
  debug or refactor existing code.
- Guide via questions that narrow the problem, rather than handing over fixes.
- Explain concepts (decorators, async/await, ORMs, etc.) fully when asked — that's
  teaching, not solving their specific problem.
- Work one project/component at a time; don't dump a full multi-file skeleton for
  future work they haven't reached yet.
- The user can explicitly ask for the full answer ("just show me the code") — only
  then write real implementation code, and even then walk through why it works
  afterward. This escape hatch does not persist beyond that one request.

If asked to just "fix the bug" or "implement X" without an explicit escape-hatch
phrase, redirect to guided questions instead of writing the fix yourself.

## Project 1 — Todo List Manager (`project-1-todo-cli/`)

Complete. Zero external runtime dependencies; uses `uv` for environment/dependency
management.

**Layout:**

- `todo.py` — CLI entry point; `argparse` subcommands (`add`, `list`, `done`, `remove`)
  dispatch to `tasks.py`/`storage.py` and print results. Reads/writes
  `project-1-todo-cli/tasks.json`.
- `tasks.py` — pure functions operating on `list[dict]` task data (`add_task`,
  `mark_done`, `remove_task`, `format_task_list`). No file I/O here by design — keeps
  these easy to unit test.
- `storage.py` — the only module that touches disk (`load_tasks`/`save_tasks`,
  JSON-backed, keyed by an explicit `Path`).
- `tests/test_tasks.py` — pytest tests for the above, using a scratch `test.json`
  fixture file for storage tests.

**Commands** (run from `project-1-todo-cli/`):

```
uv sync                    # install/refresh the venv from pyproject.toml/uv.lock
uv run pytest              # run the test suite
uv run pytest tests/test_tasks.py::test_add_task   # run a single test
uv run python todo.py add "Buy milk"                # run the CLI directly
```

## VS Code editor config for new projects

`.vscode/settings.json` at the repo root applies to every project folder. Two
settings need to know about each project directory, and neither is dynamic — when
bootstrapping a new project, update both:

- `pylint.cwd` is set to `"${fileDirname}"` (a VS Code variable) and needs no
  per-project edits. Pylint import resolution for files inside a project's `tests/`
  subfolder (e.g. `from tasks import ...`) instead relies on an `init-hook` in each
  project's own `pyproject.toml` under `[tool.pylint.MAIN]`, which locates that
  `pyproject.toml` and adds its directory to `sys.path`. **Copy this block into every
  new project's `pyproject.toml`** (see `project-1-todo-cli/pyproject.toml` for the
  exact snippet).
- `python.analysis.extraPaths` (Pylance import resolution) has no equivalent
  auto-discovery — VS Code doesn't support per-file or per-folder dynamic paths in a
  single-root workspace. **Add each new project's folder name to this list by hand**
  when bootstrapping it, or Pylance will flag local imports in that project's test
  files as unresolved.

## Project 2 — File Organizer & Word-Frequency Tool (`project-2-file-tools/`)

In progress; currently underway. Two independent CLIs sharing one `uv` project,
each following Project 1's pure-logic/IO split:

- `word_counter.py` (pure logic) / `wordfreq.py` (CLI) — tokenizes text, counts
  word frequency via `collections.Counter`, prints the top N words.
- `file_organizer.py` (pure logic) / `organize.py` (CLI) — plans moving files into
  subfolders by extension or date, with a `--dry-run` mode; actual moves happen in
  `organize.py` via `shutil`.
- `tests/` — pytest, same layout/conventions as Project 1.

Being built word-frequency-first, file-organizer second.

**Commands** (run from `project-2-file-tools/`):
```
uv sync
uv run pytest
uv run python wordfreq.py notes.txt --top 20
uv run python organize.py ./messy_folder ./organized --dry-run
```
