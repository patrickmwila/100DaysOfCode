#!/usr/bin/python3
"""
    Author     : Patrick Mwila
    Instructor : Dr. Angela Yu
    Description: This program implements a simple password generator.
"""
# import the required modules
import random

# create a list of letters, symbols, and numbers
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
           "Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f",
           "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",
           "w","x","y","z"]

symbols = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "|",
           "~", "}", "{", "@", "/", "\\", "]", "[", "."]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# prompt user for input
print("Welcome to the PyPassword Generator!" + 
      "\nHow many letters would you like in your password?")
var_num_of_letters = int(input())

print("\nHow many symbols would you like?")
var_num_of_symbols = int(input())

print("\nHow many numbers would you like?")
var_num_of_numbers = int(input())

# create an empty string...
var_password = ""

# generate n-letters...
for num in range(0, var_num_of_letters):
    var_num = random.randint(0, len(letters) - 1)

    # append the letter to the string var_password
    var_password += letters[var_num]


# generate n-symbols
# note that i have used num again because of the variable's scope
for num in range(0, var_num_of_symbols):
    var_num = random.randint(0, len(symbols) - 1)

    # append the symbol to the string var_password
    var_password += symbols[var_num]


# generate n-numbers
for num in range(0, var_num_of_numbers):
    var_num = random.randint(0, len(numbers) - 1)

    # append the number to the string var_password
    var_password += numbers[var_num]


# display the password
print(f"\nHere is your password: {var_password}")
