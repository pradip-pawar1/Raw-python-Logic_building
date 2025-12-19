import json
import random
from pathlib import Path

# ------------------------------ || -------------------------------
class Account:
    """Represents ONE bank account with its data and operations"""
    
    def __init__(self, name, age, email, pin, account_no, balance=0):
        self.name = name
        self.age = age
        self.email = email
        self.pin = pin
        self.account_no = account_no
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to this account"""
        if amount <= 0 or amount > 50000:
            return False
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        """Remove money from this account"""
        if amount > self.balance or amount <= 0:
            return False
        self.balance -= amount
        return True
    
    def get_details(self):
        """Return account details as dictionary (without pin for security)"""
        return {
            "Name": self.name,
            "Age": self.age,
            "Email": self.email,
            "Account Number": self.account_no,
            "Balance": self.balance
        }
    
    def to_dict(self):
        """Convert account to dictionary for JSON storage"""
        return {
            "Name": self.name,
            "Age": self.age,
            "Email": self.email,
            "Pin": self.pin,
            "AccountNo": self.account_no,
            "Balance": self.balance
        }
    
    def update_info(self, name=None, email=None, pin=None):
        """Update account information"""
        if name:
            self.name = name
        if email:
            self.email = email
        if pin and len(str(pin)) == 4:
            self.pin = pin


# ------------------------------ || -------------------------------
class Bank:
    """Manages all accounts and database operations"""
    
    def __init__(self, database_path):
        self.database = database_path
        self.accounts = []
        self.load_accounts()
    
    def load_accounts(self):
        """Load accounts from JSON and convert to Account objects"""
        try:
            if Path(self.database).exists():
                with open(self.database) as f:
                    data = json.load(f)
                    for item in data:
                        acc = Account(
                            item["Name"],
                            item["Age"],
                            item["Email"],
                            item["Pin"],
                            item["AccountNo"],
                            item["Balance"]
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
    
    def create_account(self, name, age, email, pin):
        """Create new account and add to bank"""
        # Validation
        if age < 18:
            print("Sorry, you must be 18 or older.")
            return None
        
        if len(str(pin)) != 4:
            print("Pin must be exactly 4 digits.")
            return None
        
        # Generate unique account number
        account_no = random.randint(100000000, 999999999)
        
        # Create Account object
        new_account = Account(name, age, email, pin, account_no, 0)
        
        # Add to list
        self.accounts.append(new_account)
        
        # Save to file
        self.save_accounts()
        
        print("\nAccount created successfully")
        print(f"Name: {name}")
        print(f"Account Number: {account_no}")
        print("Please note your account number")
        
        return new_account
    
    def find_account(self, account_no, pin):
        """Find account by account number and pin"""
        for account in self.accounts:
            if account.account_no == account_no and account.pin == pin:
                return account
        return None
    
    def delete_account(self, account_no, pin):
        """Delete an account"""
        account = self.find_account(account_no, pin)
        if account:
            self.accounts.remove(account)
            self.save_accounts()
            return True
        return False


# ------------------------------ || -------------------------------
class Banking_system:
    """Handles user interface and menu"""
    
    def __init__(self, bank):
        self.bank = bank
        self.menu = {
            1: "Create Account",
            2: "Deposit Money",
            3: "Withdraw Money",
            4: "View Details",
            5: "Update Info",
            6: "Delete Account",
            7: "Exit"
        }
    
    def get_account_credentials(self):
        """Get account number and pin from user"""
        try:
            account_no = int(input("Enter 9 digit account number: "))
            pin = int(input("Enter 4 digit pin: "))
            return account_no, pin
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return None, None
    
    def show_menu(self):
        """Display menu options"""
        print("\n" + "="*40)
        print("    BANK MANAGEMENT SYSTEM")
        print("="*40)
        for key, value in self.menu.items():
            print(f"{key}. {value}")
        print("="*40)
    
    def create_account_flow(self):
        """Handle account creation"""
        print("\n--- Create New Account ---")
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            pin = int(input("Enter 4 digit pin: "))
            
            self.bank.create_account(name, age, email, pin)
        except ValueError:
            print("Invalid input. Please try again.")
    
    def deposit_flow(self):
        """Handle deposit operation"""
        print("\n--- Deposit Money ---")
        account_no, pin = self.get_account_credentials()
        
        if account_no is None:
            return
        
        account = self.bank.find_account(account_no, pin)
        
        if not account:
            print("Account not found or wrong PIN")
            return
        
        try:
            amount = int(input("Enter amount to deposit: "))
            if account.deposit(amount):
                self.bank.save_accounts()
                print(f"Deposit successful! New balance: {account.balance}")
            else:
                print("Invalid amount. Must be between 1 and 50000")
        except ValueError:
            print("Invalid amount")
    
    def withdraw_flow(self):
        """Handle withdrawal operation"""
        print("\n--- Withdraw Money ---")
        account_no, pin = self.get_account_credentials()
        
        if account_no is None:
            return
        
        account = self.bank.find_account(account_no, pin)
        
        if not account:
            print("Account not found or wrong PIN")
            return
        
        try:
            amount = int(input("Enter amount to withdraw: "))
            if account.withdraw(amount):
                self.bank.save_accounts()
                print(f"Withdrawal successful! New balance: {account.balance}")
            else:
                print("Insufficient balance or invalid amount")
        except ValueError:
            print("Invalid amount")
    
    def view_details_flow(self):
        """Handle view details operation"""
        print("\n--- View Account Details ---")
        account_no, pin = self.get_account_credentials()
        
        if account_no is None:
            return
        
        account = self.bank.find_account(account_no, pin)
        
        if not account:
            print("Account not found or wrong PIN")
            return
        
        details = account.get_details()
        print("\nYour Account Details:")
        print("-" * 30)
        for key, value in details.items():
            print(f"{key}: {value}")
        print("-" * 30)
    
    def update_info_flow(self):
        """Handle update info operation"""
        print("\n--- Update Account Info ---")
        account_no, pin = self.get_account_credentials()
        
        if account_no is None:
            return
        
        account = self.bank.find_account(account_no, pin)
        
        if not account:
            print("Account not found or wrong PIN")
            return
        
        print("Leave blank to keep current value")
        name = input(f"Enter new name (current: {account.name}): ")
        email = input(f"Enter new email (current: {account.email}): ")
        new_pin = input("Enter new 4 digit pin: ")
        
        if new_pin:
            try:
                new_pin = int(new_pin)
            except ValueError:
                print("Invalid pin")
                return
        else:
            new_pin = None
        
        account.update_info(
            name if name else None,
            email if email else None,
            new_pin
        )
        
        self.bank.save_accounts()
        print("Account updated successfully")
    
    def delete_account_flow(self):
        """Handle account deletion"""
        print("\n--- Delete Account ---")
        account_no, pin = self.get_account_credentials()
        
        if account_no is None:
            return
        
        account = self.bank.find_account(account_no, pin)
        
        if not account:
            print("Account not found or wrong PIN")
            return
        
        confirm = input("Are you sure you want to delete this account? (Y/N): ")
        if confirm.upper() == 'Y':
            if self.bank.delete_account(account_no, pin):
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
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if choice == 1:
                self.create_account_flow()
            elif choice == 2:
                self.deposit_flow()
            elif choice == 3:
                self.withdraw_flow()
            elif choice == 4:
                self.view_details_flow()
            elif choice == 5:
                self.update_info_flow()
            elif choice == 6:
                self.delete_account_flow()
            elif choice == 7:
                print("\nThank you for using our bank. Visit again!")
                break
            else:
                print("Invalid choice. Please select 1-7")


# ------------------------------ || -------------------------------
if __name__ == "__main__":
    # Create Bank object (loads existing accounts from JSON)
    bank = Bank('object_oriented_programming/01_bank_management/data.json')
    
    # Create Banking System with the bank
    system = Banking_system(bank)
    
    # Run the system
    system.run()