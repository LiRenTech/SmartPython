# -*- encoding: utf-8 -*-
"""
PyCharm 概率论
2022年07月03日
by littlefean
"""
from typing import *

from random import *


def main():
    for _ in range(100):
        u = uniform(1, 10000)
        t = triangular(1, 10000, 200)
        # 生成1到1万的随机数，生成的值更接近第三个数

        print(int(t), end="\t\t\t")
        print(int(u))
    return None


if __name__ == "__main__":
    main()
