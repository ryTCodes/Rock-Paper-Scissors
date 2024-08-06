import random
from arts import rock, paper, scissors


def main():
    print("Welcome to Rock, Paper and Scissors!!")
    play_game()


def play_game():
    user_choice = int(input("1. Rock\n2. Paper\n3. Scissor\nEnter your Choice: "))
    computer_choice = random.randint(1, 3)

    if user_choice > 3 or user_choice < 1:
        print("Invalid Input!")
        return
    else:
        print(f"\nYour Choice:-\n{game_choices[user_choice - 1]}")
        print(f"Computer Choose:-\n{game_choices[computer_choice - 1]}")

    if user_choice == computer_choice:
        print("It's a draw")
    elif computer_choice == 1 and user_choice == 3:
        print("You Lose")
    elif user_choice == 1 and computer_choice == 3:
        print("You Won")
    elif user_choice > computer_choice:
        print("You Won")
    elif computer_choice > user_choice:
        print("You Lose")

    should_continue = input("\nEnter 'yes' to play again, 'no' to exit: ").strip().lower()
    if should_continue == 'yes':
        play_game()


if __name__ == "__main__":
    game_choices = [rock, paper, scissors]
    main()
