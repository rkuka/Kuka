import random
import time
print('                                            作者     ：     顾家                                 ', '\n')
the_number = random.randint(1, 10)
print('     Hi！让我们来玩数字扫雷游戏吧！     ')
print('     现在你有3次机会，请慎重选择！     ')
print('\n', '                ROUND   ONE                ', '\n')
count = 0
while (count < 3):
    count += 1
    print(f"        现在是你第{count}次尝试        ")
    guess_number = int(input('请输入您的猜想: '))
    if (guess_number == the_number):
        print('\n',f"        恭喜你，第{count}次猜中了        ",'\n')
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
while (count < 3):
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
the_number = random.randint(1, 2)
print('\n', '                ROUND   THREE                ', '\n')
count = 0
while (count < 3):
    count += 1
    print('\n', f"        现在是你第{count}次尝试        ", '\n')
    guess_number = int(input('请输入您的猜想: '))
    if (guess_number == the_number):
        print('\n', f"        恭喜你，第{count}次猜中了        ", '\n')
        print('\n', '戴隆有喜欢赵紫妍', '\n')
        break
    elif (guess_number > the_number):
        print('\n', '猜大了，试着猜小点！', '\n')
    else:
        print('\n', '猜小了，试着猜大点！', '\n')
if (count > 3):
    print('\n', '                     你        输        了                     ', '\n')
time.sleep(30)
