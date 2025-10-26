import json
import string
import random
from pathlib import Path


class Bank:
    database = 'Bank_management/data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No database found..!")
    except Exception as err:
        print(f"An error occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k= 3)
        nums = random.choices(string.digits, k= 3)
        spchar = random.choices("!@#$%&*", k= 1)
        id = alpha + nums + spchar
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        print("\n\nPlease provide your info: ")
        info = {
            "Name": input("Enter your name: "),
            "Age": int(input("Enter your age: ")),
            "Email": input("Enter Your Email: "),
            "Pin": int(input("Enter you pin (4 digit): ")),
            "AccountNo.": Bank.__accountgenerate(),
            "Balance": 0
        }
        
        if info['Age'] < 18 or len(str(info["Pin"])) != 4:
            print("Sorry, you are not elegible!")
        else:
            for i in info:
                print(f"{i} : {info[i]}")
            print("\nAccount created successfully")
            print("Please note your Account No.")

            Bank.data.append(info)
            Bank.__update()

    def depositMoney(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["AccountNo."]== accnumber and i["Pin"]==pin]

        if userdata == False:
            print("Sorry no data found!")
        else:
            amount = int(input("Enter the deposit amount: "))
            if amount > 10000 or amount < 0:
                print("Sorry, amount shoube < 10000 and > 0")

            else:
                # print(userdata)
                userdata[0]["Balance"] += amount
                Bank.__update()
                print("Amount deposited sucessfully.")

user = Bank()

print("Press 1: Create Account")
print("Press 2: Deposit money")
print("Press 3: Withraw money")
print("Press 4: View details")
print("Press 5: Update details")
print("Press 6: Delete account")

try:
    check = int(input("Enter your choise: "))
except ValueError as err:
    print("Please enter correct option: ")


if check == 1:
    user.createaccount()

elif check == 2:
    user.depositMoney()
