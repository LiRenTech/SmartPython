# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年08月23日
by littlefean
"""
from typing import *

from timeit import timeit


def xor():
    a = 1534
    a >>= 1


def add():
    a = 1534
    a /= 2


def main():
    print(timeit(add, number=1000_1000))
    print(timeit(xor, number=1000_1000))
    # 反而还慢了，位运算

    return None


if __name__ == "__main__":
    main()
