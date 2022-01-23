from art import logo
from calculator import *
from clear_screen import clear


def calculator_fxn():
    print(logo)

    num1 = 0
    try:
        num1 = float(input("What's the first number?: "))

    except ValueError:
        print("Invalid input detected!")
        exit(0)

    # print operator to be used
    for operator in operations:
        print(operator)

    while True:
        # prompt for operator
        valid_opt = ["+", "-", "*", "/"]
        opt_symbol = input("Pick an operation: ")

        if opt_symbol not in valid_opt:
            print("Invalid input detected!")
            exit(0)

        num2 = 0
        try:
            num2 = float(input("What's the second number?: "))

        except ValueError:
            print("Invalid input detected!")
            exit(0)

        calc_fxn = operations[opt_symbol]
        answer = calc_fxn(num1, num2)

        print(f"{num1} {opt_symbol} {num2} = {answer}")

        # prompt user to run program again
        response = input(
            f"\nType 'y' to continue calculating with {answer} or type 'n' "
            "\nto start a new calculation (any key to exit): "
        )

        if response == "y":
            num1 = answer

        elif response == "n":
            clear()
            #  implement recursion
            calculator_fxn()

        else:
            break
