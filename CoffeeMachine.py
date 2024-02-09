MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def insufficient_ingredient(order) -> str:
    order_ingredients = MENU[order]["ingredients"]
    for ingredient in order_ingredients:
        if resources[ingredient] <= order_ingredients[ingredient]:
            return ingredient
    return ""


def get_money() -> float:
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Type whole number of coins.")
        return get_money()
    money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return money


while True:
    order = input("What would you like to order? (espresso/latte/cappuccino): ")

    if order == "off":
        break

    elif order == "report":
        for resource in resources:
            print(f"{resource.capitalize()}: {resources[resource]}\n Money: ${profit}")

    elif order in MENU.keys():
        lacking_ingredient = insufficient_ingredient(order)
        if lacking_ingredient != "":
            print(f"Sorry, there's not enough {lacking_ingredient}.")
            break

        print(f"{order} costs ${MENU[order]['cost']}")
        money_inserted = get_money()

        if money_inserted < MENU[order]["cost"]:
            print(f"Sorry that's not enough money. Money refunded")
            continue
        elif money_inserted > MENU[order]["cost"]:
            change = money_inserted - MENU[order]["cost"]
            print(f"Here's ${change:.2f} in change")
            profit += MENU[order]["cost"]
        else:
            profit += MENU[order]["cost"]

        for ingredient in MENU[order]["ingredients"]:
            resources[ingredient] -= MENU[order]["ingredients"][ingredient]

        print(f"Here's your {order}. Enjoy!")
