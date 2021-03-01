from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip as pyp
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_passwd():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	passwd = [choice(letters) for _ in range(randint(8, 10))]
	[passwd.append(choice(symbols)) for _ in range(randint(2, 4))]
	[passwd.append(choice(numbers)) for _ in range(randint(2, 4))]

	shuffle(passwd)

	res = "".join(passwd)

	pass_entry.delete(0, END)
	pass_entry.insert(0, res)
	pyp.copy(pass_entry.get())


# ------------------------------ SEARCH ------------------------------------ #

def find_password(data, website):
	try:
		info = data[website]
	except KeyError:
		messagebox.showinfo(title="Error",
			message="No details for the website exists")
	else:
		email = info['email']
		passwd = info['password']
		messagebox.showinfo(title=website,
			message=f"Email: {email}\nPassword: {passwd}")
		pyp.copy(passwd)

def search():
	website = website_entry.get()
	try:
		with open("data.json", 'r') as f:
			data = json.load(f)
	except FileNotFoundError:
		messagebox.showinfo(title="Error",
			message="No Data File Found")
	else:
		find_password(data, website)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_file(data):
	with open("data.json", 'w') as f:
		json.dump(data, f, indent=4)

def save():
	website = website_entry.get()
	email = user_entry.get()
	passwd = pass_entry.get()
	new_data = {
		website: {
			"email": email,
			"password": passwd,
		}
	}

	if not website or not email or not passwd:
		messagebox.showinfo(title="Oops",
			message="Please don't leave any fields empty")
	else:
		try:
			with open("data.json", 'r') as f:
				data = json.load(f)
		except:
			write_file(new_data)
		else:
			data.update(new_data)
			write_file(data)
		finally:
			pass_entry.delete(0, END)
			website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=17)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=15,
	command=search)
search_button.grid(row=1, column=2)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

user_entry = Entry(width=36)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "sidi@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=17)
pass_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password",
	command=generate_passwd)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)
# columnspan to extend to 2 columns

window.mainloop()
