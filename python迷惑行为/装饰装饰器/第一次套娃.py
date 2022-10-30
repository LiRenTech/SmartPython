# -*- encoding: utf-8 -*-
"""
PyCharm simply
2022年10月24日
pycharm中选中输出的=号然后按 ctrl F ，可以查看有多少个=号，进而获悉有多少层
by littlefean
"""
from typing import *


def deco2(robotFunc):
    def newRobotFunc(func):
        return robotFunc(robotFunc(func))

    return newRobotFunc


# 2^n级别增长
@deco2
@deco2
@deco2
@deco2
@deco2
@deco2
def deco1(func):
    # 一个最简单的装饰器
    def newFunc():
        print("=")
        func()

    return newFunc


@deco1
def f():
    print("hello world")


def main():
    f()
    return None


if __name__ == "__main__":
    main()
