# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月01日
by littlefean
"""
from typing import *


class A:
    def __init__(self):
        self.val = 100
    ...


def main():

    a = type(type(type(A())())())()

    print(a.val)

    b = A()
    c = b.__class__().__class__().__class__()
    d = type.__class__
    print(d)
    print(A().__class__.__name__)

    return None


if __name__ == "__main__":
    main()
