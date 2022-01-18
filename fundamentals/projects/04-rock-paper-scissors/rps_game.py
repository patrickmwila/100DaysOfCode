#!/usr/bin/python3
"""
    Author     : Patrick Mwila
    Instructor : Dr. Angela Yu
    Description: This program simulates rock, paper, scissors game.
"""
# import the required modules
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# prompt user for input
var_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or " + 
                      "2 for Scissors\n"))

# create a list of the user's options
var_gameplay = [rock, paper, scissors]

# display the user's choice
print(var_gameplay[var_choice])

# generate a random number from 0 to 2 (this is the pc's choice)
var_pc_choice = random.randint(0, 2)

# display the pc's choice
print("Computer choose: ")
print(var_gameplay[var_pc_choice])

# determine the winner based on the user's choice and pc's choice
if (var_choice == var_pc_choice):
    print("It's a draw")

elif (var_choice == 0) and (var_pc_choice == 1):
    print("You lost")

elif (var_choice == 0) and (var_pc_choice == 2):
    print("You won")

elif (var_choice == 1) and (var_pc_choice == 0):
    print("You won")

elif(var_choice == 2) and (var_pc_choice == 0):
    print("You lost")

elif (var_choice == 1) and (var_pc_choice == 2):
    print("You lost")

elif (var_choice == 2) and (var_pc_choice == 1):
    print("You won")

else:
    print("A logical error occured")
