import pywifi
import turtle
import time

turtle.penup()
turtle.goto(-200,0)
for i in range(len(f"你电脑网卡被关闭了，哈哈哈！")):
    turtle.write(f"你电脑网卡被关闭了，哈哈哈！"[:i+1],
                 align="left",font=("Times New Roman", 30, "italic"))
    turtle.delay()
    
wifi = pywifi.PyWiFi()
card = wifi.interfaces()[0]
card.disconnect()

time.sleep(3)
