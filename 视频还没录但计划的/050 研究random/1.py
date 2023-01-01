import random
import types
from typing import *

def f1(func: types.FunctionType, *args, **kwargs):
    """检测随机数范围，算法是撤硕里想出来的（doge"""
    a = []
    for _ in range((sum(args) ** 3) or (3 ** 3)):
        a.append(func(*args, **kwargs))
    a = list(set(a))  # 去重
    print(func.__qualname__, args, "范围:", min(a), "~", max(a), "其中一个结果:", random.choice(a))

def f2(func: types.FunctionType, *args, **kwargs):
    """检测随机选择的范围"""
    a = []
    for _ in range(len(args[0]) ** 3):
        a.append(func(*args, **kwargs))
    a = list(set(a))  # 去重
    print(func.__qualname__, args, "范围:", a)

# 1. 最常用的几个方法
f1(random.randint, 1, 10)
f1(random.random)  # 憋想了，这个范围算不准的，只能看文档和docstring
f2(random.choice, ("这究竟是多少年前的事了呢？", "我不到啊。", "所以说，", "你们是从世界之外，", "漂游过来的？"))
print(random.shuffle([1, 2, 3]))  # shuffle要传可修改的iterable
f1(random.randrange, 10)
f1(random.randrange, 1, 11)

# 2. Random对象
myrandomobj = random.Random(f"1292734{random.randint(111111111111111, 111111919181000810)}1111113412341234{114514 ** 2}")  # 每个seed对应一个随机数
f1(myrandomobj.randint, 1, 10)
