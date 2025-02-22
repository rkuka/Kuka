import turtle
import tkinter as tk
from tkinter import messagebox

def __draw__():
    turtle.color('black')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0, -20)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()


def __circle__():
    turtle.color('white')
    turtle.begin_fill()
    turtle.penup()
    turtle.setpos(8, -180)
    turtle.pendown()
    turtle.circle(200, 360)
    turtle.end_fill()

def __background__():
    turtle.bgcolor('red')

def __end__():
    turtle.hideturtle()
    turtle.done()

def ______main______():
    turtle.speed(0)
    __circle__()
    __draw__()
    __background__()
    __end__()

______main______()

root = tk.Tk()
root.attributes("-fullscreen",True)
root.attributes("-alpha",0.1)

def small_window():
    messagebox.showinfo("元首的提醒","希特勒万岁!")

button = tk.Button(root,command=small_window,width=root.winfo_screenwidth(),height=root.winfo_screenheight())

button.pack()

root.mainloop()