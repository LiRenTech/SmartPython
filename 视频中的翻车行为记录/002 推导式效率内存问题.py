# -*- encoding: utf-8 -*-
"""
PyCharm 002 推导式效率内存问题
2022年08月22日
by littlefean
"""
from typing import *
from memory_profiler import profile


@profile
def memoryTest():
    lst0 = list(range(100))
    lst1 = list(range(100000))
    lst2 = [i ** i for i in range(10000)]


def main():
    memoryTest()
    return None


if __name__ == "__main__":
    main()
