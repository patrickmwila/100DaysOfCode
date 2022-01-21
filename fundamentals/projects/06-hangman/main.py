# imports
from hangman import hangman_logo, hang
from words import random_word
from clear_screen import clear

print(hangman_logo())
# choose a random word
chosen_word = random_word()
word_len = len(chosen_word)

# create a list of dashes corresponding to chosen_word
display = []
for _ in range(word_len):
    display.append("_")

# set the initial value for number of lives
lives = 6

# prompt for user input
chosen_word_as_list = list(chosen_word)
while display != chosen_word_as_list:
    guess = input("Guess a letter: ").lower()
    clear()  # clear output

    # check if user has already guessed the letter
    if guess in display:
        print(f"You have already guessed the letter '{guess}'")

    # check if the letter the user guessed is in chosen_word
    # and replace _ with letter
    for i in range(word_len):
        if chosen_word[i] == guess:
            display[i] = guess

    # check if the user is wrong
    if guess not in chosen_word:
        print(f"You guessed '{guess}' that's not in the word. You lose a life.")
        lives -= 1
        print(hang(lives))

        if lives == 0:
            print(f"You lose \nThe word is {chosen_word}")
            break

    # display the dashes by joining them and turn them into a string
    print(f"{' '.join(display)}")

# display the results
if display == chosen_word_as_list:
    print("You win")
