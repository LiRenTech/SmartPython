# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年05月23日
by littlefean
"""

import itertools
from typing import *


def main():
    a = 1j
    b = 1 + 1j
    c = complex(1, 1)
    print(b == c)

    # 可以当成坐标用，用于快速判断某一个点是否在某一个区域里
    s = {complex(x, y) for y, x in itertools.product(range(10), range(10))}
    print(s)

    return None


if __name__ == "__main__":
    main()
