"""Task operations: pure functions that transform a list of task dicts.

A "task" is a dict with (at least) these keys: `id` (int), `description` (str),
and `done` (bool). None of these functions read or write files directly — that's
`storage.py`'s job. Keeping these pure (input list in, new list out) makes them
easy to test without touching disk.
"""


def add_task(tasks: list[dict], description: str) -> list[dict]:
    """Return a new task list with one additional task appended.

    The new task should get a fresh unique `id` (think about how to derive one
    from the existing tasks), the given `description`, and `done` set to False.
    """
    max_id = max((task["id"] for task in tasks), default=0)
    new_task = {"id": max_id + 1, "description": description, "done": False}
    new_tasks = tasks + [new_task]

    return new_tasks


def mark_done(tasks: list[dict], task_id: int) -> list[dict]:
    """Return the task list with the task matching `task_id` marked done (`done=True`).

    Tasks that don't match `task_id` should be unaffected. Consider what should
    happen if `task_id` doesn't match anything in the list.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True

    return tasks


def remove_task(tasks: list[dict], task_id: int) -> list[dict]:
    """Return a new task list with the task matching `task_id` removed entirely."""
    new_tasks = [task for task in tasks if task["id"] != task_id]
    return new_tasks


def format_task_list(tasks: list[dict]) -> str:
    """Return a human-readable, multi-line string representation of `tasks`.

    Each line should make it clear what the task's id, description, and done
    status are (e.g. something a user could read directly in the terminal).
    """
    max_width = max((len(task["description"]) for task in tasks), default=10)
    output = f"{'Id':<1000} | {'Description':<{max_width}} | {'Done':>4}"

    for task in tasks:
        output += f"{task['id']:<1000} | {task['description']:<{max_width}} \
                | {('O' if task['done'] else ''):>4}"

    return output
