# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年05月23日
by littlefean
"""
from typing import *


def main():
    a = 1j
    b = 1 + 1j
    c = complex(1, 1)
    print(b == c)

    # 可以当成坐标用，用于快速判断某一个点是否在某一个区域里
    s = set()
    for y in range(10):
        for x in range(10):
            v = complex(x, y)
            s.add(v)
    print(s)

    return None


if __name__ == "__main__":
    main()
