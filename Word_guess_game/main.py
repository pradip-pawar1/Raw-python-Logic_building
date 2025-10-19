import enchant
import random
import time
import json

d = enchant.Dict("en_US")

# Toss function
def toss():
    players = ["Player1", "Player2"]
    winner = random.choice(players)
    return winner

# Word check function
def check(word, all_words, total_time):
    if word == "-giveup":
        print("You loose the game.")
        return False   # game over

    if not d.check(word):  # invalid dictionary word
        print("Incorrect word!")
        return False

    if word in all_words:  # word already used
        print("Word already used!")
        return False
    
    if all_words:
        last_word = all_words[-1]
        if word[0].lower() != last_word[-1].lower():
            print(f"Rule broken! Word must start with '{last_word[-1]}'")
            return False
        
    if total_time > 10:
        print("Time out you loose")
        return False

    # if word is new and valid
    print("Correct word")
    all_words.append(word)
    return True    

def save_best_of_3(match_no, winner, scores):
    data = {
        "match": match_no,
        "winner": winner,
        "score": scores
    }

    with open("best_of_3.json", "a") as f:
        json.dump(data, f)

# ---------- Main game ----------
toss_winner = toss()
print(f"{toss_winner} wins the toss!")

# Arrange players based on toss result
players = ["Player1", "Player2"]
if toss_winner == "Player2":
    players = ["Player2", "Player1"]

all_words = []
current_index = 0   # start with toss winner

# players score
score = {"Player1": 0, "Player2": 0}

secs = 0
# ---------- Game Loop ----------
while True:
    player = players[current_index]
    start = time.time()
    user_input = input(f"{player}, enter your word: ")
    end = time.time()

    total_time = end - start

    if not check(user_input, all_words, total_time):  # game ends if -giveup
        print(f"Game Over! {player} lost.!")
        break

    # Add score for correct move
    score[player] += 1

    print(f"{player} played: {user_input}")

    # Switch player
    current_index = (current_index + 1) % len(players)

# ---------- Final Score ----------
print(f"\nFinal score")
for p, s in score.items():
    print(f"{p}: {s} points")


winner = max(score, key=score.get)
print(f"\n🥇 {winner} wins with {score[winner]} points! \n")