from pathlib import Path
import json
import random


class Book:
    '''Parent class for all books'''
    # Base class for all books
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def get_borrow_days(self):
        return 14  # Default
    
    def show_info(self):
        '''Shows details of the book'''
        print(f"The book is : {self.title}")
        print(f"And author of the book is :{self.author} with ISBN :{self.isbn}")
    

class FictionBook(Book):
    # Inherits from Book
    pass

class TextBook(Book):
    # Inherits from Book
    pass

class Magazine(Book):
    # Inherits from Book
    pass

# ------------------------------ || -------------------------------
class Library:
    '''
    Manages books and members also database.
    Has methods: `add_book`, `register_member`, `borrow_book`, `return_book`
    '''

    def __init__(self, database_path):
        self.database = database_path
        self.accounts = []
        self.load_accounts()


    def load_accounts(self):
        '''Load accounts from JSON and convert to Account objects'''
        try:
            if Path(self.database).exists():
                with open(self.database) as f:
                    data = json.load(f)

                    for item in data:
                        acc = Members(
                            item['Name'],
                            item['Age'],
                            item["Email"],
                            item["Pin"],           # ✅ PIN is 4th
                            item["AccountNo"],     # ✅ Account number is 5th
                            item['Book_holds']    # ✅ Book_holds is 6th
                        )
                        self.accounts.append(acc)
                print(f"Loaded {len(self.accounts)} accounts")
            else:
                print("No database found. Starting fresh.")
        except Exception as err:
            print(f"Error loading accounts: {err}")

    
    def save_accounts(self):
        """Save all Account objects to JSON"""
        try:
            data = [account.to_dict() for account in self.accounts]
            with open(self.database, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as err:
            print(f"Error saving accounts: {err}")

    def add_member(self, name:str, age:int, email:str, pin:int):
        """Creates new account and adds new member to the library"""
        # Validation
        if age < 10:
            print("Sorry, you must be 10 or older.")
            return None
        
        if len(str(pin)) != 4:
            print("Pin must be exactly 4 digits.")
            return None

        # unique 6 digit account number 
        account_no = random.randint(11111, 99999)

        # create new account
        new_account = Members(name, age, email, pin, account_no, 0)

        # Add account to list 
        self.accounts.append(new_account)

        # Save account to file
        self.save_accounts()

        print("\nMember registered successfully!")
        print(f"Name: {name}")
        print(f"Account Number: {account_no}")
        print("Please note your account number for future use.")
# ------------------------------ || -------------------------------


class Members():
    '''Account handels all account related tasks'''
    def __init__(self, name, age, email, acc_pin, account_no, book_holds=0):
        self.name = name
        self.age = age
        self.email = email
        self.pin = acc_pin
        self.account_no = account_no
        self.book_holds = book_holds
    

    def to_dict(self):
        """Convert account to dictionary for JSON storage"""
        return {
            "Name": self.name,
            "Age": self.age,
            "Email": self.email,
            "Pin": self.pin,
            "AccountNo": self.account_no,
            "Book_holds": self.book_holds
        }
    
# ------------------------------ || -------------------------------

class LibrarySystem:
    '''UI and menu'''

    def __init__(self, data):
        self.data = data
        self.menu = {
            1: "Add new member",
            2: "Remove the member"
        }

    def show_menu(self):
        """Display menu options"""
        print("\n" + "="*40)
        print("    LIBRARY MANAGEMENT SYSTEM")
        print("="*40)
        for key, value in self.menu.items():
            print(f"{key}. {value}")
        print("="*40)

    def add_member_flow(self):
        '''Handle account creation'''
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            pin = int(input("Enter 4 digit pin no.: "))

            data.add_member(name, age, email, pin)

        except ValueError:
            print("Invalid input. Try again!")


    def run(self):
        """Main program loop"""
        while True:
            self.show_menu()

            try:
                choice = int(input("Enter your choice: "))
            except ValueError as err:
                print("Invalid input. Try again...")
                continue

            if choice == 1:
                self.add_member_flow()
            elif choice == 2:
                print("Thanks")
                break


if __name__ == "__main__":
    data = Library('object_oriented_programming/03_library_management/accounts.json')

    system = LibrarySystem(data)

    system.run()