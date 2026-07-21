# Python Practice Projects — 10 Projects, Simple → Advanced

This document is meant to be dropped into a project folder and used together with
`TUTOR.md` and Claude Code. It lists 10 projects of increasing difficulty, covering
CLIs, TUIs, GUIs, and web servers/APIs, along with the recommended Python packages
(standard library first, third-party where it genuinely helps), why they're
recommended, alternatives, and links to docs/source so you can dig deeper.

**How to use this with Claude Code:** work through the projects in order. For each
one, tell Claude Code which project you're starting (e.g. "let's start Project 3").
`TUTOR.md` tells Claude Code how to behave: it will give you a skeleton (structure,
class/function names, short descriptions) and then coach you through implementing it
via questions — not write the implementation for you.

> General tools worth having from the start, regardless of project:
> - **[venv](https://docs.python.org/3/library/venv.html)** (stdlib) — virtual environments. Alternative: [uv](https://github.com/astral-sh/uv) (very fast, handles venvs + packages + Python versions).
> - **[pytest](https://docs.pytest.org/)** ([GitHub](https://github.com/pytest-dev/pytest)) — the de facto standard test runner, much less boilerplate than stdlib `unittest`.
> - **[ruff](https://docs.astral.sh/ruff/)** ([GitHub](https://github.com/astral-sh/ruff)) — linter + formatter in one, extremely fast (Rust-based). Alternative: [black](https://black.readthedocs.io/) ([GitHub](https://github.com/psf/black)) for formatting only, plus [flake8](https://flake8.pycqa.org/) for linting.

---

## Overview Table

| # | Project | Type | Difficulty | Core New Concepts |
|---|---------|------|------------|--------------------|
| 1 | Todo List Manager | CLI | ⭐ | argparse, JSON persistence, file I/O |
| 2 | File Organizer & Word-Frequency Tool | CLI | ⭐⭐ | pathlib, regex, collections |
| 3 | Weather CLI | CLI + HTTP | ⭐⭐ | HTTP requests, APIs, env vars, pretty CLI output |
| 4 | Todo TUI | TUI | ⭐⭐⭐ | Event loops, widgets, reactive state |
| 5 | System Monitor TUI (htop-lite) | TUI | ⭐⭐⭐ | System introspection, live-updating UI |
| 6 | Desktop Todo App | GUI | ⭐⭐⭐ | Event-driven programming, MVC-ish layering |
| 7 | Image Viewer/Editor | GUI | ⭐⭐⭐⭐ | Image processing, file dialogs, undo/redo |
| 8 | Todo REST API | Web server | ⭐⭐⭐⭐ | HTTP APIs, validation, status codes |
| 9 | Full-Stack CRUD App | Web server | ⭐⭐⭐⭐⭐ | ORMs, migrations, templates/DB-backed UI |
| 10 | Real-Time Chat (capstone) | Web server + client | ⭐⭐⭐⭐⭐ | asyncio, websockets, concurrency, integration |

---

## Project 1 — Todo List Manager (CLI)

**Difficulty:** ⭐ (beginner)
**Goal:** Practice functions, data structures, control flow, and basic file persistence with zero external dependencies.

A command-line tool to add, list, complete, and delete tasks, persisted to a local JSON file. Example usage:
```
todo add "Buy milk"
todo list
todo done 2
todo remove 1
```

**Concepts practiced:** functions, dictionaries/lists, JSON serialization, file reading/writing, basic error handling, argument parsing.

**Recommended packages:**
- **[argparse](https://docs.python.org/3/library/argparse.html)** (stdlib) — parses subcommands (`add`, `list`, `done`, `remove`) and flags. It's the standard tool for this and ships with Python, so it's the right default before reaching for anything fancier.
- **[json](https://docs.python.org/3/library/json.html)** (stdlib) — trivial persistence format for a list of dicts.
- **[pathlib](https://docs.python.org/3/library/pathlib.html)** (stdlib) — for handling the storage file path in an OS-independent way.

**Alternatives / stretch goals:**
- **[click](https://click.palletsprojects.com/)** ([GitHub](https://github.com/pallets/click)) — a very popular, decorator-based CLI framework; nicer ergonomics than `argparse` for larger CLIs (auto-generated help, nested command groups).
- **[typer](https://typer.tiangolo.com/)** ([GitHub](https://github.com/fastapi/typer)) — built on top of Click, but you define commands as plain typed functions; very popular in modern Python CLIs and worth learning since you'll see it again in Project 3.
- Swap JSON for **[sqlite3](https://docs.python.org/3/library/sqlite3.html)** (stdlib) once you want querying/filtering — a nice bridge toward Project 9's databases.

---

## Project 2 — File Organizer & Word-Frequency Tool (CLI)

**Difficulty:** ⭐⭐
**Goal:** Get comfortable with the filesystem, text processing, and the standard library's data structures.

Two small utilities in one project (or pick one): (a) a script that organizes a messy folder by moving files into subfolders by extension/date, and (b) a script that reads a text file (or folder of files) and reports the top N most frequent words, ignoring punctuation/stopwords.

**Concepts practiced:** recursive directory traversal, string processing/regex, `Counter`, command-line flags, dry-run patterns (important habit: preview before you mutate the filesystem!).

**Recommended packages:**
- **[pathlib](https://docs.python.org/3/library/pathlib.html)** (stdlib) — walking directories (`Path.rglob`), moving/renaming files.
- **[re](https://docs.python.org/3/library/re.html)** (stdlib) — tokenizing words, stripping punctuation.
- **[collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter)** (stdlib) — the natural tool for frequency counting; knowing it well pays off constantly.
- **[shutil](https://docs.python.org/3/library/shutil.html)** (stdlib) — moving/copying files safely.

**Alternatives / stretch goals:**
- **[rich](https://rich.readthedocs.io/)** ([GitHub](https://github.com/Textualize/rich)) — for a nicer summary table/progress bar of what got moved or counted. This is the single most popular "make my terminal output pretty" library in the Python ecosystem and you'll reuse it in almost every later CLI/TUI project.
- **[nltk](https://www.nltk.org/)** ([GitHub](https://github.com/nltk/nltk)) or **[spaCy](https://spacy.io/)** ([GitHub](https://github.com/explosion/spaCy)) if you want proper stopword lists/tokenization instead of hand-rolled regex — overkill for this project but good to know they exist.

---

## Project 3 — Weather CLI (CLI + HTTP API)

**Difficulty:** ⭐⭐
**Goal:** First contact with calling a real HTTP API, handling network errors, and structuring a slightly bigger CLI.

A CLI that takes a city name (or coordinates) and prints current weather + a short forecast by calling a free weather API (e.g. [Open-Meteo](https://open-meteo.com/), which needs no API key — good for practice).

**Concepts practiced:** making HTTP requests, JSON responses, error/timeout handling, environment variables for config/secrets, formatting structured output.

**Recommended packages:**
- **[requests](https://requests.readthedocs.io/)** ([GitHub](https://github.com/psf/requests)) — the most widely used HTTP client in Python; simple, synchronous, huge community, the natural default for a CLI that makes a couple of API calls.
- **[typer](https://typer.tiangolo.com/)** ([GitHub](https://github.com/fastapi/typer)) — a good place to actually adopt it (vs. Project 1's `argparse`) since you'll want typed options like `--units metric`.
- **[rich](https://rich.readthedocs.io/)** ([GitHub](https://github.com/Textualize/rich)) — render the forecast as a colored table.
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** — if the API you pick needs a key, load it from a `.env` file instead of hardcoding it.

**Alternatives / stretch goals:**
- **[httpx](https://www.python-httpx.org/)** ([GitHub](https://github.com/encode/httpx)) — a modern alternative to `requests` with the same feel but native async support (`httpx.AsyncClient`); worth switching to once you meet `asyncio` in Project 10.
- Add caching of responses with **[requests-cache](https://requests-cache.readthedocs.io/)** to avoid hammering the API while developing.

---

## Project 4 — Todo TUI (Text User Interface)

**Difficulty:** ⭐⭐⭐
**Goal:** Move from linear CLI scripts to an event-driven, stateful application — a big conceptual jump.

Rebuild Project 1's todo app as a full-screen terminal app: a list of tasks you can navigate with arrow keys, mark done, add/edit/delete, all without leaving one screen.

**Concepts practiced:** event loops, widgets/composition, application state vs. UI state, keybindings, reading from and writing to the same JSON/SQLite store from Project 1 (nice continuity).

**Recommended packages:**
- **[textual](https://textual.textualize.io/)** ([GitHub](https://github.com/Textualize/textual)) — the current standard for building modern TUIs in Python: reactive attributes, CSS-like styling, widgets, works over SSH, has an active ecosystem. This is the recommended choice.
- **[rich](https://rich.readthedocs.io/)** ([GitHub](https://github.com/Textualize/rich)) — Textual is built on top of Rich for rendering; you'll use Rich renderables inside Textual widgets.

**Alternatives:**
- **[curses](https://docs.python.org/3/howto/curses.html)** (stdlib, Unix-like systems / via `windows-curses` on Windows) — the "do it from scratch" option. Good for understanding what a TUI framework is actually doing underneath, but noticeably more low-level and manual than Textual.
- **[urwid](https://urwid.org/)** ([GitHub](https://github.com/urwid/urwid)) — an older, still-used TUI library; more manual than Textual but lighter weight.
- **[prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/)** ([GitHub](https://github.com/prompt-toolkit/python-prompt-toolkit)) — great if you want an interactive REPL-style app rather than a full-screen widget app.

---

## Project 5 — System Monitor TUI ("htop-lite")

**Difficulty:** ⭐⭐⭐
**Goal:** Combine a TUI framework with live, real-world system data and periodic refresh — your first "dashboard."

A terminal dashboard showing live CPU/memory/disk usage and a sortable process list, refreshing every second or two, similar in spirit to `htop`.

**Concepts practiced:** polling/refresh loops, background tasks/timers inside a TUI event loop, sorting/formatting tabular data, working with a lower-level system API.

**Recommended packages:**
- **[psutil](https://psutil.readthedocs.io/)** ([GitHub](https://github.com/giampaolo/psutil)) — the standard cross-platform library for CPU/memory/disk/process/network stats. Virtually every "system monitor in Python" project uses this.
- **[textual](https://textual.textualize.io/)** ([GitHub](https://github.com/Textualize/textual)) — for the live-updating dashboard UI (its `DataTable` widget and `set_interval` timer API are a good fit here).

**Alternatives:**
- Use **[rich](https://rich.readthedocs.io/)**'s `Live` display instead of Textual if you want something lighter than a full TUI framework — good if you want to compare "just refresh the terminal" vs. "real widget framework."
- **[plotext](https://github.com/piccolomo/plotext)** — terminal plotting library if you want an actual live-updating line chart of CPU usage instead of just numbers.

---

## Project 6 — Desktop Todo App (GUI)

**Difficulty:** ⭐⭐⭐
**Goal:** First native desktop GUI — event-driven programming with widgets, layouts, and callbacks instead of a terminal event loop.

The same todo app again, this time as a native window with buttons, a list/table widget, and a text entry field, reusing the persistence layer from Project 1 for the third time.

**Concepts practiced:** windows/widgets/layouts, callback-driven programming, separating "data/state" from "presentation" (a lightweight MVC), packaging a small desktop app.

**Recommended packages:**
- **[tkinter](https://docs.python.org/3/library/tkinter.html)** (stdlib, plus **[ttk](https://docs.python.org/3/library/tkinter.ttk.html)** for modern-looking themed widgets) — ships with almost every Python install, no extra dependency, and is genuinely the right choice for a first GUI: you learn the concepts (widgets, layout managers, event bindings) without fighting an install.

**Alternatives:**
- **[PySide6](https://doc.qt.io/qtforpython-6/)** ([GitHub](https://github.com/qtproject/pyside-pyside-setup)) — official Python bindings for Qt (LGPL license, so freely usable commercially). More powerful/professional-looking than tkinter, steeper learning curve. Use this if you want the skills to transfer toward Project 7 and beyond.
- **[PyQt6](https://www.riverbankcomputing.com/software/pyqt/)** — the other major Qt binding, near-identical API to PySide6 but GPL/commercial licensed.
- **[Kivy](https://kivy.org/)** ([GitHub](https://github.com/kivy/kivy)) — good if you're interested in touch interfaces or eventually deploying to mobile.
- **[customtkinter](https://github.com/TomSchimansky/CustomTkinter)** — a drop-in, modern-themed layer on top of tkinter if you like tkinter's simplicity but want it to look less dated.

---

## Project 7 — Image Viewer / Simple Editor (GUI)

**Difficulty:** ⭐⭐⭐⭐
**Goal:** A GUI that does real, non-trivial work (image manipulation) and manages more complex state (undo/redo, file dialogs, multiple views).

An app to open an image, view it, and apply a few operations — crop, rotate, resize, brightness/contrast, grayscale — with undo/redo and "save as."

**Concepts practiced:** file dialogs, image processing basics, the command pattern (for undo/redo), keeping a GUI responsive during slower operations, canvas/pixel coordinate systems.

**Recommended packages:**
- **[Pillow](https://pillow.readthedocs.io/)** ([GitHub](https://github.com/python-pillow/Pillow)) — the de facto standard image processing library in Python (a maintained fork of the old PIL). Covers loading, saving, resizing, filters, color transforms — everything this project needs.
- **[PySide6](https://doc.qt.io/qtforpython-6/)** ([GitHub](https://github.com/qtproject/pyside-pyside-setup)) or **tkinter** (per Project 6) for the GUI shell — pick whichever you chose there and build on it, or use this project as a reason to switch from tkinter to PySide6 if you want the extra depth.

**Alternatives:**
- **[wxPython](https://wxpython.org/)** ([GitHub](https://github.com/wxWidgets/Phoenix)) — another mature GUI toolkit with a native look-and-feel on each OS.
- **[OpenCV](https://opencv.org/)** (`opencv-python` on PyPI) ([GitHub](https://github.com/opencv/opencv-python)) — if you want to go beyond basic edits into real computer-vision territory (edge detection, filters, face detection) instead of just Pillow's operations.

---

## Project 8 — Todo REST API (Web Server)

**Difficulty:** ⭐⭐⭐⭐
**Goal:** First web server — expose the todo app's functionality over HTTP as a JSON API instead of a UI, and understand HTTP semantics properly (methods, status codes, request/response bodies).

A REST API with endpoints like `GET /todos`, `POST /todos`, `PATCH /todos/{id}`, `DELETE /todos/{id}`, backed (for now) by an in-memory list or the JSON file from Project 1. Test it with `curl`, [HTTPie](https://httpie.io/), or the interactive docs.

**Concepts practiced:** routing, request validation, status codes, serialization, path/query/body parameters, automatically generated API docs, basic testing of an API with `pytest` + a test client.

**Recommended packages:**
- **[FastAPI](https://fastapi.tiangolo.com/)** ([GitHub](https://github.com/fastapi/fastapi)) — the recommended choice: modern, type-hint driven, generates interactive OpenAPI docs for free, async-first, and currently one of the most popular Python web frameworks for APIs specifically.
- **[pydantic](https://docs.pydantic.dev/)** ([GitHub](https://github.com/pydantic/pydantic)) — FastAPI uses this under the hood for request/response validation via type-annotated models; you'll be writing `pydantic.BaseModel` classes directly, so it's worth understanding on its own.
- **[uvicorn](https://www.uvicorn.org/)** ([GitHub](https://github.com/encode/uvicorn)) — the ASGI server that actually runs a FastAPI app (`uvicorn main:app --reload`).

**Alternatives:**
- **[Flask](https://flask.palletsprojects.com/)** ([GitHub](https://github.com/pallets/flask)) — the long-standing, simpler alternative (WSGI, synchronous, minimal by default, add pieces as needed via extensions). Great to know since a huge amount of existing Python web code is Flask; a bit less "batteries included" for building typed APIs than FastAPI.
- **[Django REST Framework](https://www.django-rest-framework.org/)** ([GitHub](https://github.com/encode/django-rest-framework)) on top of **[Django](https://www.djangoproject.com/)** ([GitHub](https://github.com/django/django)) — much heavier, but standard for larger, more "batteries included" API projects.

---

## Project 9 — Full-Stack CRUD App with a Database (Web Server)

**Difficulty:** ⭐⭐⭐⭐⭐
**Goal:** Add real persistence (a database, not a JSON file) and a server-rendered UI on top of Project 8's API concepts — the classic "full stack CRUD app."

A multi-user note-taking or bookmarking app: users can create an account, log in, and create/edit/delete their own items, stored in a real relational database, rendered either as server-side HTML pages or as an API consumed by a small frontend.

**Concepts practiced:** relational data modeling, ORMs vs. raw SQL, database migrations, sessions/authentication basics, templating (if server-rendered), separating layers (routes/business logic/data access).

**Recommended packages:**
- **[SQLAlchemy](https://docs.sqlalchemy.org/)** ([GitHub](https://github.com/sqlalchemy/sqlalchemy)) — the standard Python ORM/SQL toolkit; pairs naturally with FastAPI or Flask and is the most widely used ORM in the ecosystem outside of Django.
- **[Alembic](https://alembic.sqlalchemy.org/)** ([GitHub](https://github.com/sqlalchemy/alembic)) — schema migrations for SQLAlchemy; learning migrations (vs. just re-creating tables) is an important professional habit.
- **[Jinja2](https://jinja.palletsprojects.com/)** ([GitHub](https://github.com/pallets/jinja)) — if you render server-side HTML pages rather than a pure JSON API; both Flask and FastAPI support it.
- **SQLite** via **[sqlite3](https://docs.python.org/3/library/sqlite3.html)** (stdlib) as the actual database for local development — zero setup, a real file on disk.

**Alternatives:**
- **[Django](https://www.djangoproject.com/)** ([GitHub](https://github.com/django/django)) — if you'd rather learn "the batteries-included way": Django bundles its own ORM, admin panel, auth system, and templating, trading flexibility for a lot of built-in structure. Very popular for exactly this kind of app.
- **[SQLModel](https://sqlmodel.tiangolo.com/)** ([GitHub](https://github.com/fastapi/sqlmodel)) — combines SQLAlchemy + Pydantic into one model definition; nice if you're already using FastAPI and want less duplication between your API schema and DB schema.
- Swap SQLite for **[PostgreSQL](https://www.postgresql.org/)** + **[psycopg](https://www.psycopg.org/)** once you want something closer to production.

---

## Project 10 — Real-Time Multi-User Chat (Capstone)

**Difficulty:** ⭐⭐⭐⭐⭐
**Goal:** Tie everything together: a persistent (async) web server, real-time bidirectional communication, a database, and a client — pick a TUI or GUI client to also reuse Projects 4–7's skills.

A chat server that accepts multiple simultaneous client connections over WebSockets, broadcasts messages to everyone in a room, persists message history to a database, and supports at least a couple of rooms/usernames. Build at least one client: a TUI (Textual) or GUI (PySide6/tkinter) chat window, or even a second CLI/terminal client.

**Concepts practiced:** concurrency (`asyncio`), the WebSocket protocol, managing shared state safely across concurrent connections, client/server architecture, integrating a database into an async app, putting a UI on top of a live data stream.

**Recommended packages:**
- **[asyncio](https://docs.python.org/3/library/asyncio.html)** (stdlib) — Python's core async/concurrency library; you cannot really do this project without understanding `async`/`await`, tasks, and event loops, so this is the central new concept.
- **[FastAPI](https://fastapi.tiangolo.com/)** ([GitHub](https://github.com/fastapi/fastapi)) — has built-in WebSocket route support (`@app.websocket(...)`), so you can build the chat server as an extension of what you learned in Project 8.
- **[websockets](https://websockets.readthedocs.io/)** ([GitHub](https://github.com/python-websockets/websockets)) — a good alternative/complement if you want a standalone WebSocket server without a full web framework, or to build the *client* side of a non-browser chat client.
- Reuse **[SQLAlchemy](https://docs.sqlalchemy.org/)** ([GitHub](https://github.com/sqlalchemy/sqlalchemy)) from Project 9 for persisting chat history.
- **[textual](https://textual.textualize.io/)** ([GitHub](https://github.com/Textualize/textual)) (which also supports async natively) if you build a TUI client.

**Alternatives:**
- **[Django Channels](https://channels.readthedocs.io/)** ([GitHub](https://github.com/django/channels)) — if you went the Django route in Project 9, this is Django's answer to WebSockets/async.
- **[Redis](https://redis.io/)** via **[redis-py](https://redis-py.readthedocs.io/)** ([GitHub](https://github.com/redis/redis-py)) as a pub/sub backbone — useful once you want multiple server processes to share broadcast messages (a real horizontal-scaling concern), beyond the scope of a single-process version but a great "if I wanted to scale this" stretch goal.
- **[Celery](https://docs.celeryq.dev/)** ([GitHub](https://github.com/celery/celery)) — not needed for chat itself, but worth knowing about as the standard background-task queue if you add features like "email me a digest of missed messages."

---

## Suggested Path

1. Do Projects 1–3 back to back — they all reuse similar CLI patterns, so the second and third should feel progressively faster.
2. Projects 4 and 6 both rebuild Project 1's todo app in a new interface paradigm (TUI, then GUI) — resist the urge to skip this "repetition," it's exactly what cements event-driven thinking.
3. Project 5 and 7 add real complexity on top of a UI you already understand.
4. Projects 8 and 9 introduce the server side; 9 is a big step up (databases + migrations), so don't rush it.
5. Project 10 is intentionally a capstone that pulls together async, servers, databases, and a UI client — expect it to take meaningfully longer than the others.
