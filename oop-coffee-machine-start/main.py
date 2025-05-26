from coffee_maker import *
from menu import *
from money_machine import *

atm = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
menu = Menu()

atm.report()
coffee_maker.report()
while is_on:
    options =  menu.get_items()
    choice = input(f"What would you like? {options}): ")
    if choice =="off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        atm.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and atm.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)