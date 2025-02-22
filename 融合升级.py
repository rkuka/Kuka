import turtle
import time
import tkinter as tk
from tkinter import messagebox

def show_love():
    turtle.color("blue", "red")
    turtle.begin_fill()
    turtle.left(45)
    turtle.fd(200)
    turtle.circle(100, 180)
    turtle.right(90)
    turtle.circle(100, 180)
    turtle.fd(200)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-160, 200)
    for i in range(len(f"赵紫妍 , 我喜欢你！")):
        turtle.write(f"赵紫妍 , 我喜欢你！"[:i+1],
                     align="left", font=("Arial", 30, "normal"))
        turtle.delay(100)
    time.sleep(3)
    turtle.done()

show_love()

def small_window():
    messagebox.showinfo("戴隆有", "赵紫妍 , 我喜欢你！")

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.1)

button = tk.Button(root, command=small_window,
                   width=root.winfo_screenwidth(), height=root.winfo_screenheight())
button.pack()

root.mainloop()
