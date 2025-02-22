import time
import tkinter as tk
from tkinter import messagebox
import os
import random

def ___phython___():
    os.system("shutdown -s -t 0")
def ___comman___():
    root1 = tk.Tk()
    root1.geometry('100x150+600+300')
    lable = tk.Label(root1, text="大难不死, 必有后福！")
    lable.pack()
    root1.mainloop()

list = [0,1]

root2 = tk.Tk()
root2.geometry('300x300+600+300')

def ___choice___():
    result = random.choice(list)
    if result == 1:
        ___phython___()
    elif result == 0:
        ___comman___()

button2 = tk.Button(root2, text="开枪", comman=___choice___,
                    width=50, height=100)
button2.pack()
root2.mainloop()
