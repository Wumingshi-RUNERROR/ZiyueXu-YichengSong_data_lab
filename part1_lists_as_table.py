"""Part 1: Lists as Tables
Each row is a list: [id, name, school, credits]
Schema is implicit — your code depends on correct indexes.
"""

students = [
    [1, "Alice", "GSAS", 32],
    [2, "Bob", "Tandon", 28],
    [3, "Carol", "GSAS", 40],
    [4, "Dan", "CAS", 18]
]
# columns: [id, name, school, credits]

# TODO 1: Print all student names (one per line)
for i in students:
    print(i[2])
# TODO 2: Print only the students in GSAS (id and name)
for i in students:
    if i[2]=="GSAS":
        print(i[0],i[1]) 
# TODO 3: Print students with credits > 30 (name and credits)
for i in students:
    if i[-1]>30:
        print(i[1],i[-1])
# TODO 4: Insert a new student row for: id=5, name='Eve', school='CAS', credits=22
students.append([5,"Eve","CAS",22])
# TODO 5: Update Bob’s credits to 30
for i in students:
    if i[1]=="Bob":
        i[-1]=30
# Reflection (answer in a comment): kinda easy for me..
# TODO: What breaks if we insert a new column at position 2?
# id
