from pathlib import Path
import json

class Database:
    '''Handels all data, save, and access'''
    def __init__(self, database_path):
        self.database = database_path
        self.accounts = []


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
                            item["AccountNo"],
                            item['Books_holds']
                            )
                        self.accounts.append(acc)
                print(f"Loaded {len(self.accounts)} accounts")
            else:
                print("No database found. Starting fresh.")
        except Exception as err:
            print(f"Error loading accounts: {err}")
    

class Members():
    '''Account handels all account related tasks'''
    def __init__(self, name, age, email, acc_pin, account_no, book_holds):
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

class Member:
    # Represents a library member
    pass

class Library:
    # Manages books and members
    # Has methods: add_book, register_member, borrow_book, return_book
    pass

class LibrarySystem:
    '''UI and menu'''
    def run(self):
        """Main program loop"""
        while True:
            self.show_menu()


    pass

if __name__ == "__main__":
    data = Database('object_oriented_programming/02_vehicle_management/accounts.json')

    system = LibrarySystem(data)
    # bank = Book("Hello world", "Pradip", "ISBN2345")
    # bank.show_info()