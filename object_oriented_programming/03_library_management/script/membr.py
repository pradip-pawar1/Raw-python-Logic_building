
class Members():
    '''Account handels all account related tasks'''
    def __init__(self, name, age, email, acc_pin, account_no, book_holds=0):
        self.name = name
        self.age = age
        self.email = email
        self.pin = acc_pin
        self.account_no = account_no
        self.book_holds = book_holds
    

    def to_dict(self):
        """Convert account to dictionary for JSON storage"""
        return {
            "Name": self.name,
            "Age": self.age,
            "Email": self.email,
            "Pin": self.pin,
            "AccountNo": self.account_no,
            "Book_holds": self.book_holds
        }