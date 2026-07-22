from pathlib import Path

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
