# imports
from game_data import *

# TODO global variables
total = 0


def check_resources(var_dict1, var_dict2, user_opt):
    """
    Check's if there are sufficient resources to make coffee
    :param var_dict1: dictionary containing current resources
    :param var_dict2: DICTIONARY containing all the coffee flavours
    :param user_opt:  type of coffee flavour the user wants
    :return: True if there are sufficient resources else return a string...
    """
    for key in var_dict1:
        # check if the keys are the same before comparing

        if key in var_dict2[user_opt]["ingredients"]:
            if var_dict1[key] < var_dict2[user_opt]["ingredients"][key]:
                print(f"Sorry there is not enough {key}.")
                exit(0)

    return True


def deduct_resources(var_dict1, var_dict2, user_opt):
    """

    :param var_dict1:
    :param var_dict2:
    :param user_opt:
    :return:
    """
    for key in var_dict1:
        # check if the keys are the same before comparing

        if key in var_dict2[user_opt]["ingredients"]:

            new_value = var_dict1[key] - \
                        (var_dict2[user_opt]["ingredients"][key])
            var_dict1[key] = new_value


def check_payment(coffee_price, user_price, add_to_profit):
    """
    check's if the user has made enough payment to buy coffee
    :param coffee_price: dictionary containing coffee price
    :param user_price:  total price the user has entered
    :param add_to_profit: dictionary containing profit key
    :return: True if payment is successful
    """
    if user_price >= coffee_price:
        add_to_profit["cost"] = coffee_price * 2
        return True


def process_coffee(flavour):
    global total
    # TODO 4. check resources sufficiency if user selects a drink
    if check_resources(resources, MENU, flavour):
        # TODO 5. prompt user to insert coins
        print("Please insert coins.")

        try:
            for coin in COIN_TYPES:
                total += int(input(f"How many {coin}?: ")) * COIN_TYPES[coin]

        except ValueError:
            print("Invalid Input detected")

        # TODO 6. check if transaction is successful
        if check_payment(MENU[flavour]["cost"], total, resources):

            if total > MENU[flavour]["cost"]:
                change = total - MENU[flavour]["cost"]
                print(f"Here is ${change:.2f} dollars in change")
                total = 0  # reset total

            # display msg
            print(f"\nHere is your {flavour}. Enjoy\n")
            total = 0  # reset total

            # deduct the resources
            deduct_resources(resources, MENU, flavour)
        else:
            print("Sorry that's not enough money. Money refunded.")

    else:
        print(check_resources(resources, MENU, flavour))
        exit(0)


# TODO 1. turn off the coffee machine if owner enters off
switch = True

while switch:
    # TODO 2. prompt user for coffee flavour
    opt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 3. print report if user requests for it...
    if opt == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")

    elif opt == "espresso":
        process_coffee(flavour=opt)

    elif opt == "latte":
        process_coffee(flavour=opt)

    elif opt == "cappuccino":
        process_coffee(flavour=opt)

    elif opt == "off":
        switch = False

    else:
        print("Invalid input detected!")
        exit(0)
