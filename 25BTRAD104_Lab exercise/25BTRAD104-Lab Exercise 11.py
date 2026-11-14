# LAB 11: LOG FILE READER (sample log built in)

# Step 1: create the sample log file
sample_log = [
    "2026-11-10 09:00:01 INFO Application started",
    "2026-11-10 09:01:10 WARNING Disk usage at 85%",
    "2026-11-10 09:02:30 ERROR Database connection failed",
    "2026-11-10 09:02:40 INFO Database connection restored",
    "2026-11-10 09:05:12 WARNING Response time is slow",
    "2026-11-10 09:07:45 ERROR Payment service timeout",
    "2026-11-10 09:08:00 INFO User logout",
    "",
    "2026-11-10 09:10:00 DEBUG Cache cleared",
]
with open("app.log", "w") as file:
    for line in sample_log:
        file.write(line + "\n")
print("Sample log file 'app.log' created.")

# Step 2: read and analyze a log file
filename = input("Enter log file name (press Enter for app.log): ").strip()
if filename == "":
    filename = "app.log"

counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
total = 0

try:
    with open(filename, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error: file not found.")
else:
    for line in lines:
        if line.strip() == "":         # skip blank lines
            continue
        total = total + 1
        for keyword in counts:
            if keyword in line.upper():
                counts[keyword] = counts[keyword] + 1
                break                  # count each line only once

    if total == 0:
        print("The file is empty.")
    else:
        print("\nLOG SUMMARY")
        for keyword in counts:
            print(keyword, ":", counts[keyword])
        print("Other lines:", total - sum(counts.values()))
        print("Total lines:", total)
        if counts["ERROR"] > 0:
            print("Status: errors found - please check the log.")
            