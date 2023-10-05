import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
Checkval1=tk.IntVar()
Checkval2=tk.IntVar()
C1=tk.Checkbutton(root,text="music",variable=Checkval1,\
                  onvalue=1,offvalue=0,height=5,\
                  width=20)
C2=tk.Checkbutton(root,text="video",variable=Checkval2,onvalue=1,offvalue=0,height=5,width=20)

C1.pack()
C2.pack()

root.mainloop()
