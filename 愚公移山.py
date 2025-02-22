import turtle
import time

turtle.bgcolor('black')

def ___moutain___():
    turtle.color('brown','brown')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-200,-100)
    turtle.pendown()
    turtle.forward(400)
    turtle.left(135)
    turtle.forward(400)
    turtle.left(112.5)
    turtle.forward(315)
    turtle.end_fill()

def ___river___():
    turtle.color('white','blue')
    turtle.penup()
    turtle.goto(-380,-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(260)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(160)
    turtle.end_fill()

___moutain___()
___river___()

turtle.done()