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


|Sr. No | Project Name              | Link                                            |
| ---- | ------------------------- | ----------------------------------------------- |
| 1 | Bank Management system (OOPs)           | [View Project](../../object_oriented_programming/01_bank_management/)           |
| 2 | Word guess Game           | [View Project](../../procedural_programming/01_word_guess_game/)            |
| 3 | Library Management System | [View Project](../../procedural_programming/03_library_management/) |
| 4 | Student report card system | [View Project](../../procedural_programming/04_student_report_card_system/) |
| 5 | Number analyser | [View Project](../../procedural_programming/05_number_analyzer/) |



## Author

**Pradip Pawar**  
Exploring Python and building practical projects.  
[GitHub Profile](https://github.com/pradip-pawar1)

---

*This project is part of the Raw Python Logic-building series, aimed at developing strong programming fundamentals for beginners.*
