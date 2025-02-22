import turtle
import tkinter as tk
import time
from tkinter import messagebox

def __turtle__():
    turtle.speed(3)
    turtle.bgcolor("black")
    turtle.pencolor("black")
    turtle.fillcolor("white")
    def dumpling():
        turtle.begin_fill()
        turtle.circle(80,360)
        turtle.end_fill()
    dumpling()
    for i in [80]:
        turtle.penup()
        turtle.goto(i,-i)
        turtle.pendown()
        dumpling()
        turtle.penup()
        turtle.goto(-i,-i)
        turtle.pendown()
        dumpling()
    def word():
        turtle.color("white","white")
        turtle.penup()
        turtle.setpos(-160,160)
        turtle.pendown()
        for i in range(len("冬 至 快 乐 ！")):
            turtle.write("冬 至 快 乐 ！"[:i+1],align='left', font=("Times New Roman", 40, 'italic'))
            turtle.delay()
            time.sleep(0.2)
    word()
    turtle.done()

def __tkinter__():
    root = tk.Tk()
    root.attributes('-fullscreen',True)
    root.attributes('-alpha',0.1)
    def small_window():
        messagebox.showinfo("節日提醒……","冬至快乐！")
    button = tk.Button(root,command=small_window,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
    button.pack()
    root.mainloop()

__turtle__()
__tkinter__()