# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年06月21日
by littlefean
"""
from typing import *


def func():
    """
    这个函数是干啥啥的
    :return: 返回了个东西是啥啥啥
    """


def main():
    # help()  # 直接进入交互式

    # 传入一些奇奇怪怪的对象，会显示出这个对象的类的注释
    help(1)
    help(...)
    help(())

    # 打印注释文档
    help(func)
    import math
    help(math)

    # 关键字
    help("def")
    help("none")  # 这个不可以
    help("async")
    help("ASYNC")  # 不小心大写了也可以

    # 符号
    help(">>=")  # 打印出运算符优先级

    # help
    help(help)  # 他自己就是一个对象，会打印出他自己的注释

    return None


if __name__ == "__main__":
    main()
