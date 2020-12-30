from tkinter import *
from PIL import ImageTk, Image

root = Tk()

imageme = ImageTk.PhotoImage(Image.open('C:\\Users\\Susshruth\\Pictures\\backup\\main-qimg-28cadbd02699c25a88e5c78d73c7babc (1).png'))
label = Label(root, image = imageme)
label.pack()

# python = ImageTk.PhotoImage(Image.open('C:\\Users\\Susshruth\\Pictures\\backup\\main-qimg-28cadbd02699c25a88e5c78d73c7babc (1).png'))
# label1 = Label(root, image = python)
# label1.pack()

button = Button(root, text="Exit", command=root.quit)
button.pack()
root.mainloop()