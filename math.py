from tkinter import *

master = Tk()
master.geometry('250x155')
master.title("MATH")

# num1 = eval(input("num1: "))
# num2 = eval(input("num2: "))
e1val = IntVar()
e1 = Entry(master)
e1.pack()
e1val = e1.get()

e2val = IntVar()
e2 = Entry(master)
e2.pack()
e2val = e2.get()

def add(num1, num2):
    s = num1 + num2
    print(s)

# def make_add():
#     add(e1val, e2val)

startbutton = Button(master, text="add", command=add, args=(e1val, e2val,), fg="green")
startbutton.pack()
mainloop()