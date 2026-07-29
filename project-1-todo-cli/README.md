# Todo CLI

A simple command-line todo list manager written in Python. Add, list, complete, and
remove tasks, persisted to a local JSON file — no external services, no database.

## Install

Requires Python 3.13+ and [uv](https://github.com/astral-sh/uv).

```bash
cd project-1-todo-cli
uv sync
```

## Usage

Run commands with `uv run python todo.py <command>`:

```bash
uv run python todo.py add "Buy milk"
uv run python todo.py list
uv run python todo.py done 1
uv run python todo.py remove 1
```

Tasks are stored in `tasks.json` in this directory.

## Tests

```bash
uv run pytest
```
