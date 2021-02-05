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

def check_resources(coffe):
  for ing in MENU[coffe]['ingredients']:
    if MENU[coffe]['ingredients'][ing] > resources[ing]:
      print("Sorry there is not enough water.")
      return False
  return True

def change_resources(coffe):
  for ing in MENU[coffe]['ingredients']:
    resources[ing] -= MENU[coffe]['ingredients'][ing]

money = 0
again = True
while again:
  coffe = input("​ What would you like? (espresso/latte/cappuccino): ")
  if coffe == 'off':
    again = False
  elif coffe == 'report':
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")
  elif check_resources(coffe):
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    if total < MENU[coffe]['cost']:
      print("Sorry that's not enough money. Money refunded.")
    else:
      money += MENU[coffe]['cost']
      change_resources(coffe)
      if total > MENU[coffe]['cost']:
        print(f"Here is ${round(total - MENU[coffe]['cost'], 2)} dollars in change.")
      print(f"Here is your {coffe}. Enjoy!")


