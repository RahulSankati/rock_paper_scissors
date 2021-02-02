# imoprting random module
import random
# With the help of enum.IntEnum() method, we can get the enumeration based on integer value
from enum import IntEnum

# Creating Action class


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

# User selction


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

# Computer selection


def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

# Determining Winner


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


# Handling errors
while True:
    try:
        user_action = get_user_selection()

    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)
# Play again or not
    play_again = input("Play again? (y/n): ")
    if play_again in ["yes", 'YES', 'Y', 'y']:
        continue
    elif play_again in ['no', 'n', 'NO', 'N']:
        print("Thanks for playing")
        break
