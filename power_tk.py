from tkinter import *

master = Tk()
master.geometry('250x155')
master.title("              power")

label1 = Label(master, text="Number : ")
label1.grid(row=0,column=0)

label2 = Label(master, text="Power : ")
label2.grid(row=1,column=0)

entry1 = Entry(master, width = 15)
entry1.grid(row=0,column=1)

entry2 = Entry(master, width = 15)
entry2.grid(row=1,column=1)

def stop():
    exit()

def masterfunc():
    entryval1 = eval(entry1.get())
    entryval2 = eval(entry2.get())
    def Power(number, power):
        if power == 0:
            return 1
        else:
            return number * Power(number, power-1)
            
    answer.set(Power(entryval1, entryval2))
    exitbutton = Button(master, text="exit", command=stop, fg="red")
    exitbutton.grid(row=5,column=1)

answer = IntVar()
answer.set(0)

button = Button(master, text="check power", command=masterfunc, fg="green")
button.grid(row=3,column=1)
anstxt=Label(master, text="         Answer :      ", bg="red", fg="white")
anstxt.grid(row=4,column=1)
anslabel = Label(master, textvariable=answer, bg="red", fg="white")
anslabel.grid(row=4,column=2)
master.mainloop()