#!/usr/bin/python3
"""
    Author     : Patrick Mwila
    Instructor : Dr. Angela Yu
    Description: This program implements a tip-calculator.
"""

# Display a message and prompt for input
print("Welcome to the tip calculator.")
bill = float(input("What is the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip /= 100
tip += 1.0

p_split = int (input("How many poeple to split the bill? "))

# Calculate bill for each person
bill_per_person = (bill / p_split) * tip
bill_per_person = round(bill_per_person, 2)

# display the results
print(f"Each person should pay: ${bill_per_person}")
