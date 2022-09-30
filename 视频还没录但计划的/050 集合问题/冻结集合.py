# -*- encoding: utf-8 -*-
"""
PyCharm 冻结集合
2022年06月03日
by littlefean
"""
from typing import *


def main():
    fs = frozenset({1, 2, 3, 4})
    s = {1, 2, fs}
    print(s)  # 集合可以套冻结集合

    # 直接查询 O1
    print(frozenset({1, 2, 3, 4}) in s)
    print(frozenset((1, 2, 3, 4)) in s)
    print(frozenset([1, 2, 3, 4]) in s)
    return None


if __name__ == "__main__":
    main()
