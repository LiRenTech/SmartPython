# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年06月21日
by littlefean
"""
from typing import *


def main():
    a = 15
    b = 155
    c = 1555
    a, b, c = c, b, a
    print(a, b, c)

    d, *e = a, b, c
    print(d, e)  # 1555 [155, 15]

    f, *g, h = a, b, c, d, e  # 1555 [155, 15, 1555] [155, 15]
    print(f, g, h)

    return None


if __name__ == "__main__":
    main()
