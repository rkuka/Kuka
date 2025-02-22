import tkinter as tk
from tkinter import messagebox
import pywifi
import turtle
import time

wifi = pywifi.PyWiFi()
card = wifi.interfaces()[0]
card.disconnect()

turtle.bgcolor('black')
turtle.pencolor('white')
turtle.goto(-300, 0)
for i in range(len(f"你电脑网卡被关闭了，哈哈哈！")):
    turtle.write(f"你电脑网卡被关闭了，哈哈哈！"[:i+1],
                 align="left", font=("Times New Roman", 30, "italic"))
    turtle.delay()
    time.sleep(0.1)
time.sleep(3)
turtle.done()

def small_window():
    messagebox.showinfo("哈哈哈","你的电脑被我控制了")

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.1)

button = tk.Button(root, command=small_window,
                   width=root.winfo_screenwidth(), height=root.winfo_screenheight())
button.pack()

root.mainloop()