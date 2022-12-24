# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年08月10日
by littlefean
"""
from typing import *

import sys

a = sys.stdin.buffer.readline()
# 能快 16ms ，在一些极限排名上可以拉扯一下

print(a)


def main():
    if sys.hexversion == 50792688:  # 中键点进去不一定准确
        sys.stdin = open("input.txt")
    else:
        input = sys.stdin.readline
    MOD = 10 ** 9 + 7
    return None


if __name__ == "__main__":
    main()
