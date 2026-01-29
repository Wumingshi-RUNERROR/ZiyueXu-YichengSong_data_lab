"""Part 3: Tuples as Records
A tuple is immutable. In databases, 'tuple' can also mean a row/record.
"""

students = [
    (1, "Alice", "GSAS", 32),
    (2, "Bob", "Tandon", 28),
    (3, "Carol", "GSAS", 40)
]
# columns: (id, name, school, credits)

# TODO 1: Print the name for each record
for i in students:
    print(i[1])
# TODO 2: Try to change Bob’s credits directly (observe the error)
# for i in students:
#     if i[1]=='Bob':
#         i[-1]=1
#         break
# TODO 3: Create a new tuple for Bob with credits=30 and replace the old record in the list
students[1]=(2, "Bob", "Tandon", 30)
# Reflection (answer in a comment): Reminded me that tuple has index as well
# TODO: Why might immutability be good for data integrity?
# For protection
