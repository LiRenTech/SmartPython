# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月12日
by littlefean
"""
from typing import *
# from show import *
import show


def main():
    A = show.A
    a = A()
    print(a.b)
    print(a._b)
    # print(a.__b)
    print(a.f())
    print(a._f())
    # print(a.__f())
    print(A.c)
    print(A._c)
    # print(A.__c)
    print(A.g())
    print(A._g())
    # print(A.__g())
    return None


if __name__ == "__main__":
    main()
