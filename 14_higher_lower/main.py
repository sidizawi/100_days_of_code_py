import os
from art import *
from game_data import data
from random import choice

clear = lambda: os.system("clear")

def compare(a, b):
  res1 = ['A', 'a']
  res2 = ['B', 'b']
  if a['follower_count'] > b['follower_count']:
    return res1
  return res2

def play():
  a = choice(data)
  score = 0
  again = True
  while again:
    clear()
    b = choice(data)
    while b == a:
      b = choice(data)
    print(logo)
    if score > 0:
      print(f"You're right! Current score: {score}.")
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
    res = compare(a, b)
    answer = input("Who has more follewers? Type 'A' or 'B': ")
    if answer in res:
      score += 1
      a = b
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      again = False

play()