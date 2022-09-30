# -*- encoding: utf-8 -*-
"""
PyCharm t2
2022年07月23日
by littlefean
"""
from typing import *


def main():
    def f(n):
        return (-1) ** (n * (n - 1) / 2)

    res = ""
    for i in range(1, 10000):
        res += "-" if f(i) < 0 else "+"
    print(res)

    return None


if __name__ == "__main__":
    main()
