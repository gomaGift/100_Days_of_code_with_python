from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = web.get()
    password_ = password_entry.get()
    email_ = email.get()
    if len(website) == 0 or len(password_) == 0:
        messagebox.showinfo(title="Incomplete details", message="please fill all the fields")

    else:
        new_data = {website: {"email": email_, "password": password_}}
        try:
            with open("passwords.json", "r") as file:
                # read data from file
                data = json.load(file)

        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # update data
            data.update(new_data)
            # save appended data
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            web.delete(0, "end")
            password_entry.delete(0, "end")


def search():
    website = web.get()
    with open("passwords.json", "r") as file:
        data = json.load(file)
        user_password = data[website]["password"]
        user_email = data[website]["email"]
        print(f'website: {website}\nemail: {user_email}\npassword: {user_password}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas()
canvas.config(width=200, height=200, highlightthickness=0)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row=0, column=1)

# Labels
url = Label(text="Website:")
url.grid(row=1, column=0)

platform = Label(text="Email/Username:", pady=1)
platform.grid(row=2, column=0)

password_l = Label(text="Password:")
password_l.grid(row=3, column=0)

# Entries
web = Entry(width=33)
web.grid(row=1, column=1)
web.focus()

email = Entry(width=51)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, "gomagiftk01@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="search", width=14, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
