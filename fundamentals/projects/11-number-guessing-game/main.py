from random import randint
from art import logo


def has_lost(number):
    if number == 0:
        print("\nYou've run out of guesses, you lose.")
        exit(0)
    else:
        pass


def game_play():
    global chances
    while chances != 0:
        print(f"\nYou have {chances} chance(s) remaining to guess the number.")

        try:
            user_guess = int(input("Make a guess: "))
            if user_guess > computer_num:

                print("Too high.")
                chances -= 1

                has_lost(chances)
                print("Guess again")

            elif user_guess < computer_num:

                print("Too low.")
                chances -= 1

                has_lost(chances)
                print("Guess again")

            else:
                print(f"You got it! The answer was {computer_num}")
                exit(0)

        except ValueError:
            print("Invalid input detected!")
            exit(0)


# game play
print(logo)
print(
    "Welcome to the Number Guessing Game." +
    "Iam thinking of a number between 1 and 100."
)
computer_num = randint(1, 100)

game_lever = input(
   "\nChoose a difficulty. Type 'easy' or 'hard': "
)

if game_lever == "easy":
    chances = 10
    game_play()


elif game_lever == "hard":
    chances = 5
    game_play()

else:
    print("Invalid input detected!")
    exit(0)
