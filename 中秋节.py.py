import turtle
import time
import tkinter as tk
from tkinter import messagebox

def Mid_Autumn():
    turtle.bgcolor("black")
    turtle.color("black", "yellow")
    turtle.begin_fill()
    turtle.forward(150)
    turtle.left(45)
    turtle.circle(200, 360)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-160, 160)
    turtle.penup()
    for i in range(len(f"陈逸朗 , 中秋快乐！")):
        turtle.write(f"陈逸朗 , 中秋快乐！"[:i+1],
                     align="left", font=("Times New Roman", 30, "italic"))
        turtle.delay()
    time.sleep(3)

Mid_Autumn()

def wish_button():
    messagebox.showinfo(" ", "陈逸朗 , 中秋快乐！")

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.1)

button = tk.Button(root, command=wish_button,
                    width=root.winfo_screenwidth(), height=root.winfo_screenheight())
