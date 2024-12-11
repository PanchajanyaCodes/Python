# Problem 2
# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘High score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the High score whenever the game() function breaks the High score.

import random


def game():
    """Generates a random integer from 1 to 100."""
    random_number = random.randint(1, 100)
    return random_number


# Current Score.
current_score = game()

# File Path.
file_path = "./text/high-score.txt"

# Read the high score.
with open(file_path, "r") as file:
    high_score = file.read()
    if high_score == "":
        high_score = 0
    else:
        high_score = int(high_score)

# Compare current score with high score and update if needed.
if current_score > high_score:
    with open(file_path, "w") as file:
        file.write(str(current_score))
    print(f"New High Score: {current_score}")
else:
    print(f"Your Score: {current_score}")

print(f"Previous High Score: {high_score}")
