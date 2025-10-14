print(f"Welcome to Library System 📚\n")

books = {
    "Data Science": 2,
    "Rich dad poor dad": 3,
    "48 Laws of power": 2,
    "Insta star": 1
}

def view_books(books):
    print(books)

def borrow_books():
    pass

def return_book():
    pass

def exit():
    raise SystemExit("System closed..!")

def login(users, username):
    return_key = False
    for i in range(len(users)):
        # print(i)
        if username == users[i]:
            print(f"User verified!")
            return_key = True
            break
    else:
        print(f"User not verified.")
    return return_key

def show_details(login_key):
    if login_key == True:
        print(f"1. View avaliable Books")
        print(f"2. Borrow Book")
        print(f"3. Return Book")
        print(f"4. Exit\n")
    else:
        print("User is new or not verified!")
        exit()

users = ["Pradip", "Rahul", "Rohit", "Rani", "Ram", "Sita"]
user_name = input("Enter your username: ")
key = login(users=users, username=user_name)

show_details(key)

choise = int(input("Enter your choise: "))

while True:
    match choise:
        case 1:
            view_books(books= books)
        case 2:
            borrow_books()
        case 3:
            return_book()
        case 4:
            exit()