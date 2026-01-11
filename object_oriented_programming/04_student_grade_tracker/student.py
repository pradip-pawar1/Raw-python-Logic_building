import json
from pathlib import Path


class Student:
    database = 'object_oriented_programming/04_student_grade_tracker/data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as f:
                data = json.load(f)
        else:
            print("No data base found!")
    except Exception as err:
        print(f"Error occured as : {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as f:
            json.dump(cls.data, f, indent=4)

    def add_student(self, roll_no:int, name:str, age:int):
        '''Adds a new student into database'''
        info = {
        "Name": name,
        "Roll No": roll_no,
        "Age": age,
        "Grades": [
            {"Subject": "Mathematics", "Marks":0},
            {"Subject": "Science", "Marks":0},
            {"Subject": "English", "Marks":0},
            {"Subject": "History", "Marks":0}
        ],
        "Average": 0
        }

        # Now calculate and update
        total_marks = sum(subject["Marks"] for subject in info["Grades"])
        info["Average"] = total_marks / len(info["Grades"])

        if info['Age'] <10:
            print("Sorry you are not eligible!")
            return 
        else:
            print("Please verify your details!")
            for key, value in info.items():
                print(f"{key} : {value}")

            choice = input("Enter 'Y' if it's corrrect: ")
            if choice == 'Y'.capitalize():
                Student.data.append(info)
                Student.__update()

                print("\nYou added in database 👍")
            else:
                print("System stoped. Try again...!")



class Studentsystem:
    '''Handel UI and menu of the system.'''
    def __init__(self):
        self.menu = {
            1: "Add student",
            2: "Add Grade to Student",
            3: "View Student Details",
            4: "View All Students",
            5: "Delete Student",
            6: "Stop loop"
        }

    def show_menu(self):
        """Display menu options"""
        print("\n" + "="*30)
        print("    STUDENT GRADE SYSTEM")
        print("="*30)
        for key, value in self.menu.items():
            print(f"{key}. {value}")
        print("-"*30)

    def create_account_flow(self):
        '''Handel account creation flow'''
        print("\n--- Add new student ---")
        try:
            name = input("Enter name: ")
            roll_no = int(input("Enter roll No: "))
            age = int(input("Enter age: "))

            main.add_student(name=name, roll_no= roll_no, age=age)

        except ValueError:
            print("Ivalid input. Try again")

        



    def run(self):
        '''Main program loop'''

        while True:
            self.show_menu()

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("invalid choice try again: ")
                continue
            

            if choice == 1:
                self.create_account_flow()

            elif choice == 6:
                print("Thanks for choosing us..")
                break


if __name__ == '__main__':
    main = Student()
    system = Studentsystem()
    system.run()