# -*- encoding: utf-8 -*-
"""
PyCharm 对象生命周期理论
2022年07月02日
by littlefean
"""
from typing import *


class Person:
    def __init__(self):
        print("init!")
        ...

    def __new__(cls, *args, **kwargs):
        print("new 拦截对象的创建过程")
        ...

    def __del__(self):
        print("这个对象被回收了")


def main():
    p1 = Person()
    return None


if __name__ == "__main__":
    main()
