"""Challenge Extension (Fast Finishers)
Pick 1–4 challenges. Do as many as you can.

Hints:
- An index is just a dictionary built for a purpose.
- Constraints are just rules you enforce in code.
"""

students = [
    {"id": 1, "name": "Alice", "school": "GSAS", "credits": 32},
    {"id": 2, "name": "Bob", "school": "Tandon", "credits": 30},
    {"id": 3, "name": "Carol", "school": "GSAS", "credits": 40},
    {"id": 4, "name": "Dan", "school": "CAS", "credits": 18}
]

# Challenge 1: Build a school index: school -> list of student rows
# TODO
school_to_students={}
for student in students:
    if student["school"] in school_to_students:
        school_to_students[student["school"]].append(student)
    else:
        school_to_students[student["school"]]=[student]
# Challenge 2: Enforce unique ids on insert
# Write insert_student(students, index_by_id, new_row) that rejects duplicate id
# TODO
def insert_student(students, index_by_id, new_row):
    return

# Challenge 3: Mini query function:
# query(rows, school=None, min_credits=None) -> list of matching rows
# TODO
def query(rows, school=None, min_credits=None):
    if not school:
        return [student for student in rows if student["credits"]>=min_credits]
    elif not min_credits:
        return [student for student in rows if student["school"]==school]
    else:
        return [student for student in rows if student["school"]==school and student["credits"]>=min_credits]


# Challenge 4 (optional): Persist to disk as TSV using the csv module
# TODO
import csv
with open('names.tsv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['id', 'name','school','credits']
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    writer.writerows(students)
