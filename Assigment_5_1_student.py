""" Student marks"""

students = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "David": 88
}
name = input("Enter the student's name: ")
try:
    if name in students:
        print(f"{name}'s marks: {students[name]}")
    else:
        print("Student's name not found in the records.")
except KeyError:
    print("Student's name not found in the records.")