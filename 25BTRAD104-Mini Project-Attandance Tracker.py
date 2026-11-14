# ATTENDANCE TRACKER
# Each student is a dictionary stored inside a list:
# {"name": "Buck", "attendance": ["P", "A", "P"]}    P = Present, A = Absent

students = []

while True:
    print("\n--- ATTENDANCE TRACKER ---")
    print("1. Add student")
    print("2. Mark attendance for a new day")
    print("3. Update an old attendance entry")
    print("4. Display all records")
    print("5. Show students below a threshold")
    print("6. Load sample data (for testing)")
    print("0. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip() #removes any extra spaces from start or end
        exists = False
        for s in students:
            if s["name"].lower() == name.lower(): #lowercases everything
                exists = True
        if name == "":
            print("Name cannot be empty.")
        elif exists:
            print("Student already exists.")
        else:
            students.append({"name": name, "attendance": []})
            print(name, "added.")

    elif choice == "2":
        name = input("Enter student name: ").strip()
        status = input("Enter status (P = Present, A = Absent): ").strip().upper() 
        found = False
        for s in students:
            if s["name"].lower() == name.lower():
                found = True
                if status == "P" or status == "A":
                    s["attendance"].append(status) #adds an element into the directory
                    print("Attendance recorded.")
                else:
                    print("Status must be P or A.")
        if not found:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter student name: ").strip()
        day = int(input("Enter day number to change (1 = first day): "))
        status = input("Enter new status (P/A): ").strip().upper()
        found = False
        for s in students:
            if s["name"].lower() == name.lower():
                found = True
                if day < 1 or day > len(s["attendance"]):
                    print("Day number is out of range.")
                elif status != "P" and status != "A":
                    print("Status must be P or A.")
                else:
                    s["attendance"][day - 1] = status
                    print("Attendance updated.")
        if not found:
            print("Student not found.")

    elif choice == "4":
        if len(students) == 0:
            print("No students added yet.")
        else:
            print("\nName | Attendance | Present/Total | Percentage")
            print("-" * 50)
            for s in students:
                total = len(s["attendance"])
                present = 0
                for day in s["attendance"]:
                    if day == "P":
                        present = present + 1
                if total > 0:
                    percent = present / total * 100
                else:
                    percent = 0.0
                print(s["name"], "|", " ".join(s["attendance"]), "|",
                      present, "/", total, "|", round(percent, 1), "%")

    elif choice == "5":
        threshold = float(input("Enter attendance threshold (%): "))
        print("Students below", threshold, "%:")
        count = 0
        for s in students:
            total = len(s["attendance"])
            present = 0
            for day in s["attendance"]:
                if day == "P":
                    present = present + 1
            if total > 0:
                percent = present / total * 100
            else:
                percent = 0.0
            if percent < threshold:
                print(" ", s["name"], "-", round(percent, 1), "%")
                count = count + 1
        if count == 0:
            print("  None")

    elif choice == "6":
        students = [
            {"name": "Buck",  "attendance": list("PPPPPPPP")},   # 100%
            {"name": "Vaishnavi", "attendance": list("PPPPPPAA")},   # 75%
            {"name": "Sushanth", "attendance": list("PAPAPAAA")},   # 37.5%
            {"name": "Rashmika", "attendance": list("AAAAAAAA")},   # 0%
            {"name": "David M", "attendance": []}                  # no records
        ]
        print("Sample data loaded.")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
