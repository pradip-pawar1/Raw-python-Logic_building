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

print(f"1. View avaliable Books")
print(f"2. Borrow Book")
print(f"3. Return Book")
print(f"4. Exit\n")

choise = int(input("Enter your choise: "))

match choise:
    case 1:
        view_books(books= books)
    case 2:
        borrow_books()
    case 3:
        return_book()
    case 4:
        exit()