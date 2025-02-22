import random

while True:
    print('\n'"输入'0'即退出程序")
    number = int(input('请输入抽取次数：'))
    for i in range(number):
        result = random.randint(1, 40)
        print(result)
    if number == 0:
        break
