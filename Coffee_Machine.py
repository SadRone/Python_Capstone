from statistics import median_low

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients":{
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
is_on = True
profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made and false when ingredients are insufficient          process_coins("""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough water. {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many quarters?: ")) * 0.1
    total += int(input("how many quarters?: ")) * 0.05
    total += int(input("how many quarters?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted and return False if money is insufficient"""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's  not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

while is_on:
    user_input = input(f'''
    What would you like? (espresso/latte/cappuccino): ''')


    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(user_input, drink["ingredients"])