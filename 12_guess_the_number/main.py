from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")

number = randint(1, 100)
attempts = 0
print("I'm thinking of a number between 1 and 100.")
if input("Choose a difficulity. Type 'easy' or 'hard': ") == 'easy':
  attempts = 10
else:
  attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

guess = 0
while guess != number and attempts > 0:
  guess = int(input("Make a guess: "))
  if guess != number:
    attempts -= 1
    if guess < number:
      print("Too low.")
    elif guess > number:
      print("Too high.")
    if attempts > 0:
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
    else:
      print("You've run out of guesses, you lose.")
  else:
    print(f"You got it! The answer was {number}.")