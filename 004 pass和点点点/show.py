# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年06月17日
by littlefean
"""
from typing import *


# ... 可以写在注解里面
def test(a: ..., b: ...) -> ...:
    ...


# 有一个类我还不知道怎么写，我可以先写个占位符
class A:
    ...


class B:
    pass


def f():
    ...


def g():
    pass


def main():
    # 写个空循环
    for _ in range(10):
        ...

    # 经过测试发现 点点点和pass做空循环速度是一样的。

    for _ in range(100):
        ...
        ...
        ...
        ...

    # 经过测试发现，这样写四个，并没有出现速度慢了四倍的情况

    print(id(...) == id(Ellipsis))
    # print(id(...) == id(ellipsis))  # 没有小写开头的东西了，因为是单例了，虽然pycharm里这个单词还会变蓝

    print(type(...))
    print(type(Ellipsis))
    print(Ellipsis.__class__)
    print(Ellipsis.__class__())
    print(Ellipsis.__class__.__name__)
    print(Ellipsis.__class__.__bases__)
    print(Ellipsis.__class__.__class__)
    return None


if __name__ == "__main__":
    main()
