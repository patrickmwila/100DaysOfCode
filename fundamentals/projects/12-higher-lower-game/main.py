from art import *
from clear_screen import clear
from game_data import data
from random import choice


def f_data(d):
    return f"{d['name']}, a {d['description']}, from {d['country']}."


def compare(d1, d2):
    if d1['follower_count'] > d2['follower_count'] or \
       d1['follower_count'] == d2['follower_count']: 
        return True

    else:
        return False


def d_data(win):
    global c_score

    if win:
        c_score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {c_score}")

    else:
        print(f"Sorry, that's wrong. Final score: {c_score}")
        exit(0)


def switch_play():
    global first_item, second_item

    # make sure to compare B against any other random person
    first_item = second_item
    second_item = choice(data)


# start the game
print(logo)
c_score = 0
first_item = choice(data)
second_item = choice(data)

if first_item == second_item:
    second_item = choice(data)

while True:
    print(f"Compare A: {f_data(first_item)}")
    print(vs)
    print(f"Against B: {f_data(second_item)}")
    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_input == "A":
        if compare(first_item, second_item):
            d_data(True)
            switch_play()  # make sure to compare starting with B
        else:
            d_data(False)

    elif user_input == "B":
        if not compare(first_item, second_item):
            d_data(True)
            switch_play()  # make sure to compare starting with B

        else:
            d_data(False)

    else:
        print("Invalid input detected!")
        exit(0)
