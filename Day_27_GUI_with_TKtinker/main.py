from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=150, pady=150)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(row=0, column=0)


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click_Me", command=action)
button.grid(row=1, column=1)

# Entries
entry = Entry(width=30)
# Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(row=5, column=3)

new_button = Button(text="New button")
new_button.grid(row=0, column=2)
window.mainloop()