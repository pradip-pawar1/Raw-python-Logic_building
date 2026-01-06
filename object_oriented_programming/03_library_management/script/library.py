from pathlib import Path
import json
import random
from membr import Members


class Library:
    '''
    Manages books and members also database.
    Has methods: `add_book`, `register_member`, `borrow_book`, `return_book`
    '''

    def __init__(self, database_path:str):
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
                            item["Pin"],           
                            item["AccountNo"],     
                            item['Book_holds']
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

    def find_account(self, account_no:int, pin:int):
        """Find account by account number and pin"""
        for account in self.accounts:
            if account.account_no == account_no and account.pin == pin:
                print(account)
                return account
        return None

    def remove_member(self, account_no:int, pin:int):
        '''Removes the existent member form database with canceling the membership,
        of the person.'''
        account = self.find_account(account_no, pin)
        if account:
            self.accounts.remove(account)
            self.save_accounts()
            return True
        return False
    

obj = Library('object_oriented_programming/03_library_management/data/accounts.json')
obj.find_account(91917, 1234)