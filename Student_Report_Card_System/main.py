from pathlib import Path
import json

database = "Student_Report_Card_System/data.json"
data = [] # Creating dummy data for using deep copy

try:
    if Path(database).exists(): # Checking path exists or not
        with open(database, "r") as fs:
            data = json.load(fs)
    else:
        print("No database found!")
except Exception as err:
    print(f"Error occured as {err}")

def updateInfo():
    with open(database, 'w') as fs:
        json.dump(data, fs, indent=2) # loding dummy data into data.json file

def add_record():
    # taking inputs
    name = input("\nEnter full name: ")
    roll_no = int(input("Enter roll no.: "))
    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))

    # calculating total, percentage, and grade
    total = maths + science + english
    percentage = total/3
    grade = "F"
    if percentage >= 80:
        grade = "A"
    elif percentage >=65:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = grade

    studentInfo = {
        "Student Name": name,
        "Roll No.": roll_no,
        "Marks":{
            "Maths":maths,
            "Science": science,
            "English": english
        },
        "Total Marks": total,
        "Percentage": percentage,
        "Grade": grade
    }

    data.append(studentInfo)
    updateInfo()
    print(f"\n\nYour record updated succesfully!")

def remove_record(name:str, roll:int):
    student_data = [i for i in data if i["Student Name"]== name and i["Roll No."]==roll]
    check = input("\nPress Y for delete records else Press N: ")

    if check == "n" or check == "N":
        print("By-passed..!")
    else:
        idx = data.index(student_data[0])
        data.pop(idx)
        updateInfo()

        print("\nYour record deleted succesfully..!")
    
def searchStudent(name:str, roll:int):
    student_data = [i for i in data if i['Student Name']==name and i['Roll No.']== roll]
    print("Your data is: \n")
    for i in student_data[0]:
        print(f"{i} : {student_data[0][i]}")


def exit():
    check = input("Press Y to exit... ")
    if check == "Y" or "y":
        raise SystemExit("Thanks for choosing us..!")


while True:
    print(f"Press 1: Add student records")
    print(f"Press 2: Remove student records")
    print(f"Press 3: Search student")
    print(f"Press 4: Exit\n")

    try:
        check = int(input("\nEnter your choise: "))
    except ValueError:
        print("Please enter corrct option: ")

    if check == 1:
        add_record()

    if check == 2:
        name = input("\nEnter your name: ")
        roll_no = int(input("Enter your roll no.: "))
        remove_record(name=name, roll=roll_no)

    if check == 3:
        name = input("\nEnter your name: ")
        roll_no = int(input("Enter your roll no.: "))
        searchStudent(name=name, roll=roll_no)

    if check == 4:
        exit()