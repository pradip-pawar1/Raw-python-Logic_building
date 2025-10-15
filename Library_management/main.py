print(f"Welcome to Library System 📚\n")

data = {
    "Data Science": 2,
    "Rich dad poor dad": 3,
    "48 Laws of power": 2,
    "Insta star": 1
}


def view_books(books):
    for i in books:
        print(f"{i}: {books[i]}")

def borrow_books(bookList):
    for i in bookList:
        print(f"{i} : {bookList[i]}")

    user_pick = input("Enter the book you want: ")

    for i in bookList:
        if user_pick == i:
            bookList[i] -= 1
            print("Book Issued..!")
            break
     
    return bookList 

def return_book(bookList):
    for i in bookList:
        print(f"{i} : {bookList[i]}")

    user_return = input("Enter book name: ")

    for i in bookList:
        if user_return == i:
            bookList[i] += 1
            print("Succesfully returned..!")
            break
    return bookList

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
    

users = ["Pradip", "Rahul", "Rohit", "Rani", "Ram", "Sita"]
user_name = input("Enter your username: ")
key = login(users=users, username=user_name)


while True:
    if key == True:
        print(f"\n1. View avaliable Books")
        print(f"2. Borrow Book")
        print(f"3. Return Book")
        print(f"4. Exit\n")
    else:
        print("User is new or not verified!")
        exit()

    choise = int(input("Enter your choise: "))


    match choise:
        case 1:
            view_books(books= data)
        case 2:
            borrow_books(bookList=data)
        case 3:
            return_book(bookList= data)
        case 4:
            exit()