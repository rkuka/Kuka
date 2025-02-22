import tkinter
import turtle
import time
import sys

def add(a,b):
    result = a + b
    return result
def jian(a,b):
    result = a - b
    return result
def cheng(a,b):
    result = a * b
    return result
def chu(a,b):
    result = a / b
    return result
while True:
    q = input("请输入要运行的程序：")
    q1 = "函数计算"
    q2 = "for循环"
    q3 = "while循环"
    q4 = "内存查询"
    q5 = "逻辑运算"
    q6 = "位运算"

    if q == q1:
        n = int(input("请输入要输入的数字的小数位数：")) 
        if n == 0:
            a = int(input("请输入第一个数："))
            d = input("请输入运算符号(+,-,x,/):")
            b = int(input("请输入第二个数："))
            if d == "+":
                c = add(a,b)
                print('\n')
                print(c)
                print('\n')
                time.sleep(0.1)
                turtle.bgcolor('black')
                turtle.pencolor('white')
                turtle.goto(-100,0)
                turtle.speed(1)
                for i in range(len("结果是：{c}")):
                    turtle.write(f"结果是：{c}"[:i+1], align='left',
                                 font=('Times New Roman', 30, 'italic'))
                    time.sleep(0.1)
                turtle.delay()
                turtle.done()
                root = tkinter.Tk()
                label = tkinter.Label(root, text=f"结果是：{c}")
                label.pack()
                root.mainloop()
            elif d == "-":
                c = jian(a,b)
                print('\n')
                print(c)
                print('\n')
                time.sleep(0.1)
                turtle.bgcolor('black')
                turtle.pencolor('white')
                turtle.goto(-100,0)
                turtle.speed(1)
                for i in range(len("结果是：{c}")):
                    turtle.write(f"结果是：{c}"[:i+1], align='left',
                                 font=('Times New Roman', 30, 'italic'))
                    time.sleep(0.1)
                turtle.delay()
                turtle.done()
                root = tkinter.Tk()
                label = tkinter.Label(root, text=f"结果是：{c}")
                label.pack()
                root.mainloop()
            elif d == "x":
                c = cheng(a,b)
                print('\n')
                print(c)
                print('\n')
                time.sleep(0.1)
                turtle.bgcolor('black')
                turtle.pencolor('white')
                turtle.goto(-100,0)
                turtle.speed(1)
                for i in range(len("结果是：{c}")):
                    turtle.write(f"结果是：{c}"[:i+1], align='left',
                                 font=('Times New Roman', 30, 'italic'))
                    time.sleep(0.1)
                turtle.delay()
                turtle.done()
                root = tkinter.Tk()
                label = tkinter.Label(root, text=f"结果是：{c}")
                label.pack()
                root.mainloop()
            elif d == "/":
                c = chu(a,b)
                print('\n')
                print(c)
                print('\n')
                time.sleep(0.1)
                turtle.bgcolor('black')
                turtle.pencolor('white')
                turtle.goto(-100,0)
                turtle.speed(1)
                for i in range(len("结果是：{c}")):
                    turtle.write(f"结果是：{c}"[:i+1], align='left',
                                 font=('Times New Roman', 30, 'italic'))
                    time.sleep(0.1)
                turtle.delay()
                turtle.done()
                root = tkinter.Tk()
                label = tkinter.Label(root, text=f"结果是：{c}")
                label.pack()
                root.mainloop()
        else:
            a = float(input("请输入第一个数："))
            d = input("请输入运算符号(+,-,x,/):")
            b = float(input("请输入第二个数："))
            if d == "+":
                c = add(a,b)
                print('\n')
                print(c)
                print('\n')
                time.sleep(0.1)
                turtle.bgcolor('black')
                turtle.pencolor('white')
                turtle.speed(1)
                turtle.setpos(-100,0)
                for i in range(len("结果是：{c}")):
                    turtle.write(f"结果是：{c}"[:i+1], align='left',
                                font=('Times New Roman', 30, 'italic'))
                    time.sleep(0.1)
                turtle.delay()
                turtle.done()
                root1 = tkinter.Tk()
                label_0 = tkinter.Label(root, text=f"结果是：{c}")
                label_0.pack()
                root1.mainloop()
            elif d == "-":
                c = jian(a,b)
                print('\n')
                print(c)
                print('\n')
                time.sleep(0.1)
                turtle.bgcolor('black')
                turtle.pencolor('white')
                turtle.goto(-100,0)
                turtle.speed(1)
                for i in range(len("结果是：{c}")):
                    turtle.write(f"结果是：{c}"[:i+1], align='left',
                                 font=('Times New Roman', 30, 'italic'))
                    time.sleep(0.1)
                turtle.delay()
                turtle.done()
                root = tkinter.Tk()
                label = tkinter.Label(root, text=f"结果是：{c}")
                label.pack()
                root.mainloop()
            elif d == "x":
                c = cheng(a,b)
                print('\n')
                print(c)
                print('\n')
                time.sleep(0.1)
                turtle.bgcolor('black')
                turtle.pencolor('white')
                turtle.goto(-100,0)
                turtle.speed(1)
                for i in range(len("结果是：{c}")):
                    turtle.write(f"结果是：{c}"[:i+1], align='left',
                                 font=('Times New Roman', 30, 'italic'))
                    time.sleep(0.1)
                turtle.delay()
                turtle.done()
                root = tkinter.Tk()
                label = tkinter.Label(root, text=f"结果是：{c}")
                label.pack()
                root.mainloop()
            elif d == "/":
                c = chu(a,b)
                print('\n')
                print(c)
                print('\n')
                time.sleep(0.1)
                turtle.bgcolor('black')
                turtle.pencolor('white')
                turtle.goto(-100,0)
                turtle.speed(1)
                for i in range(len("结果是：{c}")):
                    turtle.write(f"结果是：{c}"[:i+1], align='left',
                                 font=('Times New Roman', 30, 'italic'))
                    time.sleep(0.1)
                turtle.delay(300)
                turtle.clear()
                turtle.done()
                root = tkinter.Tk()
                label = tkinter.Label(root, text=f"结果是：{c}")
                label.pack()
                root.mainloop()
    elif q == q2:
        a = int(input("请输入要循环的数字："))
        b = int(input("请输入要循环的次数："))
        for i in range(b):
            print(a)
            print('\n')
    elif q == q3:
        a = int(input("请输入要循环的数字："))
        b = int(input("请输入要循环的次数："))
        i = 0
        while i <= b:
            print(a)
            print('\n')
            i += 1
    elif q == q4:
        a = input("请输入要查询的数据类型(整数，小数，字符):")
        if a == "整数":
            b = int(input("请输入要查询的整数："))
            c = sys.getsizeof(b)
            print(c)
            turtle.setpos(-200,0)
            for i in range(len("内存是：{c}")):
                turtle.write(f"内存是{c}"[:i-1],align='left',font=("Times New Roman",30,"italic"))
                time.sleep(0.1)
            turtle.delay(300)
            turtle.clear()
            turtle.done()
            root = tkinter.Tk()
            label = tkinter.Label(root, text=f"内存是：{c}")
            label.pack()
            root.mainloop()
        elif a == "小数":
            b = float(input("请输入要查询的小数："))
            c = sys.getsizeof(b)
            print(c)
            turtle.setpos(-200,0)
            for i in range(len("内存是：{c}")):
                turtle.write(f"内存是{c}"[:i-1],align='left',font=("Times New Roman",30,"italic"))
                time.sleep(0.1)
            turtle.delay(300)
            turtle.clear()
            turtle.done()
            root = tkinter.Tk()
            label = tkinter.Label(root, text=f"内存是：{c}")
            label.pack()
            root.mainloop()
        elif a == "字符":
            b = input("请输入要查询的字符：")
            c = sys.getsizeof(b)
            print(c)
            turtle.setpos(-200,0)
            for i in range(len("内存是：{c}")):
                turtle.write(f"内存是{c}"[:i-1],align='left',font=("Times New Roman",30,"italic"))
                time.sleep(0.1)
            turtle.delay(300)
            turtle.clear()
            turtle.done()
            root = tkinter.Tk()
            label = tkinter.Label(root, text=f"内存是：{c}")
            label.pack()
            root.mainloop()
    elif q == q5:
        def lyu(a,b):
            result = a and b
            return result
        def lhuo(a,b):
            result = a or b
            return result
        c = input("请输入要进行的运算:")
        a = int(input("请输入第一个数字:"))
        b = int(input("请输入第二个数字:"))
        if c == "与":
            result = lyu(a,b)
            print(f"结果是:{result}")
        elif c== "或":
            result = lhuo(a,b)
            print(f"结果是:{result}")
    elif q == q6:
        def wyu(a,b):
            result = a & b
            return result
        def whuo(a,b):
            result = a | b
            return result
        def wyihuo(a,b):
            result = a ^ b
            return result
        def wqvfan(a):
            result = ~a
            return result
        def wzuoyi(a,b):
            result = a << b
            return result
        def wyouyi(a,b):
            result = a >> b
            return result
        c = input("请输入要进行的运算:")
        if c == "与":
            a = int(input("请输入第一个数字:"))
            b = int(input("请输入第二个数字:"))
            result = wyu(a,b)
            print(f"结果是:{result}")
        elif c== "或":
            a = int(input("请输入第一个数字:"))
            b = int(input("请输入第二个数字:"))
            result = whuo(a,b)
            print(f"结果是:{result}")
        elif c== "异或":
            a = int(input("请输入第一个数字:"))
            b = int(input("请输入第二个数字:"))
            result = wyihuo(a,b)
            print(f"结果是:{result}")
        elif c == "取反":
            a = int(input("请输入数字:"))
            result = wqvfan(a)
            print(f"结果是:{result}")
        elif c == "左移":
            int(input("请输入要进行位移的数字:"))
            int(input(f"请输入{c}的位数:"))
            result = wzuoyi(a,b)
            print(f"结果是:{result}")
        elif c == "右移":
            int(input("请输入要进行位移的数字:"))
            int(input(f"请输入{c}的位数:"))
            result = wyouyi(a,b)
            print(f"结果是:{result}")
    s = int(input("输入'1'继续运行，输入'0'结束运行："))
    if s == 1:
        continue
    elif s == 0:
        break