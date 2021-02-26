import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
letters_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ")
result = [letters_dict[letter.upper()] for letter in user_input]

print(result)
