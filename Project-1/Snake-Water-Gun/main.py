# Snake Water Gun Game......
import random


def computer_choice():
    """Makes computer choices."""
    choices = ["snake", "water", "gun"]
    return random.choice(choices)


def get_winner(player, computer):
    """Declare the winner."""
    if player == computer:
        return "It's a Tie!"
    elif (player == 'snake' and computer == 'water') or (player == 'water' and computer == 'gun') or (player == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"


def game():
    """Starts the game."""
    print("\nWelcome to the Snake, Water, Gun Game!\n")

    valid_choices = ["snake", "water", "gun"]

    while True:
        player = input("Make a choice (snake, water, gun): ").lower()

        if player not in valid_choices:
            print(
                "Invalid choice. Please enter one of the following: snake, water, gun.\n")
        else:
            break

    computer = computer_choice()

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    result = get_winner(player, computer)
    print(result)


game()
