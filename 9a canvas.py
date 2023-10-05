#Try to configure the widget with various options like: bg=”red”,
#family=”times”, size=18
import tkinter
from tkinter import *
root = Tk()
O = Canvas(root,bg = "grey", height = 500, width= 500)
O.pack()
n = Label(root,text = "Hello World")
n.pack()
root.mainloop()
