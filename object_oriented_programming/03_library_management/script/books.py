class Book:
    '''Parent class for all books'''
    # Base class for all books
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def get_borrow_days(self):
        return 14  # Default
    
    def show_info(self):
        '''Shows details of the book'''
        print(f"The book is : {self.title}")
        print(f"And author of the book is :{self.author} with ISBN :{self.isbn}")



class FictionBook(Book):
    # Inherits from Book
    pass

class TextBook(Book):
    # Inherits from Book
    pass

class Magazine(Book):
    # Inherits from Book
    pass