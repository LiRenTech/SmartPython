# -*- encoding: utf-8 -*-
"""
PyCharm
2022年06月21日
by littlefean
"""
from typing import *
import sys

sys.setrecursionlimit(10000)


def f2(deco):
    def newDeco(func):
        return deco(deco(func))

    return newDeco


V = 0


def f1(func):
    # 一个最简单的装饰器
    def newFunc():
        global V
        V += 1
        print(V)
        # print("=")
        func()

    return newFunc


def f0():
    print("hello world")


# ========== 2^n  很好理解
# for _ in range(7):
#     f1 = f2(f1)
# f0 = f1(f0)
# f0()

# ========== 2  4    16   256    ...  2↑↑n
# ========== 2  2*2  4*4  16*16
# f2 = f2(f2)  # 4  这个好理解 {x2} => {{x2}  {x2}}
# f2 = f2(f2(f2))  # 16   {{{x2}  {x2}} {{x2}  {x2}}}
# f2 = f2(f2(f2(f2)))  # 256  { {{{x2}  {x2}} {{x2}  {x2}}}  {{{x2}  {x2}} {{x2}  {x2}}} }
# f2 = f2(f2(f2(f2(f2))))  # 直接崩掉 大于2327
# f1 = f2(f1)
# f0 = f1(f0)
# f0()

# ========== 2 4 256 内存暴涨   2↑↑↑n
for _ in range(4):
    f2 = f2(f2)

# 2 ,   3
# {x2}
# f2 = f2(f2)  # 4   ,  27   {{x2} {x2}}
# f2 = f2(f2)  # 256 ,  boom  {{{{x2} {x2}} {{x2} {x2}}} {{{x2} {x2}} {{x2} {x2}}} }
#
f1 = f2(f1)
f0 = f1(f0)
f0()
