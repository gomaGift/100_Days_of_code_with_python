import math
from playsound import playsound
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, mark
    window.after_cancel(timer)
    reps = 0
    mark = ""
    canvas.itemconfig(text_id, text="00:00")
    activity.config(text="Timer")
    checkmark.config(text=mark)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps

    reps += 1
    if reps % 8 == 0:
        playsound('ring.mp3')
        count_down(LONG_BREAK_MIN * 60)
        activity.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        playsound('ring.mp3')
        count_down(SHORT_BREAK_MIN * 60)
        activity.config(text="Short Break", fg=PINK)
    else:
        activity.config(text="Work", fg=YELLOW)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minute = math.floor(count / 60)
    second = math.floor(count % 60)
    global mark
    global timer

    canvas.itemconfig(text_id, text=f"{minute:02d}:{second:02d}")

    if count > 0:
        timer = canvas.after(1000, count_down, count - 1)
    else:
        start_time()
        if reps % 2 == 0:
            mark += "✓"
            checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodolo Timer")
window.config(padx=100, pady=100, bg=GREEN)

canvas = Canvas()
canvas.config(width=200, height=223, bg=GREEN, highlightthickness=0)
bg_image = PhotoImage(file="pomodolo_timer/tomato.png")
canvas.create_image(100, 110, image=bg_image)
text_id = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 20, "bold"), fill="white")
canvas.grid(row=1, column=1)

activity = Label(text="Timer", fg=YELLOW, bg=GREEN, font=(FONT_NAME, 20, "bold"))
activity.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, command=start_time)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset)
reset_button.grid(row=2, column=2)

checkmark = Label(text=mark, fg=YELLOW, bg=GREEN, font=(FONT_NAME, 15))
checkmark.grid(row=3, column=1)

window.mainloop()
gi