# -*- encoding: utf-8 -*-
"""
PyCharm
2022年06月21日
by littlefean
"""
from typing import *


# 装饰装饰器的装饰器
def deco(robotFunc):
    def newRobotFunc(func):
        return robotFunc(robotFunc(func))

    return newRobotFunc


def robot(func):
    # 一个最简单的装饰器
    def newFunc():
        print("=")
        func()

    return newFunc


for _ in range(10):  # 2^n
    robot = deco(robot)


@robot
def f():
    print("hello world")


f()
