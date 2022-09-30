# -*- encoding: utf-8 -*-
"""
PyCharm 前缀和
2022年08月10日
by littlefean
"""
from typing import *
from itertools import accumulate


def main():
    arr = [1, 2, 3, 4, 5]
    acc = list(accumulate(arr, initial=0))
    acc2 = list(accumulate(arr, initial=1000))
    print(acc)
    print(acc2)
    return None


if __name__ == "__main__":
    main()
