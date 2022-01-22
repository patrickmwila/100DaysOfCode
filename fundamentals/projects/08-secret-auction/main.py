from clear_screen import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidders = {}


def auction_prompt():
    name = input("What is your name?: ")
    bid = float(input("What is your bid: $"))

    # initialize name as key and bid as value
    bidders[name] = bid


# invoke the auction_prompt()
auction_prompt()

bidders_present = True
while bidders_present:
    print("Are there any other bidders? Type 'yes' or 'no'.")
    check = input().lower()

    if check == "yes":
        clear()
        auction_prompt()

    elif check == "no":
        bidders_present = False

    else:
        print("Invalid input detected!")

# check for the highest bidder
highest_bidder = 0
winner = ""

for bidder in bidders:
    if bidders[bidder] > highest_bidder:
        highest_bidder = bidders[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bidder}.")
