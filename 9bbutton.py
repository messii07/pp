import tkinter as tk
from tkinter import messagebox

# Function to be called when the button is clicked
def show_message_box():
    messagebox.showinfo("hello python", "practicals!")

# Create the main window
root = tk.Tk()
root.title("Button Example")

# Create a button
button = tk.Button(root, text="hello", command=show_message_box)
button.pack(pady=10)

# Start the main loop
root.mainloop()
