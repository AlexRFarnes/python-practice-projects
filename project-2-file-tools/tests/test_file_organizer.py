from file_organizer import group_by_date, group_by_extension, plan_moves  # noqa: F401

# Write your own tests here for the functions in file_organizer.py.
# A few things worth thinking about testing once you get there:
#   - group_by_extension: what happens to a file with no extension at all?
#   - group_by_date: how will you control mtime in a test so it's deterministic?
#     (hint: you don't have to use real files on disk for the grouping functions.)
#   - plan_moves: does it produce the destination paths you expect for a small,
#     hand-built list of Path objects?
