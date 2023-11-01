from tkinter import *

window = Tk()
window.title("Mile to Kilometer")
window.minsize(width=400, height=400)
window.config(padx=150, pady=150)

entry = Entry()
entry.grid(row=0, column=1)

label = Label(text="Miles")
label.grid(row=0, column=2)

label1 = Label(text=0)
label1.grid(row=1, column=1)

label2 = Label(text="Km")
label2.grid(row=1, column=2)

label3 = Label(text="is equal to")
label3.grid(row=1, column=0)


def convert():
    label1.config(text=f"{float(entry.get()) * 1.609}")


button = Button(text="calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
