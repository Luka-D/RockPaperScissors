# Standard
import random, time, os, argparse

# Local
from ASCII_sprites import ASCII_sprites


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_result(images):
    strings_by_column = [s.split("\n") for s in images]
    strings_by_line = zip(*strings_by_column)
    max_length_by_column = [
        max([len(s) for s in col_strings]) for col_strings in strings_by_column
    ]
    for parts in strings_by_line:
        # Pad strings in each column so they are the same length
        padded_strings = [
            parts[i].ljust(max_length_by_column[i]) for i in range(len(parts))
        ]
        print("".join(padded_strings))


def player_chooses():
    print("\n")
    print("    Welcome to Rock, Paper, Scissors    ")
    print("=" * 40)
    print("\n")
    result = input("Choose either rock, paper or scissors: ").casefold()
    choicelist = ["rock", "paper", "scissors"]
    if result in choicelist:
        players_choice = result
        return players_choice
    else:
        print("Invalid Selection")
        time.sleep(0.8)
        return None


def opponent_chooses():
    choice = random.randrange(0, 3)
    if choice == 0:
        opponents_choice = "rock"
    elif choice == 1:
        opponents_choice = "paper"
    else:
        opponents_choice = "scissors"
    return opponents_choice


def ro_sham_bo(num):
    print(num)
    print_result(ASCII_sprites["rock_rotated"])
    time.sleep(0.3)
    clear_screen()
    print_result(ASCII_sprites["rock_rock"])
    time.sleep(0.3)
    clear_screen()


def game(players_choice, opponents_choice):
    clear_screen()
    count = 3
    while count > 0:
        ro_sham_bo(count)
        count -= 1
    print("Go!")
    print_result(ASCII_sprites["rock_rotated"])
    time.sleep(0.3)
    clear_screen()
    if players_choice == "rock" and opponents_choice == "scissors":
        print_result(ASCII_sprites["rock_scissors"])
        print("rock beats scissors. You win!")
    elif players_choice == "rock" and opponents_choice == "paper":
        print_result(ASCII_sprites["rock_paper"])
        print("paper beats rock. You lose.")
    elif players_choice == "paper" and opponents_choice == "rock":
        print_result(ASCII_sprites["paper_rock"])
        print("paper beats rock. You win!")
    elif players_choice == "paper" and opponents_choice == "scissors":
        print_result(ASCII_sprites["paper_scissors"])
        print("scissors beat paper. You lose.")
    elif players_choice == "scissors" and opponents_choice == "paper":
        print_result(ASCII_sprites["scissors_paper"])
        print("scissors beat paper. You win!")
    elif players_choice == "scissors" and opponents_choice == "rock":
        print_result(ASCII_sprites["scissors_rock"])
        print("rock beats scissors. You lose.")
    elif players_choice == "rock" and opponents_choice == "rock":
        print_result(ASCII_sprites["rock_rock"])
        print("Same result. Try again.")
    elif players_choice == "paper" and opponents_choice == "paper":
        print_result(ASCII_sprites["paper_paper"])
        print("Same result. Try again.")
    elif players_choice == "scissors" and opponents_choice == "scissors":
        print_result(ASCII_sprites["scissors_scissors"])
        print("Same result. Try again.")
    play_again = input("Play again? (y = Yes, n = No) ").casefold()
    if play_again not in ["y", "yes"]:
        print("Goodbye!")
        quit()

def old_school_game(players_choice, opponents_choice):
    clear_screen()
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("Go!")
    time.sleep(0.5)
    print(f"Opponent chooses {opponents_choice}.")
    time.sleep(0.5)
    print(f"You chose {players_choice}.")
    if players_choice == "rock" and opponents_choice == "scissors":
        print("rock beats scissors. You win!")
    elif players_choice == "rock" and opponents_choice == "paper":
        print("paper beats rock. You lose.")
    elif players_choice == "paper" and opponents_choice == "rock":
        print("paper beats rock. You win!")
    elif players_choice == "paper" and opponents_choice == "scissors":
        print("scissors beat paper. You lose.")
    elif players_choice == "scissors" and opponents_choice == "paper":
        print("scissors beat paper. You win!")
    elif players_choice == "scissors" and opponents_choice == "rock":
        print("rock beats scissors. You lose.")
    elif players_choice == "rock" and opponents_choice == "rock":
        print("Same result. Try again.")
    elif players_choice == "paper" and opponents_choice == "paper":
        print("Same result. Try again.")
    elif players_choice == "scissors" and opponents_choice == "scissors":
        print("Same result. Try again.")
    play_again = input("Play again? (y = Yes, n = No) ").casefold()
    if play_again not in ["y", "yes"]:
        print("Goodbye!")
        quit()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--old_school",
        help="Play Rock Paper Scissors with only text and no images.",
        required=False,
        action="store_true",
    )
    return parser.parse_args()

def main():
    # Choose symbols
    args = parse_arguments()
    players_choice = None
    while players_choice is None:
        clear_screen()
        players_choice = player_chooses()
    opponents_choice = opponent_chooses()

    # Play the game
    if args.old_school:
        old_school_game(players_choice, opponents_choice)
    else:
        game(players_choice, opponents_choice)


if __name__ == "__main__":
    while True:
        main()
