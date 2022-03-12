from tkinter import *
from tkinter.font import Font

root = Tk()


for i in range(8):
    title = 0
    title = Label(root, text='ROYAL CARIBBEAN SHIP ARCHIVE', font=Font(size=30, family='Bahnschrift Bold'), bg='white')

    title.place(x=0, y=i*100)

root.mainloop()
