# 🏦 ATM System - Python

A beginner-friendly ATM simulation written in Python, designed to reinforce core programming concepts such as functions, control flow, and error handling. This project provides a practical example of building a simple banking system with a focus on secure login, transaction validation, and program termination.

## Overview

This ATM system allows users to log in using a PIN, check their balance, deposit money, and withdraw funds. It emphasizes secure input validation, exception handling, and clean code structure, making it ideal for learners to strengthen their understanding of function design and control flow.

## Features

- Secure PIN login with 3 attempts
- Balance inquiry feature
- Money deposit and withdrawal with validation
- Proper handling of insufficient balance
- Graceful system exit using exception handling
- Memory of account balance throughout the session

## How It Works

1. The user is prompted to enter a PIN for authentication.
2. After successful login, the menu options are displayed:
   - Check current balance
   - Deposit money
   - Withdraw money
   - Exit the system
3. The program continuously prompts for operations until the user chooses to exit.
4. All transactions update in real-time with validation to prevent errors such as overdraft.
5. The program terminates gracefully, providing a clear exit message.

## Technologies Used

| Library        | Purpose                               |
|----------------|---------------------------------------|
| Python Standard Library | Basic programming constructs, control flow |

## Usage Instructions

1. Save the code in a Python file, e.g., `atm_system.py`.
2. Run the program using the command:
```bash
python main.py
```

3. Follow the on-screen prompts to authenticate and perform banking operations.

## Example Interaction

```yaml
Enter the pin: 1234
Choose 1: Check Balance
Choose 2: Deposit Money
Choose 3: Withdraw Money
Choose 4: Exit

Enter Your choice: 2
Enter amount: 1000
Your 1000 RS is added...

Choose 1: Check Balance
Enter Your choice: 1
Your current balance is: 6000 RS...
```


## Project Structure

```bash
atm_simulation/  
├── atm_system.py    # Main program file
```


## Future Enhancements

- Implement a graphical user interface (GUI)
- Add account management for multiple users
- Record transaction history
- Enhance security with hashed PIN storage
- Integrate with real banking APIs for practical use
---

## Project List

| Project Name | Description | Link |
|---------------|--------------|------|
| **Word Guess Game** | Two-player word chain game where each player must form valid words within a time limit. Demonstrates input validation, loops, and condition handling. | [Open](../Word_guess_game) |
| **Library Management System** | A simple command-line library system for viewing, borrowing, and returning books. Built using dictionaries and conditional logic. | [Open](../Library_management) |
| **Bank Management System (OOP)** | First OOP-based project in the series. Implements account creation, deposits, withdrawals, and updates using class-based design and JSON storage. | [Open](../OPPs_projects/Bank_management) |
---


## Author

**Pradip Pawar**  
Exploring Python and building practical projects.  
[GitHub Profile](https://github.com/pradip-pawar1)

---

*This project is part of the Raw Python Logic-building series, aimed at developing strong programming fundamentals for beginners.*
