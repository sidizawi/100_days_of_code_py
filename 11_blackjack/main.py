import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

clear = lambda : os.system("clear")

def sum_cards(card):
  total = 0
  for i in card:
    total += i
  if 11 in card and total > 21:
    total -= 10
  return total

def dealer_final(dealer_cards):
  dealer_score = sum_cards(dealer_cards)
  while dealer_score < 17:
    dealer_cards.append(random.choice(cards))
    dealer_score = sum_cards(dealer_cards)
  return dealer_cards

def check_winner(player_score, player_cards, dealer_score, dealer_cards):
  if player_score > 21:
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print("You went over. You lose 😤")
  elif dealer_score > 21:
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print("Opponent went over. You win 😁")
  elif player_score < dealer_score:
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print("You lose 😤")
  elif player_score > dealer_score:
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print("You win 😁")
  else:
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print("Draw")

def play():
  print(logo)
  player_score = 0
  dealer_score = 0
  player_cards = []
  dealer_cards = []
  for i in range(2):
    dealer_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
  player_score = sum_cards(player_cards)
  print(f"Your cards: {player_cards}, current score: {player_score}")
  print(f"Computer's first card: {dealer_cards[0]}")
  player_score = sum_cards(player_cards)
  while player_score < 21 and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
    player_cards.append(random.choice(cards))
    player_score = sum_cards(player_cards)
    print(f"Your cards: {player_cards}, current score: {sum_cards(player_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")
  dealer_cards = dealer_final(dealer_cards)
  dealer_score = sum_cards(dealer_cards)
  check_winner(player_score, player_cards, dealer_score, dealer_cards)



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  play()