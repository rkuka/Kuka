import turtle
import math

turtle.bgcolor("black")

turtle.speed(0)

def X(h,i):
    jd = math.radians(i)
    return h * math.cos(jd)

def Y(g,i):
    jd = math.radians(i)
    return g * math.sin(jd)

def floor():
    turtle.color("white","pink")
    turtle.begin_fill()
    for i in range(360):
        x = X(150,i)
        y = Y(60,i)
        turtle.setpos(x,y)
        turtle.setpos(x,y+120)
    turtle.end_fill()

floor()

turtle.done()