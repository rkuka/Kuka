import turtle
import time
import tkinter as tk
from tkinter import messagebox
from sklearn import neighbors
import random

def gun():
    def ___phython___():
        wifi = pywifi.PyWiFi()
        card = wifi.interfaces()[0]
        card.disconnect()
        turtle.bgcolor("black")
        turtle.color("white", "red")
        turtle.begin_fill()
        turtle.left(45)
        turtle.forward(200)
        turtle.circle(100, 180)
        turtle.right(90)
        turtle.circle(100, 180)
        turtle.forward(200)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-200, 0)
        turtle.pendown()
        for i in range(len(f"网卡被关了哦!")):
            turtle.write(f"网卡被关了哦!"[
                         :i+1], align='left', font=('Times New Roman', 30, 'italic'))
            turtle.delay()
            time.sleep(0.1)
        time.sleep(3)
        turtle.done()
        words = "love"
        for item in words.split():
         letterlist = []
         for y in range(20, -20, -1):
          list_X = []
          letters = ''
          for x in range(-30, 30):
           expression = ((x*0.05)**2+(y*0.1)**2-1.5)**3-(x*0.05)**2*(y*0.1)**5
           if expression <= 0:
            letters += item[(x-y) % len(item)]
           else:
            letters += ' '
          list_X.append(letters)
          letterlist += list_X
         print('\n'.join(letterlist))
        root = tk.Tk()
        root.attributes('-fullscree', True)
        root.attributes('-alpha', 0.1)

        def small_window():
            messagebox.showinfo(" ", "桌面被控制了哦!")
        button = tk.Button(root, command=small_window, width=root.winfo_screenwidth(
        ), height=root.winfo_screenheight())
        button.pack()
        root.mainloop()

    def ___comman___():
        root1 = tk.Tk()
        root1.geometry('100x150+600+300')
        lable = tk.Label(root1, text="大难不死, 必有后福！")
        lable.pack()
        root1.mainloop()

    list = [1, 0]
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

def choice_1():
    while True:
        print('\n'"输入'0'即退出程序")
        number = int(input('请输入抽取次数：'))
        for i in range(number):
            result = random.randint(1, 40)
            print(result)
        if number == 0:
            break

def choice_2():
    while True:
        number = int(input('\n'"输入1启动程序，输入0退出程序。请输入:"))
        if number == 1:
            result = random.randint(1, 40)
            print(result)
        elif number == 0:
            break

def choice_3():
    list = ["张三", "李四", "王五"]

    while True:
        tips = int(input('\n'"输入1启动程序，输入任意数字退出程序。请输入:"))
        if tips == 1:
            result = random.choice(list)
            print(result)
        else:
            break

def __phython__():
    turtle.bgcolor('black')
    turtle.color('white', 'red')
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(200)
    turtle.circle(100, 180)
    turtle.right(90)
    turtle.circle(100, 180)
    turtle.forward(200)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    for i in range(len(f"网卡被关了哦")):
        turtle.write(f"网卡被关了哦"[:i+1], align='left',
                     font=('Times New Roman', 30, 'italic'))
        turtle.delay()
        time.sleep(0.1)
    time.sleep(3)
    turtle.done()

    words = "love"
    for item in words.split():
     letterlist = []
     for y in range(20, -20, -1):
      list_X = []
      letters = ''
      for x in range(-30, 30):
       expression = ((x*0.05)**2+(y*0.1)**2-1.5)**3-(x*0.05)**2*(y*0.1)**5
       if expression <= 0:
        letters += item[(x-y) % len(item)]
       else:
        letters += ' '
      list_X.append(letters)
      letterlist += list_X
     print('\n'.join(letterlist))

    root = tk.Tk()
    root.attributes('-fullscree', True)
    root.attributes('-alpha', 0.1)

    def small_window():
        messagebox.showinfo(" ", "桌面被控制了哦")

    button = tk.Button(root, command=small_window,
                       width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    button.pack()

    root.mainloop()

def game():
    print("                                            作者     ：     顾家                                 ", '\n')
    the_number = random.randint(1, 10)
    print('     Hi！让我们来玩数字扫雷游戏吧！     ')
    print('     现在你有3次机会，请慎重选择！     ')
    print('\n', '                ROUND   ONE                ', '\n')
    count = 0
    while count < 3:
        count += 1
        print(f"        现在是你第{count}次尝试        ")
        guess_number = int(input('请输入您的猜想: '))
        if (guess_number == the_number):
            print('\n', f"        恭喜你，第{count}次猜中了        ", '\n')
            break
        elif (guess_number > the_number):
            print('\n', '猜大了，试着猜小点！', '\n')
        else:
            print('\n', '猜小了，试着猜大点！', '\n')
    if (count > 3):
        print('\n', '                     你        输        了                     ', '\n')
    the_number = random.randint(11, 100)
    print('\n', '                ROUND   TWO                ', '\n')
    count = 0
    while count < 3:
        count += 1
        print('\n', f"        现在是你第{count}次尝试        ", '\n')
        guess_number = int(input('请输入您的猜想: '))
        if (guess_number == the_number):
            print('\n', f"        恭喜你，第{count}次猜中了        ", '\n')
            break
        elif (guess_number > the_number):
            print('\n', '猜大了，试着猜小点！', '\n')
        else:
            print('\n', '猜小了，试着猜大点！', '\n')
    if (count > 3):
        print('\n', '                     你        输        了                     ', '\n')
    the_number = random.randint(101, 1000)
    print('\n', '                ROUND   THREE                ', '\n')
    count = 0
    while count < 3:
      print('\n', f"        现在是你第{count}次尝试        ", '\n')
    guess_number = int(input('请输入您的猜想: '))
    if (guess_number == the_number):
        print('\n', f"        恭喜你，第{count}次猜中了        ", '\n')
        print('\n', '戴隆有喜欢赵紫妍', '\n')
    elif (guess_number > the_number):
        print('\n', '猜大了，试着猜小点！', '\n')
    else:
        print('\n', '猜小了，试着猜大点！', '\n')
    if (count > 3):
        print('\n', '                     你        输        了                     ', '\n')
    time.sleep(30)
def train():
    features = [[80, 85, 88, 78], [95, 94, 93, 92],
                [90, 90, 90, 90], [80, 80, 80, 80]]
    lables = [0, 1, 1, 0]

    clf = neighbors.KNeighborsClassifier(3)
    clf = clf.fit(features, lables)

    while True:
        result = int(input("道法："))
        result1 = int(input("生物："))
        result2 = int(input("地理："))
        result3 = int(input("历史："))
        print(clf.predict([[result, result1, result2, result3]]))
        print('\n')
        result4 = int(input("(1为退出，0为继续)是否退出："))
        print('\n')
        if result4 == 1:
            break
        else:
            continue

def happy_birthday():
    turtle.goto(-200, 0)
    for i in range(len("赵紫妍,祝你生日快乐")):
        turtle.write("赵紫妍,祝你生日快乐"[:i+1],
                     align="left", font=("Times New Roman", 30, "italic"))
        turtle.delay()
    time.sleep(3)
    turtle.done()

    def small_window():
        messagebox.showinfo(" ", "赵紫妍,祝你生日快乐")

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.1)

    button = tk.Button(root, command=small_window,
                       width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    button.pack()

    root.mainloop()

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

    def small_window():
        messagebox.showinfo("戴隆有", "赵紫妍 , 我喜欢你！")


    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.1)

    button = tk.Button(root, command=small_window,
                       width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    button.pack()

    root.mainloop()

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

laungre = input("请选择一门语言 (简体中文/繁體中文/English):")
while True:
    target = input("请输入问题：")

    list1 = '抱歉，您的问题太过高端，我没有能力回答, 或许你可以换一种提问方式或询问另一个问题，我将尽力而为'
    list1_ = '抱歉，您的問題太過高端，我沒有能力回答，或許你可以換一種提問方式或詢問另一個問題，我將盡力而爲'
    list1_1 = 'sorry ,I’m too stupid ,I can’t answer your question, maybe you can ask this question agin in another way or change your question，I’ll try my best to answer it'

    list2 = '你好，我叫人机，不知道该如何称呼您呢'
    list2_ = '你好，我叫人機，不知道該如何稱呼您呢'
    list2_2 = 'hello,my name is AI ,what’s your name'

    if laungre == '简体中文':
        if target == "你叫什么名字" or "你的名字" or "你叫什么" or "你是谁":
            print('\n')
            print(list2)
            print('\n')
            name = input()
            print('\n')
            print(f'你好,{name}')
            print('\n')
        else:
            print('\n')
            print(list1)
            print('\n')
    elif laungre == '繁體中文':
        if target == "你叫什麽名字" or "你的名字" or "你叫什麽" or "你是誰":
            print('\n')
            print(list2_)
            print('\n')
            name = input()
            print('\n')
            print(f'你好,{name}')
            print('\n')
        else:
            print('\n')
            print(list1_)
            print('\n')
    elif laungre == 'English':
        if target == "What's your name" or "Who are you":
            print('\n')
            print(list2_2)
            print('\n')
            name = input()
            print('\n')
            print(f'Hi,{name}')
            print('\n')
        else:
            print('\n')
            print(list1_1)
            print('\n')
