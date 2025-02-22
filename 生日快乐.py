import tkinter as tk
from tkinter import messagebox
import turtle
import time

def tips_button():
    messagebox.showinfo(" ", "生日祝福即将到来...")

root1 = tk.Tk()
root1.attributes("-fullscreen", True)
root1.attributes("-alpha", 0.1)

button1 = tk.Button(root1, command=tips_button(), width=root1.winfo_screenwidth(),
                    height=root1.winfo_screenheight())

turtle.goto(-200, 0)
for i in range(len("退出窗口后请按 Alt 和 F4 键")):
    turtle.write("退出窗口后请按 Alt 和 F4 键"[:i+1],
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