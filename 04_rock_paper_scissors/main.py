rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choices = [rock, paper, scissors]

comp = random.randint(0, 2)

pers = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if pers >= 0 and pers < 3:
  print(choices[pers])
  print("Computer chose:\n\n" + choices[comp])
  if comp == pers:
    print("It's a draw")
  elif comp == 0:
    if pers == 1:
      print('You win!')
    else:
      print("You lose")
  elif comp == 1:
    if pers == 0:
      print('You lose')
    else:
      print('You win!')
  elif comp == 2:
    if pers == 0:
      print('You win!')
    else:
      print('You lose')
  print('_')
else:
  print("You typed an invalid number, you lose!")