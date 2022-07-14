# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年07月11日
by littlefean
"""
from typing import *
from types import MappingProxyType


def main():
    arr = [1, 2, 3, 4, 5]
    t = tuple(arr)

    s = {1, 2, 3, 4}
    fs = frozenset(s)
    print(1 in fs)

    s = {1, 2, 3, frozenset({2})}
    return None


if __name__ == "__main__":
    main()
