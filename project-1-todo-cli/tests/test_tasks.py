from pathlib import Path

import pytest
from tasks import add_task, format_task_list

# Write your own tests here for the functions in tasks.py and storage.py.
# A few things worth thinking about testing once you get there:
#   - add_task: does it assign a sensible new id? does done start False?
#   - mark_done: does the right task change, and only that one?
#   - remove_task: what happens if the id isn't in the list?
#   - load_tasks: what should happen if the file doesn't exist yet?


TEST_FILE = Path(__file__).parent / "test.json"
tasks = [
    {"id": 0, "description": "Buy milk", "done": True},
    {"id": 1, "description": "Pay bills", "done": False},
    {"id": 2, "description": "Cook dinner", "done": False},
]


def test_format_task_list():
    output = format_task_list(tasks)
    assert isinstance(output, str), "Output should be a string"
    assert "Id" in output, "Output should contain the word 'Id'"
    assert "Description" in output, "Output should contain the word 'Description'"
    assert "Done" in output, "Output should contain the word 'IdDone'"


def test_add_task():
    description = "Buy groceries"

    new_tasks = add_task(tasks, description)

    assert len(new_tasks) == len(tasks) + 1, (
        "After adding the task, the new tasks list should be greater by one than the original"
    )

    with pytest.raises(ValueError, match="Description can't be empty"):
        add_task(tasks, "")
