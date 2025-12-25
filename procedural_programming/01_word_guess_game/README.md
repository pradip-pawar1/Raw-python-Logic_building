# Word Guess Game - Python

A two-player console-based Python game testing vocabulary and quick thinking. Each player enters valid English words that start with the last letter of the previous word. Designed for logic-building, timing, and control flow mastery. Part of the **Raw Python Logic-building** series.

## Overview

The game emphasizes fast reasoning, input validation, and strict adherence to chaining rules. Created to strengthen core Python skills in an engaging format.

## Features

- **Random Toss:** Fairly selects which player starts first.
- **Word Validation:** Checks English word validity (using `pyenchant`).
- **Rule Enforcement:** Enforces word chaining and prevents repetition.
- **Timing Mechanism:** Ten-second limit per input.
- **Persistent Results:** Records each match in `best_of_3.json`.
- **Input Handling:** Supports voluntary surrender with `-giveup`.

## How It Works

1. Toss decides who begins.
2. Players alternate, each entering words within 10 seconds.
3. Each word must:
   - Be a valid English word
   - Start with the last letter of the previous word
   - Not repeat previous words
4. Any rule violation or timeout means instant loss.
5. Game records are saved to `best_of_3.json`.

## Technologies Used

| Library    | Purpose                        |
|------------|-------------------------------|
| random     | Toss & turn selection         |
| time       | Timing player inputs          |
| json       | Saving game results           |
| pyenchant  | Dictionary word validation    |

## Example Run
```yaml
Player1 wins the toss!

Player1, enter your word: apple
Correct word
Player2, enter your word: egg
Correct word
Player1, enter your word: goat
Correct word
Player2, enter your word: tiger
Correct word
Player1, enter your word: rabbit
Correct word

Any rule break or timeout — automatic loss for that player.
```


## Installation & Usage

1. **Install Dependencies:**
```bash
pip install pyenchant
```

2. **Run the Program:**
```bash
python main.py
```



## Project Structure
```bash
word-guess-game/
├── main.py # Game logic
├── best_of_3.json # Match records
└── README.md # Documentation
```


## Future Enhancements

- Player name entry
- Player profiles with statistics
- Match summary and history display
- Difficulty levels and timer customization
- Leaderboard and win tracking

## Repository Integration

This game is part of the **[Raw-python-Logic_building](https://github.com/pradip-pawar1/Raw-python-Logic_building)** repository, featuring beginner-friendly Python logic projects.

## Project List

|Sr. No | Project Name              | Link                                            |
| ---- | ------------------------- | ----------------------------------------------- |
| 1 | Bank Management system (OOPs)           | [View Project](../../object_oriented_programming/01_bank_management/)           |
| 2 | ATM Simulation            | [View Project](../../procedural_programming/02_atm_simulation/)            |
| 3 | Library Management System | [View Project](../../procedural_programming/03_library_management/) |
| 4 | Student report card system | [View Project](../../procedural_programming/04_student_report_card_system/) |
| 5 | Number analyser | [View Project](../../procedural_programming/05_number_analyzer/) |
| 6 | Vehicle Management System | [View Project](../../object_oriented_programming/02_vehicle_management/)


## Author

**Pradip Pawar**  
Exploring Python, one project at a time.  
[GitHub](https://github.com/pradip-pawar1) • [Repository](https://github.com/pradip-pawar1/Raw-python-Logic_building)

---

*Developed as part of the Raw Python Logic-building series—a pathway to mastering fundamental Python programming logic.*
