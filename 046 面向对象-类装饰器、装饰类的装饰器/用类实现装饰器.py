# -*- encoding: utf-8 -*-
"""
PyCharm 用类实现装饰器
2022年07月02日
by littlefean
"""
from typing import *


class Check(object):
    """类装饰器"""

    def __init__(self, fn):
        """
        传入的是被装饰的原的函数
        """
        self.__fn = fn

    def __call__(self, *args, **kwargs):  # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用
        print("登录")  # 在这之前可以写登录代码
        self.__fn()


def main():

    def deco(func):
        def newFunc():
            func()

        return newFunc

    def f():
        ...

    g = deco(f)   # 这才是@语法糖的本质过程

    return None


if __name__ == "__main__":
    main()
