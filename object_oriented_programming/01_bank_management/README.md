# Bank Management System

The **Bank Management System** is a console-based Python project built using the **Object-Oriented Programming (OOP)** approach. A Python-based bank management system demonstrating object-oriented programming principles. This project implements core banking operations including account creation, deposits, withdrawals, and account management with persistent JSON storage.

This is the **first OOP project** in the **[Raw Python Logic-building](https://github.com/pradip-pawar1/Raw-python-Logic_building.git)** series, designed to shift from procedural thinking to structured, class-based design.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Class Architecture](#class-architecture)
- [OOP Concepts Demonstrated](#oop-concepts-demonstrated)
- [Technical Details](#technical-details)
- [Future Enhancements](#future-enhancements)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)
- [License](#license)
- [Author & contact](#author)



## Features

- **Account Management**
  - Create new bank accounts with validation
  - View account details securely (PIN protected)
  - Update account information (name, email, PIN)
  - Delete accounts with confirmation
  - Data persistence using JSON file (`data.json`)
  - Deposit and withdrawal with balance checks  
  - Each account stored as **OBJECTS**

- **Banking Operations**
  - Deposit money with amount validation
  - Withdraw money with balance checking
  - Real-time balance updates

- **Data Persistence**
  - Automatic saving to JSON database
  - Load existing accounts on startup
  - Data integrity maintained across sessions

- **Security**
  - PIN-based authentication
  - Age verification (18+ requirement)
  - Secure credential validation


## 📁 Project Structure

```bash
Raw-python-Logic_building/ # Main repo folder
├── 01_bank_management/ # Folder of project
└── banking.py   # Main application file
└── data.json    # Database file (auto-generated)
└── README.md    # Project documentation
```

## Installation
### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only standard library)


### Setup
1. Clone the repository or download the project files:
```bash
git clone https://github.com/pradip-pawar1/Raw-python-Logic_building.git
cd 01_bank_management
```
2. Ensure the project directory structure is maintained
3. Run the application:

```bash
python banking.py
```

## Usage

### Starting the Application

```bash
python banking.py
```

### Menu Options

```yaml
1. Create Account    # Register a new bank account
2. Deposit Money     # Add funds to your account
3. Withdraw Money    # Withdraw funds from your account
4. View Details      # Display your account information
5. Update Info       # Modify account details
6. Delete Account    # Permanently remove your account
7. Exit             # Close the application
```

### Example Workflow

**Creating an Account:**
```bash
Enter your name: Pradip Pawar
Enter your age: 20
Enter your email: pradip@example.com
Enter 4 digit pin: 1234

Account created successfully
Account Number: 123456789
```

**Depositing Money:**
```bash
Enter 9 digit account number: 123456789
Enter 4 digit pin: 1234
Enter amount to deposit: 5000

Deposit successful! New balance: 5000
```


## Class Architecture

### 1. Account Class

Represents a single bank account with its data and operations.

**Attributes:**
- `name`: Account holder's name
- `age`: Account holder's age
- `email`: Contact email
- `pin`: 4-digit security PIN
- `account_no`: Unique 9-digit account number
- `balance`: Current account balance

**Methods:**
- `deposit(amount)`: Add money to account
- `withdraw(amount)`: Remove money from account
- `get_details()`: Return account information
- `to_dict()`: Convert account to dictionary for storage
- `update_info(name, email, pin)`: Update account details

### 2. Bank Class

Manages all accounts and handles database operations.

**Attributes:**
- `database`: Path to JSON database file
- `accounts`: List of Account objects

**Methods:**
- `load_accounts()`: Load accounts from JSON file
- `save_accounts()`: Save all accounts to JSON file
- `create_account(name, age, email, pin)`: Create new account
- `find_account(account_no, pin)`: Authenticate and retrieve account
- `delete_account(account_no, pin)`: Remove account from system

### 3. Banking_system Class

Handles user interface and application flow.

**Attributes:**
- `bank`: Reference to Bank object
- `menu`: Dictionary of menu options

**Methods:**
- `show_menu()`: Display menu options
- `create_account_flow()`: Handle account creation
- `deposit_flow()`: Handle deposit operations
- `withdraw_flow()`: Handle withdrawal operations
- `view_details_flow()`: Display account details
- `update_info_flow()`: Update account information
- `delete_account_flow()`: Delete account
- `run()`: Main application loop

## OOP Concepts Demonstrated

### Encapsulation
- Account data is bundled with operations that manipulate it
- Methods control access to sensitive data (balance, PIN)

### Abstraction
- Complex operations hidden behind simple method calls
- Users interact through clean interface without knowing implementation details

### Separation of Concerns
- **Account**: Manages individual account data and operations
- **Bank**: Handles multiple accounts and persistence
- **Banking_system**: Manages user interaction and flow

### Object Composition
- Bank contains multiple Account objects
- Banking_system uses Bank object for operations

## Technical Details

### Data Validation

**Account Creation:**
- Age must be 18 or above
- PIN must be exactly 4 digits
- All fields are required

**Deposit:**
- Amount must be positive
- Maximum deposit: 50,000 per transaction
- No decimal values (integer only)

**Withdrawal:**
- Amount must be positive
- Cannot exceed current balance
- No overdraft facility

### Data Persistence

Accounts are stored in JSON format:

```json
[
  {
    "Name": "Spyder man",
    "Age": 25,
    "Email": "spyder@example.com",
    "Pin": 1234,
    "AccountNo": 123456789,
    "Balance": 5000
  }
]
```

### Error Handling

- Invalid input types caught with try-except blocks
- Account not found scenarios handled gracefully
- PIN verification before sensitive operations
- Balance validation during withdrawals
- Age and PIN format validation during account creation


### Security Features

- PIN required for all account operations
- PIN not displayed when showing account details
- Account number validation (9 digits)
- PIN validation (4 digits)

### Validation Rules

- Minimum age: 18 years
- PIN: Exactly 4 digits
- Deposit limit: Maximum 50,000 per transaction
- Withdrawal: Cannot exceed current balance
- Account number: 9-digit unique random number

## Future Enhancements

Planned improvements for the next version:

- [ ] Transaction history with timestamps
- [ ] Money transfer between accounts
- [ ] Interest calculation for savings accounts
- [ ] Account types (Savings, Current, Fixed Deposit)
- [ ] Admin panel for bank management
- [ ] Password hashing for enhanced security
- [ ] Export account statements to PDF
- [ ] Email notifications for transactions
- [ ] Multi-currency support
- [ ] Loan management system

## Learning Outcomes

Building this project helped me understand:

**OOP Principles:**
- How to separate concerns across multiple classes
- Difference between objects and dictionaries
- When to use class methods vs instance methods
- Importance of encapsulation and data protection

**Software Design:**
- Organizing code into logical modules
- Creating reusable methods to avoid duplication
- Designing user-friendly menu systems
- Handling edge cases and errors gracefully

**Python Skills:**
- Working with JSON for data persistence
- File I/O operations with proper error handling
- List comprehensions for data filtering
- Type hints for better code readability

**Real-World Application:**
- Understanding how banking systems work
- Implementing authentication and validation
- Managing persistent data across sessions
- Building interactive command-line applications


## Contributing

This is a learning project, but suggestions are welcome!

If you'd like to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](../../LICENSE).

## Author

**Pradip Pawar**

- GitHub: [@pradip-pawar1](https://github.com/pradip-pawar1)
- LinkedIn: [@pradip-pawar1](https://www.linkedin.com/in/pradip-pawar1/)
- Email-1: pradipp8806@gmail.com
- Email-2: pradip.codelabplus@gmail.com



## Screenshots

### Main Menu
```
========================================
    BANK MANAGEMENT SYSTEM
========================================
1. Create Account
2. Deposit Money
3. Withdraw Money
4. View Details
5. Update Info
6. Delete Account
7. Exit
========================================
```

### Account Creation Success
```
Account created successfully
Name: Pradip Pawar
Account Number: 123456789
Please note your account number
```

---

## Check out my other projects

|Sr. No | Project Name              | Link                                            |
| ---- | ------------------------- | ----------------------------------------------- |
| 1 | Word Guess Game           | [View Project](../../procedural_programming/01_word_guess_game/)           |
| 2 | ATM Simulation            | [View Project](../../procedural_programming/02_atm_simulation/)            |
| 3 | Library Management System | [View Project](../../procedural_programming/03_library_management/) |
| 4 | Student report card system | [View Project](../../procedural_programming/04_student_report_card_system/) |
| 5 | Number analyser | [View Project](../../procedural_programming/05_number_analyzer/) |
| 6 | Vehicle Management System | [View Project](../../object_oriented_programming/02_vehicle_management/)


### Thanks for visiting..!