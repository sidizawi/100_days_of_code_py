from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def play():
    again = True
    menu = Menu()
    coffe = CoffeeMaker()
    money = MoneyMachine()
    while again:
        order_name = input(f"What would you like? {menu.get_items()}: ")
        if order_name == "off":
            again = False
        elif order_name == "report":
            coffe.report()
            money.report()
        else:
            order = menu.find_drink(order_name)
            if coffe.is_resource_sufficient(order):
                if money.make_payment(order.cost):
                    coffe.make_coffee(order)


play()