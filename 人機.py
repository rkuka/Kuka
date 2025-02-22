import time

while True:

    laungry = input("请选择一门语言（简体中文/繁體中文）：")

    if laungry == "简体中文":
        print('\n')
        programe_1 = input("请选择要启动的程序：")
        print('\n')
        if programe_1 == "人机":
            question_1 = input("'人机' 已启动，请输入问题：")
            list1 = [
               '正在分析问题，请稍侯…………', '正在分析逻辑，请稍候…………', '正在爬取目标信息，请稍候…………',
                '正在数据分析，请稍候…………','正在计算结果，请稍候…………', '正在分角度作答，请稍候…………',
                '正在作答，请稍候…………', '让您久等了，以下是问题的答案，请笑纳'
            ]
            print('\n')
            if question_1 == "初中，女同学慌张的把一包粉色的东西放进袋子里，这个东西是什么":
                for i in list1:
                    print(i)
                    print('\n')
                    time.sleep(1)
                print("客观：")
                print('\n')
                print("纸巾：4%")
                print("湿巾：5%")
                print("零食：1%")
                print("卫生巾：90%")
                print('\n')
                time.sleep(2)
                print("主观：")
                print('\n')
                print("因为对方是初中生，正处青春期，并且是女生，所以很大可能是'卫生巾'，")
                print("且因为对方很慌张的将其收起，所以大概是比较隐私的物品")
                print('\n')
                time.sleep(1)
                print("由此可见：")
                print('\n')
                print("该物品极大可能是'卫生巾'")
                print('\n')

    elif laungry == "繁體中文":
        print('\n')
        programe_2 = input("請選擇要啓動的程序：")
        print('\n')
        if programe_2 == "人機":
            question_2 = input("'人機'已啓動，請輸入問題：")
            list2 = [
                '正在分析問題，請稍候…………', '正在分析邏輯，請稍候…………', '正在爬取目標信息，請稍候…………',
                '正在數據分析，請稍候…………', '正在計算結果，請稍候…………', '正在分角度作答，請稍候…………',
                '正在作答，請稍候…………', '讓您久等了，以下是問題的答案，請笑納'
            ]
            print('\n')
            if question_2 == "上一個問題中的女生是誰":
                for i in list2:
                    print(i)
                    print('\n')
                    time.sleep(1)
                print("客觀：")
                print('\n')
                print("根據七十一便利店的監控，對方是廣州市第四中學的學生")
                print("根據地理位置分析，應該是康園的學生，推斷是初二或初三的學生")
                print("根據七十一便利店記錄的時間，應該是初二級放學的時間")
                print("根據廣州市第四中學附近的監控所示，該生從二樓樓道旁的班級走出，應該是九班")
                print("依據其身高，對比得出其為初二九班的趙紫妍")
                time.sleep(2)
                print('\n')
                print("主觀：")
                print('\n')
                print("該問題無需從主觀角度回答，因爲客觀方面證據已充足")
                print('\n')
                time.sleep(1)
                print("由此可見：")
                print('\n')
                print("該人極大可能是'趙紫妍'")
                print('\n')
                time.sleep(2)
    else:
        break