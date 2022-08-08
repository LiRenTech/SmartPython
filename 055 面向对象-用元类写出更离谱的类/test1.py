# -*- encoding: utf-8 -*-
"""
PyCharm test1
2022年07月12日
by littlefean
"""
from typing import *


class MyType(type):

    def __str__(self):
        return "ABABA"

    def __add__(self, other):
        print("add", other)

    ...


class A(metaclass=MyType):
    def __str__(self):
        return "obj"

    ...


def main():
    a = A()
    print(a)
    print(A)
    print(A + A)

    return None


if __name__ == "__main__":
    main()
