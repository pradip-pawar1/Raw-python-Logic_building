from pathlib import Path
from library import Library

class LibrarySystem:
    '''UI and menu'''
    def __init__(self, data):
        self.data = data
        self.menu = {
            1: "Add new member",
            2: "Remove member",
            3: "Show all books",
            5: "Stop"
        }

    def show_menu(self):
        """Display menu options"""
        print("\n" + "="*30)
        print("    LIBRARY MANAGEMENT SYSTEM")
        print("="*30)
        for key, value in self.menu.items():
            print(f"{key}. {value}")
        print("="*30)

    def add_member_flow(self):
        '''Handle account creation'''
        print("\n--- Add member ---")
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            pin = int(input("Enter 4 digit pin no.: "))

            data.add_member(name, age, email, pin)

        except ValueError:
            print("Invalid input. Try again!")

    
    def remove_member_flow(self):
        '''Handels account deletion'''

        print("\n--- Delete Member ---")
        try:
            account_no = int(input("Enter account no: "))
            pin = int(input("Enter pin: "))

            if account_no or pin is None:
                return
        except ValueError:
            print("Invalid input. Try again")
            
            account = library_method.find_account(account_no, pin)

            if not account:
                print("Account not found or wrong PIN")
                return
            
            confirm = input("Are you sure you want to delete this account? (Y/N): ")
            if confirm.upper() == 'Y':
                if library_method.remove_member(account_no, pin):
                    print("Account deleted successfully")
                else:
                    print("Failed to delete account")
            else:
                print("Deletion cancelled")


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
                self.remove_member_flow()
                
            elif choice == 5:
                print("Thanks")
                break


if __name__ == "__main__":
    # Providing path to Library
    data = Library('object_oriented_programming/03_library_management/data/accounts.json')

    # Handling methods of Library class
    library_method = 
    
    system = LibrarySystem(data)

    # Running main program loop 
    system.run()