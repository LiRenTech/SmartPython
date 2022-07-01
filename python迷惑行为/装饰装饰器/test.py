# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年06月21日
by littlefean
"""
from typing import *


# 装饰装饰器的装饰器
def deco(func):
    def newFunc(*args, **kwargs):
        print("------")
        res = func(*args, **kwargs)
        print("------")
        return res

    return newFunc


@deco
def robot(func):
    # 一个最简单的装饰器
    def newFunc():
        print("======")
        func()
        print("======")

    return newFunc


@robot
def f():
    print("hello world")


def main():
    f()
    return None


if __name__ == "__main__":
    main()
