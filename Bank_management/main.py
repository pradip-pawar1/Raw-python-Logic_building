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

    def withrawlMoney(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["AccountNo."]== accnumber and i["Pin"]==pin]

        if userdata == False:
            print("Sorry no data found!")
        else:
            amount = int(input("Enter the deposit amount: "))
            if amount > userdata[0]["Balance"]:
                print("Sorry, you don't have enough balance!")

            else:
                # print(userdata)
                userdata[0]["Balance"] -= amount
                Bank.__update()
                print("Amount withrawed sucessfully.")


    def showdetails(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["AccountNo."]== accnumber and i["Pin"]==pin]
        print("\nYour information is\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updateinfo(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["AccountNo."]== accnumber and i["Pin"]==pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            print(f"You cannot change \n1. Age \n2.Account No. \n3. Balance")
            print("Fill the detail for change else leave it empty.")

            newdata = {
                "Name": input("Enter new name or enter to skip: "),
                "Email": input("Enter the new email or enter to skip: "),
                "Pin": input("Enter new pin or enter to skip: ")
            }

            if newdata["Name"] == "":
                newdata["Name"] = userdata[0]['Name']
            if newdata["Email"] == "":
                newdata["Email"] = userdata[0]['Email']
            if newdata["Pin"] == "":
                newdata["Pin"] = userdata[0]['Pin']

            newdata["Age"] = userdata[0]["Age"]
            newdata["Balance"] = userdata[0]["Balance"]
            newdata["AccountNo."] = userdata[0]["AccountNo."]

            if type(newdata["Pin"]) == str:
                newdata["Pin"] == int(newdata["Pin"])
            
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details updated succesfully")

    def delete(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter the pin: "))

        userdata = [i for i in Bank.data if i["AccountNo."]== accnumber and i["Pin"]==pin]

        if userdata == False:
            print("No data found")
        else:
            check = input("Enter y if you want to delete, else n for not deleting: ")
            if check == 'n' or check == 'N':
                print("By-passed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account delete succesfully...")
                Bank.__update()




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

if check == 2:
    user.depositMoney()

if check == 3:
    user.withrawlMoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updateinfo()

if check == 6:
    user.delete()