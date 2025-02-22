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
        if target == "你叫什么名字":
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
        if target == "你叫什麽名字":
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
        if target == "What's your name":
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
