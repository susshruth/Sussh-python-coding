from tkinter import *

master = Tk()
master.geometry('250x155')

root = Tk()
root.geometry('250x155')

# ---------------------FIRST ROW----------------------------------

label1 = Label(master, text="Password : ")
label1.grid(row=0, column=0)

e1 = Entry(master)
e1.grid(row=0, column=1)

# ---------------------SECOND ROW----------------------------------

label2 = Label(master, text="User Id : ")
label2.grid(row=1, column=0)

e2 = Entry(master)
e2.grid(row=1, column=1)

def submit():
    try:
        entry1 = complex(e1.get())
        entry2 = complex(e2.get())
        correct.config(text="correct", fg="green")
    except ValueError:
        correct.config(text="wrong", fg="red")

def user_id():
    print("userid")

# def submit():
    # print("submit")

correct = Label(master, text='')
correct.grid(row=3, column=2)

button = Button(master, text="submit", command=submit)
button.grid(row=2,column=1)

master.mainloop()
root.mainloop()