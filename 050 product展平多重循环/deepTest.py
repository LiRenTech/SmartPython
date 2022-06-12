# -*- encoding: utf-8 -*-
"""
PyCharm deepTest
2022年06月12日
by littlefean
"""
from typing import *
from itertools import product


def a():
    c = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                for l in range(100):
                    c += 1


def b():
    d = 0
    for i, j, k, l in product(range(100), range(100), range(100), range(100)):
        d += 1


def main():
    import dis
    dis.dis(a)
    print("-" * 100)
    dis.dis(b)
    return None


if __name__ == "__main__":
    main()
