# How to write and store data in a .csv file using input
import csv

name = input("what's your name? ")
home = input("what's your home? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) # When using Dictwriter you need give a hint order of columns
    writer.writerow({"name": name, "home": home})


# csv.DictReader is more powerful than csv.reader
# You can make changes in your .csv file and it won't break the code
"""
import csv

students = []

with open("students_home.csv", "r") as file: # If you are reading a file you don't need to specify "r"
    reader = csv.DictReader(file)
    for row in reader:
       students.append({"name": row["name"], "house": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']}")

# Student Dict. "name", "house"
"""


"""
students = []
with open("students.csv", "r") as file: # If you are reading a file you don't need to specify "r"
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)
"""


# To sort using a function
"""
def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
"""

# if you are defining a variable or function(as above) immediately using it but not needing it later,
# instead of passing in the key= the "name of function" use the lambda function(function with no name since we'll call it in one place)
# To sort using lambda
"""
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
"""