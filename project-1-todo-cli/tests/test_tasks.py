from json import dump
from pathlib import Path

import pytest
from storage import load_tasks, save_tasks
from tasks import add_task, format_task_list, mark_done, remove_task

# Write your own tests here for the functions in tasks.py and storage.py.
# A few things worth thinking about testing once you get there:
#   - add_task: does it assign a sensible new id? does done start False?
#   - mark_done: does the right task change, and only that one?
#   - remove_task: what happens if the id isn't in the list?
#   - load_tasks: what should happen if the file doesn't exist yet?


TEST_FILE = Path(__file__).parent / "test.json"


def test_format_task_list():
    tasks = [
        {"id": 0, "description": "Buy milk", "done": True},
        {"id": 1, "description": "Pay bills", "done": False},
        {"id": 2, "description": "Cook dinner", "done": False},
    ]
    output = format_task_list(tasks)
    assert isinstance(output, str), "Output should be a string"
    assert "Id" in output, "Output should contain the word 'Id'"
    assert "Description" in output, "Output should contain the word 'Description'"
    assert "Done" in output, "Output should contain the word 'IdDone'"


def test_add_task():
    tasks = [
        {"id": 0, "description": "Buy milk", "done": True},
        {"id": 1, "description": "Pay bills", "done": False},
        {"id": 2, "description": "Cook dinner", "done": False},
    ]

    description = "Buy groceries"

    updated_tasks = add_task(tasks, description)

    assert len(updated_tasks) == len(tasks) + 1, (
        "After adding the task, the upodated tasks list length should be greater by one than the original"
    )

    with pytest.raises(ValueError, match="Description can't be empty"):
        add_task(tasks, "")


def test_remove_task():
    tasks = [
        {"id": 0, "description": "Buy milk", "done": True},
        {"id": 1, "description": "Pay bills", "done": False},
        {"id": 2, "description": "Cook dinner", "done": False},
    ]

    task_id = 0

    updated_tasks = remove_task(tasks, task_id)

    assert len(updated_tasks) == len(tasks) - 1, (
        "After removing a task, the updated taks list length should be one less than the original task list"
    )

    assert 0 not in [task["id"] for task in updated_tasks], (
        f"Task with id {task_id} should not be in the updated tasks list"
    )


def test_done_task():
    tasks = [
        {"id": 0, "description": "Buy milk", "done": False},
        {"id": 1, "description": "Pay bills", "done": False},
        {"id": 2, "description": "Cook dinner", "done": False},
    ]

    task_id = 0

    updated_tasks = mark_done(tasks, task_id)

    assert updated_tasks[0]["done"] is True, (
        f"Done should be true for the task with id: {task_id}"
    )


def test_save_tasks():
    tasks = [
        {"id": 0, "description": "Buy milk", "done": False},
        {"id": 1, "description": "Pay bills", "done": False},
        {"id": 2, "description": "Cook dinner", "done": False},
    ]

    save_tasks(TEST_FILE, tasks)

    with open(TEST_FILE, "r", encoding="utf-8") as file:
        read_tasks = file.readlines()

        assert len(read_tasks) > 0, (
            "The file should not be empty after saving the tasks to it"
        )

    TEST_FILE.unlink()


def test_load_tasks():
    TEST_FILE = Path(__file__).parent / "test.json"

    tasks = load_tasks(TEST_FILE)

    assert len(tasks) == 0, "Loading a nonexistent file should return an empty list"

    tasks = [
        {"id": 0, "description": "Buy milk", "done": False},
        {"id": 1, "description": "Pay bills", "done": False},
        {"id": 2, "description": "Cook dinner", "done": False},
    ]

    with TEST_FILE.open("w", encoding="utf-8") as file:
        dump(tasks, file)

    tasks = load_tasks(TEST_FILE)

    assert len(tasks) == 3, "Loading a file with data should return the whole data"

    TEST_FILE.unlink()
