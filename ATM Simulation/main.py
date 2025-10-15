def check_balance(deposit = 0, withraw = 0):
    global card_balance   
    card_balance += deposit
    card_balance -= withraw
    return card_balance

def deposit_money(deposit):
    added_mondy = deposit
    check_balance(deposit=added_mondy)
    print(f"\nYour {deposit} RS is added...")

def withraw_money(amount):
    if amount > card_balance:
        print("\nInsufficient Balance!")
        exit(login_key=False)
    else:
        check_balance(withraw=amount)
    print(f"\nYou withrew: {amount} RS...")

def exit(login_key):
        if login_key == False:
            raise SystemExit("System closed!")

def login(card_pin):
    attempts = 0

    while attempts < 3:
        enterd_pin = int(input("Enter the pin: "))
        if enterd_pin == card_pin:
            login_key = True
            return login_key
        else:
            attempts += 1
            print("Incorrect PIN! Try again\n")
    return False

card_pin = 1234
card_balance = 5000
login_access = login(card_pin=card_pin)

while True:
    if login_access == True:
        print(f"Choose 1: Check Balance")
        print(f"Choose 2: Deposit Money")
        print(f"Choose 3: Withdraw Money")
        print(f"Choose 4: Exit")
    else:
        print("Card Blocked!")
        exit(login_key=login_access)

    operation = int(input("\nEnter Your choise: "))

    match operation:
        case 1:
            print(f"\nYour current balance is: {check_balance()} RS...\n")
        case 2:
            deposit = int(input("\nEnter amount: "))
            deposit_money(deposit=deposit)
        case 3:
            amount = int(input("Enter amount: "))
            withraw_money(amount=amount)
        case 4:
            login_key = False
            exit(login_key)