# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年06月29日
by littlefean
"""
from typing import *


def func1(a, b, c):
    ...


def func2(a, *b, **c):
    ...


# 非法
# def func3(a, *b, *c):
#     ...

# 非法
# def func4(a, b, **c, *d):
#     ...

# 得到结论，*？ 与**？只能有一个，并且顺序有讲究

def func4(*d, a, **b):
    ...



# def f(a, b, /, c, d, *, e, h):  / 是3.8里面的
#     print(a, b, c, d, e, h)


def main():
    return None


if __name__ == "__main__":
    main()
