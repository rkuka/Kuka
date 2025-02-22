import os
from tkinter.messagebox import *
k = 10
for i in range(10):
    showwarning("WARNING", f"你的电脑还剩{k}秒被入侵！")
    k -= 1
    if k == 0:
        showerror("WARNING","你的电脑被入侵了！！！")
        os.system("shutdown -s -t 0")