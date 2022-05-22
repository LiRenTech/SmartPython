a = 15

a == 15 if print("yes1") else print("no1")
print("yes2") if a == 15 else print("no2")

if bool(None):
    print(111)
else:
    print(222)

if print("if if"):
    print(111)





# 嵌套写法
score = 83
if score in range(101):
    if score < 60:
        print("不合格")
    else:
        print("合格")
else:
    print("成绩错误")

print("不合格") if score < 60 else print("合格") if score in range(101) else print("成绩错误")

from random import random

def do():
    ...

if random() < 0.5:
    do()

do() if random() < 0.5 else ...



value = 65

res = "ok" if value > 60 else "no"
# print("空") if name == "" elif print("找到人了") else print("没找到")
