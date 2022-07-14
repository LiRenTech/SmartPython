# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月01日
by littlefean
"""
from typing import *


class A:
    def __init__(self, n=1):
        self.n = n
        print("init")

    def __call__(self, *args, **kwargs):
        print("call")
        return A

    def __getitem__(self, item):
        return self


def main():
    # a = A()[:]()()[:]()()()()[:][::]()()[:]()()()[:]()()
    # print(a)

    a = A()
    a.__class__ = a

    print(type(a))
    return None


if __name__ == "__main__":
    main()
