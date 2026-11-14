# List of students and their scores in 3 internal assesment tests
students = {
    "Bakhteyar": [85, 90, 78],
    "Sushanth": [67, 88, 70],
    "Vaishnavi": [95, 92, 88],
    "Almer Eigenstein": [40, 50, 45]
}

# Now we process each student and calculate their average score and assign a grade based on that
for name, scores in students.items():
    average = sum(scores) / len(scores)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: Average = {average:.2f}, Grade = {grade}")
