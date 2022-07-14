# -*- encoding: utf-8 -*-
"""
PyCharm 类运算
2022年07月13日
by littlefean
"""
from typing import *


class M(type):

    # 定义一些类的操作

    def __lshift__(self, other):
        # 类1 << 类2
        return self

    def __invert__(self):
        print("-")
        return self

    def __add__(self, other):
        # 返回一个新的类，整合两个类的资源
        return M(self.__name__ + other.__name__, (), self.__dict__ | other.__dict__)

    def __le__(self, other):
        # 类1 <<= 类2
        for k, v in other.__dict__.items():
            if k.startswith("__"):
                continue
            setattr(self, k, v)

    print("in meta")
    ...


class A(metaclass=M):
    DATA = 15
    INFO = 15
    ...


class C:
    C_DATA = 15


def main():
    print("in main\n")

    # B = A + int + dict
    #
    # print(B, type(B))
    # for item in B.__dict__:
    #     print(item)
    #
    # print(B.real)

    A <= C
    print(A.__dict__)
    return None


if __name__ == "__main__":
    main()
