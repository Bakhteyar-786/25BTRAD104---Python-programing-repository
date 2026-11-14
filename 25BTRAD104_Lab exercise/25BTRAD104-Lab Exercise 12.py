# LAB 12: STUDENT DATA MANAGER USING FILES
# Each line of students.txt:  roll,name,department,marks
FILE = "students.txt"


def load():
    students = []
    try:
        with open(FILE, "r") as f:
            for line in f:
                if line.strip() != "":
                    students.append(line.strip().split(","))
    except FileNotFoundError:
        pass
    return students


def save(students):
    with open(FILE, "w") as f:
        for s in students:
            f.write(",".join(s) + "\n")


def get_details():
    """Ask for name, department, marks. Returns None if input is invalid."""
    name = input("Name: ").strip()
    dept = input("Department: ").strip()
    if name == "" or dept == "" or "," in name or "," in dept:
        print("Name and department must not be empty or contain commas.")
        return None
    try:
        marks = float(input("Marks (0-100): "))
    except ValueError:
        print("Marks must be a number.")
        return None
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        return None
    return [name, dept, str(marks)]


while True:
    print("\n--- STUDENT DATA MANAGER ---")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search student")
    print("4. Update student")
    print("0. Exit")
    choice = input("Enter choice: ").strip()
    students = load()

    if choice == "1":
        roll = input("Roll number: ").strip()
        if not roll.isdigit():
            print("Roll number must be digits only.")
        elif any(s[0] == roll for s in students):
            print("Roll number already exists.")
        else:
            details = get_details()
            if details is not None:
                students.append([roll] + details)
                save(students)
                print("Student saved.")

    elif choice == "2":
        if len(students) == 0:
            print("No records found.")
        for s in students:
            print("Roll:", s[0], "| Name:", s[1], "| Dept:", s[2], "| Marks:", s[3])

    elif choice == "3":
        text = input("Enter roll number or name: ").strip().lower()
        found = False
        for s in students:
            if text == s[0] or (text != "" and text in s[1].lower()):
                print("Found -> Roll:", s[0], "| Name:", s[1], "| Dept:", s[2], "| Marks:", s[3])
                found = True
        if not found:
            print("No matching student.")

    elif choice == "4":
        roll = input("Roll number to update: ").strip()
        for s in students:
            if s[0] == roll:
                details = get_details()
                if details is not None:
                    s[1], s[2], s[3] = details
                    save(students)
                    print("Record updated.")
                break
        else:
            print("Student not found.")

    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")        