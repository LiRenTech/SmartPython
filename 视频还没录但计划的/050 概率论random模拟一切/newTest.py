# -*- encoding: utf-8 -*-
"""
PyCharm newTest
2022年07月23日
by littlefean
"""
from typing import *
from functools import lru_cache


@lru_cache()
def fab(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fab(n - 1) + fab(n - 2)


def main():
    for i in range(1000):
        print(i, fab(i + 1))
    return None


if __name__ == "__main__":
    main()
