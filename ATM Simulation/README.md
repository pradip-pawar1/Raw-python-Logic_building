# 🏦 Simple ATM System (Python)

A beginner-friendly **ATM Simulation** program written in raw Python.  
This project is designed to strengthen your **logic-building skills** and reinforce **function-based programming** concepts.

---

## ⚙️ Features

- Secure **PIN-based login** system (3 attempts allowed)  
- **Deposit** and **Withdraw** functionalities  
- Real-time **Balance Check**  
- Proper validation for:
  - Incorrect PINs  
  - Insufficient balance  
  - Clean exit using custom error handling (`SystemExit`)  

---

## 🧠 Concepts Covered

- Function design and parameter passing  
- Use of `global` variables for maintaining program state  
- Control flow using `while` and `match-case`  
- Error handling and safe program termination  
- Basic input/output formatting  

---

## 🪜 How It Works

1. The user enters a **PIN** to log in (default PIN: `1234`).  
2. After successful login, the user can:
   - Check their current balance  
   - Deposit money  
   - Withdraw money  
   - Exit the system  
3. The system maintains the balance in memory using a global variable.  
4. The program terminates when the user chooses to exit.

---

## 💻 Code Structure

| Function | Purpose |
|-----------|----------|
| `check_balance()` | Updates and returns the current balance |
| `deposit_money()` | Handles money deposit |
| `withraw_money()` | Handles withdrawal with validation |
| `login()` | Authenticates user with 3 PIN attempts |
| `exit()` | Stops program using `SystemExit` exception |

---

## ▶️ How to Run

1. Make sure Python (3.10+) is installed.  
2. Save the code in a file, for example: `atm_system.py`  
3. Open terminal or command prompt and run:

   ```bash
   python atm_system.py

## 📘 Example Interaction
Enter the pin: 1234<br>
Choose 1: Check Balance<br>
Choose 2: Deposit Money<br>
Choose 3: Withdraw Money<br>
Choose 4: Exit<br>
Enter Your choice: 2<br>
Enter amount: 1000<br>
Your 1000RS is added...<br>
<br>
Choose 1: Check Balance<br>
Enter Your choice: 1<br>
Your current balance is: 6000RS...<br>
