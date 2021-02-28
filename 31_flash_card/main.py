from tkinter import *
import pandas as pd
from random import randint

BACKGROUND_COLOR = "#B1DDC6"

def flip_card():
	card.itemconfig(card_image, image=card_back_img)
	card.itemconfig(title_text, text="English", fill="white")
	word = list_words[word_index]['English']
	card.itemconfig(word_text, text=word, fill="white")

def change_word():
	global word_index
	card.itemconfig(card_image, image=card_front_img)
	card.itemconfig(title_text, text="French", fill="black")
	word_index = randint(0, len(list_words) - 1)
	word = list_words[word_index]['French']
	card.itemconfig(word_text, text=word, fill="black")
	window.after(3000, flip_card)

def remove_word():
	global list_words
	list_words.pop(word_index)
	if len(list_words):
		df = pd.DataFrame(list_words)
		df.to_csv("data/words_to_learn.csv", index=False)
	change_word()

french_words = pd.read_csv("data/french_words.csv")
list_words = french_words.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, flip_card)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
	highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_image = card.create_image(400, 263, image=card_front_img)

title_text = card.create_text(400, 130, text="French",
	fill="black", font=("Ariel", 40, "italic"))

word_index = randint(0, len(list_words) - 1)
word = list_words[word_index]['French']
word_text = card.create_text(400, 263, text=word,
	fill="black", font=("Ariel", 60, "bold"))

card.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR,
	highlightthickness=0, command=change_word)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR,
	highlightthickness=0, command=remove_word)
right_button.grid(row=1, column=1)


window.mainloop()
