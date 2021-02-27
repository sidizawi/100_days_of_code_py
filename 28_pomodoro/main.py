from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
	global reps
	global check_rep
	if timer != None:
		window.after_cancel(timer)
		title_label.config(text="Timer", fg=GREEN)
		canvas.itemconfig(canvas_text, text="00:00")
		reps = 0
		check_rep = 0
		check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
	global reps
	reps += 1
	if not reps % 8:
		title_label.config(text="Break", fg=RED)
		count_down(LONG_BREAK_MIN * 60)
	elif not reps % 2:
		title_label.config(text="Break", fg=PINK)
		count_down(SHORT_BREAK_MIN * 60)
	else:
		title_label.config(text="Work", fg=GREEN)
		count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
	global check_rep
	global timer
	count_min = math.floor(count / 60) 
	count_sec = round(count % 60)
	if count_sec < 10:
		count_sec = f"0{count_sec}"
	if count_min < 10:
		count_min = f"0{count_min}"
	canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
	if count > 0:
		timer = window.after(1000, count_down, count - 1)
	elif count == 0:
		if reps % 2:
			check_rep += 1
			check_label.config(text=("✔" * check_rep))
		start()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW,
	highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00",
	fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", fg=GREEN,
	font=(FONT_NAME, 30, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)


start_button = Button(text="Start", command=start,
	highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset,
	highlightthickness=0)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
