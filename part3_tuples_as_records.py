"""Part 4: Indexing with a Dictionary (id -> row)
This mimics a database index for fast lookups.
"""

students = [
    {"id": 1, "name": "Alice", "school": "GSAS", "credits": 32},
    {"id": 2, "name": "Bob", "school": "Tandon", "credits": 30},
    {"id": 3, "name": "Carol", "school": "GSAS", "credits": 40},
    {"id": 4, "name": "Dan", "school": "CAS", "credits": 18}
]

# Build an index: id -> student row
index_by_id = {}
for row in students:
    index_by_id[row["id"]] = row

# TODO 1: Use index_by_id to print the record for id=3

def find_by_id(index, student_id):
    """Return the row for student_id, or None if missing."""
    # TODO 2: implement
    for student in index:
        if student["id"]==student_id:
            return student

# TODO 3: Insert a new student into BOTH students and index_by_id
#   Example: {"id": 5, "name": "Eve", "school": "CAS", "credits": 22}
students.append({"id": 5, "name": "Eve", "school": "CAS", "credits": 22})
index_by_id[5]={"id": 5, "name": "Eve", "school": "CAS", "credits": 22}
# TODO 4: Update a student’s credits using the index (show list reflects it too)
index_by_id[0]["credits"]+=4
# Reflection (answer in a comment):
# TODO: Why is dict lookup conceptually faster than scanning a list?
#becuse dict is a hash map is theoretically O(1) for searching. List searching is O(n)
