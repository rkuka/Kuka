import random

while True:
    number = int(input('\n'"输入1启动程序，输入0退出程序。请输入:"))
    if number == 1:
        result = random.randint(1,40)
        print(result)
    elif number == 0:
        break