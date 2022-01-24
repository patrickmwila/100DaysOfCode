from art import logo
from clear_screen import clear
from random import choice


# define a deal card function
def deal_card():
    """
    Generates random card from the deck
    :return: random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


# calculate score function
def calculate_score(cards):
    """
    takes in a list of cards
    :param cards:
    :return: the score calculated from the cards
    """
    if len(cards) == 2 and sum(cards) == 21:
        return 0  # indicating a blackjack score

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# compare function
def compare_score(u_score, p_score):
    if u_score == p_score:
        print("Draw! 🙃")
    elif p_score == 0:
        print("You Lose! Opponent has Blackjack 😱")
    elif u_score == 0:
        print("You Win with a Blackjack 😎")
    elif u_score > 21:
        print("You went over. you Lose 😩")
    elif p_score > 21:
        print("You Win. Opponent went over 😜")
    elif u_score > p_score:
        print("You win 😋")
    else:
        print("You Lose 😕")


def game_play():
    print(logo)

    # deal user and computer 2 cards
    user_cards = []
    user_score = 0

    pc_cards = []
    pc_score = 0

    for _ in range(2):
        user_cards.append(deal_card())
        pc_cards.append(deal_card())

    # user play
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"PC first card: {pc_cards[0]}")

        # check gameplay
        if user_score == 0 or pc_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if deal == "y":
                user_cards.append(deal_card())

            elif deal == "n":
                is_game_over = True

            else:
                print("Invalid input detected!")
                exit(0)

    # computer play
    while pc_score != 0 and pc_score < 17:
        pc_cards.append(deal_card())
        pc_score = calculate_score(pc_cards)

    # display results
    print(f"\nYour final hand: {user_cards}, Final score: {user_score}")
    print(f"PC final hand: {pc_cards}, Final score: {pc_score}")
    compare_score(user_score, pc_score)


# start the game
game_play()

# prompt user to play again
while input("\nType 'y' to restart or (any key to exit): ") == "y":
    clear()
    game_play()
