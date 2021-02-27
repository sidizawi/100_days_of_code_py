from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=800, height=600)

# label
label = Label(text="this is old text")
label.config(text="this is new text")
label.pack()

# button cammand
def action():
	print("Do smth")

# Button
button = Button(text="click me", command=action)
button.pack()

# Entry
entry = Entry(width=30)
entry.insert(END, string="some text to begin with.")
entry.pack()

# Text
text = Text(height=5, width=30)
# puts cursor in textbox.
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
	print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scake_used(value):
	print(value)

scale = Scale(from_=0, to=100, command=scake_used)
scale.pack()

# Checkbutton
def checkbutton_used():
	# print 1 if checked else 0
	print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?",
	variable=checked_state,
	command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
	print(radio_state.get())

#var to hold which radio b is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, 
	variable=radio_state,
	command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, 
	variable=radio_state,
	command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
	# gets current selction
	print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
i = 0
for item in fruits:
	listbox.insert(i, item)
	i += 1
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()

"""
.pack(): met les objets un en dessous de l'autre
or change .pack(side="left")

.place(x=0, y=0) : on peut choisir l'emplacement

.grid(column=0, row=0)	: on le place top left

adding padding to the edge:
window.config(padx=20, pady=20)

to a widget:
label.config(padx=50, pady=20)

"""