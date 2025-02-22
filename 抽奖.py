import random
import tkinter as tk
from tkinter import messagebox

prize = random.randint(0,2)

password = []
i = random.randint(1,8)
h = random.randint(1,8)
g = random.randint(1,8)
q = random.randint(1,8)
l = random.randint(1,8)
j = random.randint(1,8)
k = random.randint(1,8)
password = f"{i}{g}{h}{j}{q}{k}{l}{prize}"

root = tk.Tk()
def choice():    
    label1 = tk.Label(root,text=f"奖金：{prize}人民币")
    label1.pack(pady=5)
    if(prize!=0):
        lable2 = tk.Label(root,text=password)
        lable2.pack(pady=5)
button = tk.Button(root,text="抽取",command=choice)
button.pack(pady=10)

root.mainloop()