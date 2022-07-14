# -*- encoding: utf-8 -*-
"""
PyCharm 基本数据类型也是对象
2022年07月02日
by littlefean
"""
from typing import *


def main():
    # class int(object):
    a = int()
    print(a)

    b = str()
    print(b)

    c = float()
    print(c)

    # 这个n可以点出来很多
    n = 1
    print(n)
    print(n.imag)
    print(n.numerator)
    print(n.denominator)
    print(n.conjugate())
    return None


if __name__ == "__main__":
    main()
