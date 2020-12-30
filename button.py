from tkinter import *

master = Tk()
def closewindow():
    exit()
button = Button(master, text="close window", command=closewindow)
button.pack()
mainloop()
