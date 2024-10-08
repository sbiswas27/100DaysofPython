# PDF Steps to complete the project: https://drive.google.com/uc?export=download&id=1eIZt2TeFGVrk4nXkx8E_5Slw2coEcOUo

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
money = 0


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total_coins = int(input("How many quarters?: ")) * 0.25
    total_coins += int(input("How many dimes?: ")) * 0.1
    total_coins += int(input("How many nickles?: ")) * 0.05
    total_coins += int(input("How many pennies?: ")) * 0.01
    return total_coins

def is_transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change = round(money_received - drink_cost , 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True

while is_on:
    prompt = input("What would you like? (espresso/latte/cappucino): ").lower()

    if prompt == 'off':
        is_on = False


    elif prompt == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${money}")

    else:
        drink = MENU[prompt]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(prompt, drink['ingredients'])






