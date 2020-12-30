import math
from tkinter import *
import power_tk

master = Tk()
master.title("math by tkinter")
master.geometry("400x200")

def add():
    try:
        entry1 = float(e1.get())
        entry2 = float(e2.get())
        ans = entry1 + entry2
        ans = math.floor(ans)
        answer.config(text=ans)
        correct.config(text="correct", fg="green")
    except ValueError:
        answer.config(text="")
        correct.config(text="wrong", fg="red")

def sub():
    try:
        entry1 = float(e1.get())
        entry2 = float(e2.get())
        ans = entry1 - entry2
        ans = math.floor(ans)
        answer.config(text=ans)
        correct.config(text="correct", fg="green")
    except ValueError:
        answer.config(text="")
        correct.config(text="wrong", fg="red")

def multi():
    try:
        entry1 = float(e1.get())
        entry2 = float(e2.get())
        ans = entry1 * entry2
        ans = math.floor(ans)
        answer.config(text=ans)
        correct.config(text="correct", fg="green")
    except ValueError:
        answer.config(text="")
        correct.config(text="wrong", fg="red")

def div():
    try:
        entry1 = float(e1.get())
        entry2 = float(e2.get())
        ans = entry1 / entry2
        ans = math.floor(ans)
        answer.config(text=ans)
        correct.config(text="correct", fg="green")
    except ValueError:
        answer.config(text="")
        correct.config(text="wrong", fg="red")
# ---------------------FIRST ROW----------------------------------

label1 = Label(master, text="Number 1 : ")
label1.grid(row=0, column=0)

e1 = Entry(master)
e1.grid(row=0, column=1)

# ---------------------SECOND ROW----------------------------------

label2 = Label(master, text="Number 2 : ")
label2.grid(row=1, column=0)

e2 = Entry(master)
e2.grid(row=1, column=1)

# ---------------------THIRD ROW----------------------------------

addbutton = Button(master, command=add, text="+")
addbutton.grid(row=2, column=0)

subbutton = Button(master, command=sub, text="-")
subbutton.grid(row=2, column=1)

multibutton = Button(master, command=multi, text="x")
multibutton.grid(row=2, column=2)

divbutton = Button(master, command=div, text="/")
divbutton.grid(row=2, column=4)

exitbutton = Button(master, command=exit, text="exit", fg="red")
exitbutton.grid(row=5, column=4)
# ---------------------FOURTH ROW----------------------------------

answer = Label(master, text='')
answer.grid(row=3, column=1)

correct = Label(master, text='')
correct.grid(row=3, column=2)

master.mainloop()