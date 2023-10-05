import tkinter
from tkinter import *
top=Tk()
l=Label(top,text="username",relief=RAISED)
l.pack(side=LEFT)
c=Entry(top,bd=5)
c.pack(side=RIGHT)
top.mainloop()
