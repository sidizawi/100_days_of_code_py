from tkinter import *

def calculate():
	res = round(int(entry.get()) * 1.609)
	result.config(text=str(res))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=125)
window.config(padx=20, pady=20)


entry = Entry(width=10)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.config(padx=10, pady=5)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.config(padx=10, pady=5)
equal_label.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()