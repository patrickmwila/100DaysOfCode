from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ")

    if user_choice == "off":
        is_on = False

    elif user_choice == "report":
        # print current report
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_choice)

        if coffee_maker.is_resource_sufficient(drink) and \
                money_machine.make_payment(drink.cost):

            coffee_maker.make_coffee(drink)
        else:
            continue
