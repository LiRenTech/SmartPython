# -*- encoding: utf-8 -*-
"""
PyCharm 输入技巧
2022年08月10日
by littlefean
"""
from typing import *


def main():
    # 一行输入两个变量
    a, b = map(int, input().split())
    # 一行输入n个变量用一个元组接收
    *c, = map(int, input().split())

    print(a, b, c)

    return None


if __name__ == "__main__":
    main()
