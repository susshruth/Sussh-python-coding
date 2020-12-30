from tkinter import*
window=Tk()
c=Canvas(window, height=600, width=900, bg='black')
c.pack()
rectangle=c.create_rectangle(50, 50, 150, 150, fill='red')
rect_spd=10
def move_ship(event):
    if event.keysym=='up':
        c.move(rectangle, 0, -rect_spd)
        print('you went up!')
    if event.keysym=='down':
        c.move(rectangle, 0, rect_spd)
        print('you went down!')
    if event.keysym=='right':
        c.move(rectangle, rect_spd, 0)
        print('you went right!')   
    if event.keysym=='left':
        c.move(rectangle, -rect_spd, 0)
        print('you went left!')
        c.bind_all('<Key>', move_ship)

window.mainloop()