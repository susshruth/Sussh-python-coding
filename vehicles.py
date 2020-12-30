from tkinter import *

master = Tk()
master.geometry('250x155')

def car():
    startcar = bool(False)
    def start():
        if(startcar == bool(False)):
            print("drrdrr...")
            startcar = bool(True)
        else:
            print("car is already started")
    startbutton = Button(master, text="start", command=start, fg="green")
    startbutton.grid(row=1,column=0)
    def stop():
        exit()
    stopbutton = Button(master, text="stop", command=stop, fg="red")
    stopbutton.grid(row=1,column=1)
    def windowup():
        window_up = bool(True)
        print("window up")
        window_up = True
    windowupbutton = Button(master, text="window", command=windowup)
    windowupbutton.grid(row=2,column=0)
    def windowdown():
        window_up = bool(True)
        print("window down")
        window_up = False
    windowdownbutton = Button(master, text="window", command=windowdown)
    windowdownbutton.grid(row=2,column=1)

button = Button(master, text="car", command=car)
button.grid(row=1,column=1)
mainloop()