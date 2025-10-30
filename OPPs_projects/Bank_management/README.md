# Bank Management System (OOP Project)

## Overview
The **Bank Management System** is a console-based Python project built using the **Object-Oriented Programming (OOP)** approach.  
It simulates a simple digital banking system that allows users to create accounts, deposit or withdraw money, view account details, update information, and delete accounts.

This is the **first OOP project** in the **Raw Python Logic-building** series, designed to shift from procedural thinking to structured, class-based design.

---

## Features
- Account creation with age and PIN verification  
- Unique account number generation  
- Deposit and withdrawal with balance checks  
- View full user details  
- Update account information (Name, Email, PIN)  
- Delete account with confirmation  
- Data persistence using JSON file (`data.json`)  

---

## Core Concepts Demonstrated

| Concept | How It’s Used |
|----------|----------------|
| **Class and Object** | `Bank` class defines the structure; `user = Bank()` creates the instance. |
| **Class Variables** | `database` and `data` shared across all instances. |
| **Class Methods** | `__update()` and `__accountgenerate()` are used for database handling and account creation. |
| **Encapsulation** | Internal data management handled via private methods (`__update`). |
| **Exception Handling** | Prevents runtime crashes during file reading and input errors. |
| **File Handling (JSON)** | Saves and retrieves data from `data.json` for persistent storage. |

---

## Project Flow

1. **Initialization**  
   The program checks if the database file (`data.json`) exists. If it does, existing user data is loaded.

2. **Menu Options**  
   Upon execution, the user is presented with options:
```
    Press 1: Create Account
    Press 2: Deposit money
    Press 3: Withdraw money
    Press 4: View details
    Press 5: Update details
    Press 6: Delete account
```

3. **Account Creation**
- Collects user details such as name, age, email, and 4-digit PIN.  
- Automatically generates a unique alphanumeric account number.  
- Validates eligibility (must be 18+ with a valid 4-digit PIN).  
- Saves the user data into `data.json`.

4. **Depositing Money**
- User enters account number and PIN for verification.  
- Allows deposits up to ₹10,000 per transaction.  
- Updates and saves new balance in the database.

5. **Withdrawing Money**
- Ensures sufficient balance before withdrawal.  
- Updates balance after successful transaction.

6. **Viewing Account Details**
- Displays full account details including name, balance, and account number.

7. **Updating User Information**
- Allows changing name, email, or PIN.  
- Restricts modification of age, account number, or balance.  
- Reflects all updates in `data.json`.

8. **Deleting an Account**
- Confirms user intent before deletion.  
- Removes user data permanently from the file.

---

## Code Explanation

### Class Definition
```python
class Bank:
 database = 'Bank_management/data.json'
 data = []
```
Defines the Bank class with a shared database path and data container.
---

### Database Handling
```python
if Path(database).exists():
    with open(database) as fs:
        data = json.loads(fs.read())
```
Checks for the existing database and loads all account information.
---

### Account Creation
```python
def createaccount(self):
    info = {
        "Name": input("Enter your name: "),
        "Age": int(input("Enter your age: ")),
        "Email": input("Enter Your Email: "),
        "Pin": int(input("Enter you pin (4 digit): ")),
        "AccountNo.": Bank.__accountgenerate(),
        "Balance": 0
    }
```
Takes user inputs, validates them, generates an account number, and stores data persistently.
---

### Deposit and Withdrawal

- Both methods (depositMoney, withrawlMoney) perform:
- Account and PIN verification
- Validation of amount limits
- Balance updates followed by saving data to JSON
---

### Updating Account Details

Allows partial modification:
```python
"Name": input("Enter new name or enter to skip: "),
"Email": input("Enter the new email or enter to skip: "),
"Pin": input("Enter new pin or enter to skip: ")
```
---

### Data Persistence

Every change is written to the JSON file through:
```python
with open(cls.database, 'w') as fs:
    fs.write(json.dumps(Bank.data))
```
---

### Example Run
```yaml
Press 1: Create Account
Press 2: Deposit money
Press 3: Withdraw money
Press 4: View details
Press 5: Update details
Press 6: Delete account

Enter your choice: 1

Please provide your info:
Enter your name: Pradip
Enter your age: 20
Enter Your Email: pradip@example.com
Enter your pin (4 digit): 1234

Account created successfully
Please note your Account No.
```
---

### Project Structure
```bach
📁 Bank Management System (OOP)
 ├── bank_app.py            # Main Python script
 ├── data.json              # Stores all user data
 └── README.md              # Project documentation
```
---

### How to Run

1. Clone or download the repository.
2. Navigate to the project folder.
3. Run the file:
```
python main.py
```
---

### Future Improvements

- Implement transaction history.
- Add login session system.
- Support for interest calculation.
- Improved validation and error messages.
- Option to export account statements.
---

## Author

**Pradip Pawar**

Raw Python Logic-building Series — OOP Edition
GitHub: **[Raw-python-Logic_building](https://github.com/pradip-pawar1/Raw-python-Logic_building)**

```yaml

---

Would you like me to **append an “OOP Learning Reflection”** section at the end (e.g., what you learned about class methods, encapsulation, etc.) — written in your tone, so it looks natural in your repo?  
It’ll make the README feel personal and educational.
```