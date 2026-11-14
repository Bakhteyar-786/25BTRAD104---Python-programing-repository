# LAB 13: CSV-BASED PAYROLL SYSTEM (sample employee file built in)
# Rules: HRA = 20% of basic, DA = 10% of basic, Gross = Basic + HRA + DA
#        PF = 12% of basic, Tax = 5% of gross, Net = Gross - PF - Tax
import csv

# Step 1: create the sample employee file
sample_rows = [
    ["emp_id", "name", "department", "basic_salary"],
    ["101", "Bakhteyar", "IT", "30000"],
    ["102", "Vaishnavi", "HR", "45000"],
    ["103", "Sushanth", "Finance", "60000"],
    ["104", "Rashmika", "IT", "abc"],       # invalid salary (for testing)
    ["105", "David M", "HR", "-5000"],      # negative salary (for testing)
    ["106", "", "IT", "25000"],             # missing name (for testing)
]
with open("employees.csv", "w", newline="") as f:
    csv.writer(f).writerows(sample_rows)
print("Sample file 'employees.csv' created.")

# Step 2: read and process an employee file
filename = input("Enter CSV file name (press Enter for employees.csv): ").strip()
if filename == "":
    filename = "employees.csv"

try:
    with open(filename, "r") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    print("Error: file not found.")
    rows = []

results = []
for row in rows:
    try:
        name = row["name"].strip()
        basic = float(row["basic_salary"])
        if name == "" or basic <= 0:
            raise ValueError
    except Exception:
        print("Skipped invalid row:", dict(row))
        continue

    gross = basic + basic * 0.20 + basic * 0.10
    deductions = basic * 0.12 + gross * 0.05
    net = gross - deductions
    results.append([row["emp_id"], name, row["department"], basic, gross, deductions, net])

if len(results) == 0:
    print("No valid employee records to process.")
else:
    print("\nID   Name      Dept      Basic      Gross      Deductions  Net")
    for r in results:
        print(f"{r[0]:<5}{r[1]:<10}{r[2]:<10}{r[3]:<11.2f}{r[4]:<11.2f}{r[5]:<12.2f}{r[6]:.2f}")

    print("\nSUMMARY")
    print("Employees paid :", len(results))
    print("Total gross    :", round(sum(r[4] for r in results), 2))
    print("Total deduction:", round(sum(r[5] for r in results), 2))
    print("Total net pay  :", round(sum(r[6] for r in results), 2))
    top = max(results, key=lambda r: r[6])
    print("Highest net pay:", top[1], "-", round(top[6], 2))

    with open("salary_summary.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["emp_id", "name", "department", "basic", "gross", "deductions", "net"])
        for r in results:
            writer.writerow([r[0], r[1], r[2], r[3], round(r[4], 2), round(r[5], 2), round(r[6], 2)])
    print("Saved to salary_summary.csv")