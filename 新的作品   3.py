import turtle
import time

def top_cake():
    turtle.color("black","pink")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()

def first_cake():
    turtle.color("black","pink")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

def second_cake():
    turtle.color("black","pink")
    turtle.begin_fill()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(150)
    turtle.end_fill()

top_cake()
first_cake()
second_cake()

time.sleep(10)
