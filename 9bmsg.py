#B. Try to change the widget type and configuration options to experiment with
#other widget types like Message, Button, Entry, Checkbutton, Radiobutton,
#Scale etc.
#Message
import tkinter
from tkinter import *
root=Tk()
var=StringVar()
label=Message(root,textvariable=var,relief=RAISED)
var.set("Hey!?how are you doing??")
label.pack()
root.mainloop()
