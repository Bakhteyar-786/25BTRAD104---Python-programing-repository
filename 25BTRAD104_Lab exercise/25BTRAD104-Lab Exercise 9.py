# Student Grading System using a dictionary (name -> marks)
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks (0-100): "))
    students[name] = marks

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

print("\n--- Results ---")
for name, marks in students.items():
    print(name, "-", marks, "-", get_grade(marks))