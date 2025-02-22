import tkinter as tk
from tkinter import messagebox
import turtle
import time

turtle.goto(-200, 0)
for i in range(len("叶倩妤,祝你生日快乐")):
    turtle.write("叶倩妤,祝你生日快乐"[:i+1],
                 align="left", font=("Times New Roman", 30, "italic"))
    turtle.delay()
time.sleep(3)
turtle.done()

def small_window():
    messagebox.showinfo(" ", "叶倩妤,祝你生日快乐")

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.1)

button = tk.Button(root, command=small_window,
                   width=root.winfo_screenwidth(), height=root.winfo_screenheight())
button.pack()

root.mainloop()