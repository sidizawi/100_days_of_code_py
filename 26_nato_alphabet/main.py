import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
letters_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
	word = input("Enter a word: ")
	try:
		result = [letters_dict[letter.upper()] for letter in word]
	except:
		print("Sorry, only letters in the alphabet please")
		generate_phonetic()
	else:
		print(result)

generate_phonetic()
