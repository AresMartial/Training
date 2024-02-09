from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:

    order = input(f"What would you like to order? ({menu.get_items()}): ")

    if order == "off":
        break

    elif order == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    ordered_drink = menu.find_drink(order)

    if ordered_drink is not None:
        if coffee_maker.is_resource_sufficient(ordered_drink) and money_machine.make_payment(ordered_drink.cost):
            coffee_maker.make_coffee(ordered_drink)
