import json
import string
import random
from pathlib import Path

class Utils:
    """Utility class for code reusability"""

    def get_account(self) -> tuple[int, int]:
        """Get account method """
        acc_no = int(input("Enter 9 digit account no.: "))
        pin = int(input("Enter 4 digit pin: "))
        return acc_no, pin
    
    def get_userdata(self, accountNo:int, pin: int) -> list:
        self.acc_no = accountNo
        self.pin = pin

        userdata = [i for i in Bank.data if i["AccountNo"] == self.acc_no and i["Pin"]==self.pin]
        return userdata[0]


class Bank:
    """Class Bank handels things like:
    1. Load accounts
    2. Save accounts
    3. Create new account
    4. Find a specific account
    5. Deleting an account
    6. store the list of account
    7. Handel database"""

    database = 'object_oriented_programming/01_bank_management/data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("No database found..!")
    except Exception as err:
        print(f"An error occured as {err}")

        
    @classmethod
    def update(self):
        with open(Bank.database, 'w') as fs:
            json.dump(Bank.data, fs, indent=4)


    def create_account(self, name:str, age:int, email:str, pin:int)->dict:
        """Method takes name, age, email, pin & create new account. 
        Make sure the Pin should only conatin 4 digits."""

        info = {
            "Name": name,
            "Age":age,
            "Email":email,
            "Pin": pin,
            "AccountNo":random.randint(100000000, 999999999),
            "Balance": 0
        }

        if info['Age'] <18 or len(str(info['Pin'])) != 4:
            print("Sorry, you are not valid cadidate!")
        else:
            for i in info:
                print(f"{i} : {info[i]}")

            self.data.append(info)
            Bank.update()
            print("\nAccount created successfully")
            print("Please note your Account No.")
            

    def showDetails(self):
        """Show details returns a dict of details of user"""

        acc_no, Pin = utility.get_account()
        user = utility.get_userdata(accountNo=acc_no, pin=Pin)
        print("Your details\n")

        for i in user:
            print(f"{i} -> {user[i]}")
        print("\n")


class Account:
    """
    Docstring for Account
    """
    def depositMoney(self):
        """This function `depositMoney` added the amount in the users account."""
        acc_no, pin = utility.get_account()
        userdata = utility.get_userdata(accountNo=acc_no, pin=pin)

        if not userdata:
            print("No data found!")
        else:
            amount = int(input("Enter the deposit amount: "))
            if amount > 50000 or amount < 0:
                print("Amount should be <50000 and >0")

            else:
                userdata["Balance"] += amount
                Bank.update() # <- Calling @classmethod 
                print("Amount deposit succesfully...")

    def witheawlMoney(self):
        """The `withrawlMoney` function withrawls the selected amount for the users account."""
        acc_no, pin = utility.get_account()
        userdata = utility.get_userdata(accountNo=acc_no, pin=pin)

        # print(userdata)
        if not userdata:
            print("No data found!")
        else:
            amount = int(input("Enter the amount: "))
            if amount > userdata["Balance"]:
                print("You don't have enough balance!")
            else:
                userdata["Balance"] -= amount
                Bank.update()
                print("Amount withrawed Succesfully.")

    def updateInfo(self):
        """Only 3 things can be updated:
        1. Name
        2. Email
        3. Pin"""
        
        acc_no, pin = utility.get_account()
        user = utility.get_userdata(accountNo=acc_no, pin=pin)

        if not user:
            print("No data found!")
        else:
            print(f"You cannot change \n1. Age \n2.Account No. \n3. Balance")
            print("Fill the detail to change else leave it empty.")

            newdata = {
                "Name": input("Enter new name: "),
                "Email": input("Enter new email: "),
                "Pin": input("Enter the pin: ")
            }
            
            if newdata["Name"] == "":
                newdata["Name"] == user["Name"]
            if newdata["Email"] == "":
                newdata["Email"] == user["Email"]
            if newdata["Pin"] == "":
                newdata["Pin"] == user["Pin"]

            newdata["Age"] = user["Age"]
            newdata["Balance"] = user["Balance"]
            newdata["AccountNo"] = user["AccountNo"]

            if isinstance(newdata["Pin"], str):
                newdata["Pin"] = int(newdata["Pin"])

            # if type(newdata["Pin"]) == str:
            #     newdata["Pin"] == int(newdata["Pin"])

            for i in newdata:
                if newdata[i] == user[i]:
                    continue
                else:
                    user[i] = newdata[i]

            Bank.update()
            print("Details updated succesfully.")
            print("You can check it\n")


class Banking_system:
    """
    Docstring for Banking_system, which handels the Interaction + menu
    + main loop
    """

    def stop(self):
        raise SystemExit("Thanks, visit again!")

    menu = {
            1: "Create Account",
            2: "Deposit money",
            3: "Withraw money",
            4: "View details",
            5: "Update details",
            6: "Delete account",
            7: "Stop Runnig"
        }

    
    def run(self):
        """Main program loop which don't stop program execution until user wants"""
        while True:
            for i in self.menu:
                print(f"{i} : {self.menu[i]}")

            choice = int(input("Enter your choise: "))
            
            if choice == 1:
                name = input("Enter the name: ")
                age = int(input("Enter the age: "))
                email = input("Enter the email: ")
                pin = int(input("Enter teh pin: "))
                
                bank.create_account(name=name, age=age, email=email, pin=pin)

            if choice == 2:
                account.depositMoney()

            if choice == 3:
                account.witheawlMoney()

            if choice == 4:
                bank.showDetails()

            if choice == 5:
                account.updateInfo()

            if choice == 7:
                start.stop()




start = Banking_system()
bank = Bank()
account = Account()
utility = Utils()

start.run()