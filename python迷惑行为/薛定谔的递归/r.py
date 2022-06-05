from random import random

c = 1


def f():
    global c
    c *= 2
    print(c)
    return f if random() < 0.5 else f()


# 等效写法
# f()
# f()
# f()

f()()()
