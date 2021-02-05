import os
from art import logo

clear = lambda: os.system('clear')
clear()
print(logo)
print("Welcome to the secret auction program.")

bidders = {}

def high_bidders(bidders):
  high_price = 0
  winner = ""
  for pers in bidders:
    if bidders[pers] > high_price:
      high_price = bidders[pers]
      winner = pers
  clear()
  print(f"The winner is {winner} with a bid of ${high_price}.")

other = True
while other:
  name = input("What is your name?: ")
  price = int(input("What's your bid?: $"))

  again = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  bidders[name] = price

  if again == "no":
    other = False
    high_bidders(bidders)
  else:
    clear()