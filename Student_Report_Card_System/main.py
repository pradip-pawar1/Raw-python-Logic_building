from pathlib import Path
import string
import json

database = "Student_Report_Card_System/data.json"
data = {}

try:
    if Path(database).exists():
        with open(database, "r") as fs:
            data = json.load(fs)
            # print(data)
    else:
        print("No database found!")
except Exception as err:
    print(f"Error occured as {err}")

def update():
    with open(database, 'w') as fs:
        json.dump(data, fs, indent=4)
