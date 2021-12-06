#!/usr/bin/python3
"""
    Author     : Patrick Mwila
    Instructor : Dr. Angela Yu
    Description: This program simulates rock, paper, scissors game.
"""
import random

pc_rand = random.randint(0, 2)

# display message and prompt for input
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
var_opt = int(input())

if (var_opt == 0):
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')

    print("Computer chose: ")
    if (pc_rand == 0):
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

It's a draw
        ''')

    elif (pc_rand == 1):
        print('''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

You won
        ''')

    elif (pc_rand == 2):
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You won
        ''')
    else: 
        print("An error occured! Contact admin.")

elif (var_opt == 1):
    print('''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    ''')

    print("Computer chose: ")
    if (pc_rand == 0):
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

You lose
        ''')

    elif (pc_rand == 1):
        print('''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

It's a draw
        ''')

    elif (pc_rand == 2):
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You lose
        ''')
    else:
        print("An error occured! Contact admin.")

elif (var_opt == 2):
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

    print("Computer chose: ")
    if (pc_rand == 0):
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

You lose
        ''')

    elif (pc_rand == 1):
        print('''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

You won
        ''')

    elif (pc_rand == 2):
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

It's a draw
        ''')
    else:
        print("An error occured! Contact admin.")
else: 
    print("Invalid option." +
          "\nGame over!")
