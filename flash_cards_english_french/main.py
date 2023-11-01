import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash_Cards")
window.config(pady=70, padx=70, bg=BACKGROUND_COLOR)

current_word = {}
words_list = []
# data processing
try:
    updated_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    words_list = data.to_dict(orient="records")
else:
    words_list = updated_data.to_dict(orient="records")


# dictionary that will hold, a random dictionary from the data_dictionary


def check_mark_button():
    words_list.remove(current_word)
    updated_list = pd.DataFrame(words_list)
    updated_list.to_csv("data/words_to_learn.csv", index=False)
    french_word_card()


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_word['English']}", fill="white")


translation_timer = ' '


def french_word_card():
    global current_word, translation_timer
    window.after_cancel(translation_timer)
    current_word = random.choice(words_list)
    french_word = current_word['French']
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=f"{french_word}", fill="black")
    translation_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526)

back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_image)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

language = canvas.create_text(400, 100, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text((400, 263), text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=french_word_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=check_mark_button)
right_button.grid(row=1, column=1)

french_word_card()
window.mainloop()
