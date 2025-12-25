# Library Management System

A console-based library management system built with core Python to demonstrate fundamental programming concepts and logic building.

## Overview

This project implements a simple library system that allows verified users to view available books, borrow books, and return them. Built without external dependencies, it focuses on core Python features including dictionaries, functions, control flow, and pattern matching.

## Features

- **User Authentication** – Validates username before granting access
- **View Available Books** – Displays current inventory with quantities
- **Borrow Books** – Decrements book count when borrowed
- **Return Books** – Increments book count when returned
- **Session Management** – Exit option to close the system

## Technical Implementation

**Core Concepts:**
- Dictionary-based data storage
- Function modularity with parameter passing
- Control flow using loops and conditionals
- Pattern matching with `match-case` statements
- Exception handling via `SystemExit`

## Installation & Usage

**Requirements:** Python 3.10+

**Run the program:**
```bash
python main.py
```

**Sample workflow:**
```yaml
Welcome to Library System 📚

Enter your username: Pradip
User verified!

1. View available Books
2. Borrow Book
3. Return Book
4. Exit

Enter your choice: 1
Data Science: 2
Rich dad poor dad: 3
48 Laws of power: 2
Insta star: 1
```

## Project Structure

```bash
library-management-system/
├── main-Library.py     # Core application logic
├── map.tldr            # Visual mapping for understanding
└── README.md           # Documentation
```

## Known Limitations

- User and book data not persisted (in-memory only)
- Case-sensitive book title matching
- No stock validation (can result in negative counts)
- Limited error handling for invalid inputs

## Planned Enhancements

- File-based persistence for users and inventory
- Input validation and error handling
- Case-insensitive search functionality
- Borrowing history and due date tracking
- Book categories and search filters

## Part of Raw Python Logic Building Series

This project is part of a collection of Python fundamentals projects:


|Sr. No | Project Name              | Link                                            |
| ---- | ------------------------- | ----------------------------------------------- |
| 1 | Bank Management system (OOPs)           | [View Project](../../object_oriented_programming/01_bank_management/)           |
| 2 | ATM Simulation            | [View Project](../../procedural_programming/02_atm_simulation/)            |
| 3 | Word Guess game | [View Project](../../procedural_programming/01_word_guess_game/) |
| 4 | Student report card system | [View Project](../../procedural_programming/04_student_report_card_system/) |
| 5 | Number analyser | [View Project](../../procedural_programming/05_number_analyzer/) |
| 6 | Vehicle Management System | [View Project](../../object_oriented_programming/02_vehicle_management/)

**Repository:** [Raw-python-Logic_building](https://github.com/pradip-pawar1/Raw-python-Logic_building)

## Author

**Pradip Pawar**  
Data Scientist | Python Enthusiast  
[GitHub](https://github.com/pradip-pawar1) • [LinkedIn](https://linkedin.com/in/pradip-pawar-4843b028a)

---

*Built to strengthen Python fundamentals through practical implementation*