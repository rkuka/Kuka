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
                     align="left", font=("Times New Roman", 30, "italic"))
        turtle.delay()
        time.sleep(0.1)
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

print("                                作者     ：     顾家                     ", '\n')
print('To  赵紫妍 ：')
words = "Love"
for item in words.split():
 letterlist = []
 for y in range(12, -12, -1):
  list_X = []
  letters = ''
  for x in range(-30, 30):
   expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
   if expression <= 0:
    letters += item[(x-y) % len(item)]
   else:
    letters += ' '
  list_X.append(letters)
  letterlist += list_X
 print('\n'.join(letterlist))
 time.sleep(0.5)
print('                                           Yours,')
print('                                           戴隆有')
time.sleep(30)
