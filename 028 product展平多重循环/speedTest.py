# -*- encoding: utf-8 -*-
"""
PyCharm speedTest
2022年06月12日
by littlefean
"""
from typing import *

from itertools import product
from time import perf_counter


def main():
    t1 = perf_counter()
    c = 0
    d = 0

    for i, j, k, l in product(range(100), range(100), range(100), range(100)):
        d += 1

    t2 = perf_counter()

    for i in range(100):
        for j in range(100):
            for k in range(100):
                for l in range(100):
                    c += 1

    t3 = perf_counter()

    print(t2 - t1, t3 - t2)
    # 0.9892027 2.1248509
    # 3.8394042 4.7534811999999995
    # 经过测试发现反而慢了

    return None


if __name__ == "__main__":
    main()
