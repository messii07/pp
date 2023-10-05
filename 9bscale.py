import tkinter
from tkinter import *
def sel():
    selection=" value"+str(var.get())
    label.config(text=selection)
root=Tk()
var=DoubleVar()
s=Scale(root,variable=var)
s.pack(anchor=CENTER)
r=Button(root,text="Enter scale value",command=sel)
r.pack(anchor=CENTER)
label=Label(root)
label.pack()
root.mainloop()
