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
    def _update(cls):
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

        if info['Age'] <10:
            print("Sorry you are not eligible!")
            return 
        else:
            # Updating information to show
            new_info = {
                "Name":info['Name'],
                "Age":info["Age"],
                "Roll No":info["Roll No"]
            }

            print("Please verify your details!")

            # show info
            for key, value in new_info.items():
                print(f"{key} : {value}")

            # conformation of creation
            choice = input("Enter 'Y' if it's corrrect: ")
            if choice == 'Y'.lower():
                Student.data.append(info)
                Student._update()

                print("\nYou added in database 👍")
            else:
                print("System stoped. Try again...!")

    def find_student(self, name:str, roll_no:int) -> dict:
        '''Search student into database'''
        student = [i for i in self.data if i['Name']==name and i['Roll No']==roll_no]
        student = student[0]
        return student

class Marks:
    '''This class handels marks and grades related tasks'''
    def add_marks(self, 
                  name:str, 
                  roll_no:int, 
                  marks:dict):
        '''Method add marks of the students'''
        student = main.find_student(name, roll_no)

        if student is None:
            print("Student not found.")
            return
    
        # Update marks for each subject
        for grade in student["Grades"]:
            subject_name = grade["Subject"]
            if subject_name in marks:
                grade["Marks"] = marks[subject_name]
        
        # Recalculate average
        total_marks = sum(grade["Marks"] for grade in student["Grades"])
        student["Average"] = round(total_marks / len(student["Grades"]), 2)
        
        main._update()
        print(f"Marks updated successfully for {name}.")
        
    

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

    def student_credentials(self):
        '''Search a student from database'''
        print("\n--- Enter details ---")
        try:
            name = input("Enter name: ")
            roll_no = int(input("Enter roll No: "))
            return name, roll_no

        except Exception as err:
            print(f"Error occured as {err}")

    def show_menu(self):
        """Display menu options"""
        print("\n" + "="*30)
        print("    STUDENT GRADE SYSTEM")
        print("="*30 + "\n")
        for key, value in self.menu.items():
            print(f"{key}. {value}")
        print("-"*30+"\n")

    def create_account_flow(self):
        '''Handel account creation flow'''
        print("\n--- Add new student ---")
        try:
            name, roll_no = self.student_credentials()
            age = int(input("Enter age: "))

            if not name or not roll_no:
                print("Invalid info")
            else:
                main.add_student(name=name, roll_no= roll_no, age=age)

        except ValueError:
            print("Ivalid input. Try again")

    def add_marks_flow(self):
        '''Add marks of the student'''
        try:
            name, roll_no = self.student_credentials()
            marks = {
                "Mathematics": float(input("Maths marks (ex:87.90): ")),
                "Science": float(input("Science marks (ex:87.90): ")),
                "English": float(input("English marks (ex:87.90): ")),
                "History": float(input("History marks (Ex: 89.90): "))
            }

            mark_cls.add_marks(name, roll_no, marks)
        except Exception as err:
            print(f"Error occured as {err}")  

    def run(self):
        '''Main program loop'''

        while True:
            self.show_menu()

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("invalid choice try again: ")
                continue
            

            if choice > 6 or choice < 1:
                print("Out of range.\nSelect valid option...")
            
            elif choice == 1:
                self.create_account_flow()

            elif choice == 6:
                print("Thanks for choosing us..")
                break
            elif choice == 2:
                self.add_marks_flow()


if __name__ == '__main__':
    main = Student()
    mark_cls = Marks()
    system = Studentsystem()
    system.run()