"""CLI entry point: wires argparse subcommands to the storage and tasks modules."""

import argparse
from pathlib import Path

from storage import load_tasks, save_tasks
from tasks import add_task, format_task_list, mark_done, remove_task

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
    # Create the main parser
    parser = argparse.ArgumentParser(
        description="A CLI to manage your todos in the terminal built with Python 🐍"
    )

    # Add subparsers container
    # 'dest="command"' stores the name of the invoked sub-command into args.command
    subparsers = parser.add_subparsers(
        dest="command", help="Available sub-commands", required=True
    )

    # Create the add sub-command parser
    parser_add = subparsers.add_parser("add", help="Add a new todo")
    parser_add.add_argument("description", help="Description of the todo")

    # Create the list sub-command parser
    subparsers.add_parser("list", help="List all the todos")

    # Create the done sub-command parser
    parser_done = subparsers.add_parser("done", help="Mark a todo as done")
    parser_done.add_argument("id", type=int, help="The id of the todo to mark as done")

    # Create the remove sub-command parser
    parser_remove = subparsers.add_parser("remove", help="Delete a todo")
    parser_remove.add_argument("id", type=int, help="The id of the todo to remove")

    return parser


def main() -> None:
    """Parse CLI args, dispatch to the right storage/tasks functions, and print output.

    This should load tasks from TASKS_FILE, perform whatever action the parsed
    args request (using functions from `tasks.py`), save any changes back via
    `storage.py`, and print appropriate output to the user.
    """
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        tasks = load_tasks(TASKS_FILE)
        tasks = add_task(tasks, args.description)
        save_tasks(TASKS_FILE, tasks)
        print("Todo added!")
    elif args.command == "list":
        tasks = load_tasks(TASKS_FILE)
        print(format_task_list(tasks))
    elif args.command == "done":
        tasks = load_tasks(TASKS_FILE)
        tasks = mark_done(tasks, args.id)
        save_tasks(TASKS_FILE, tasks)
        print(f"Todo {args.id} done!")
    elif args.command == "remove":
        tasks = load_tasks(TASKS_FILE)
        tasks = remove_task(tasks, args.id)
        save_tasks(TASKS_FILE, tasks)
        print(f"Todo {args.id} removed!")


if __name__ == "__main__":
    main()
