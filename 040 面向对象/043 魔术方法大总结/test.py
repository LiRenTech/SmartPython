# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月10日
by littlefean
"""
from typing import *
from math import *
import sys


class A:
    def __sizeof__(self):
        print("......")  # 在此基础上加
        return 1000000

    def __trunc__(self):
        print("???")
        return 5

    def __invert__(self):
        ...


def main():
    a = A()
    print(~a)
    print(trunc(a))
    print(sys.getsizeof(a))
    return None


if __name__ == "__main__":
    main()
