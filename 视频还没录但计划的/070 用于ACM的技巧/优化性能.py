# -*- encoding: utf-8 -*-
"""
PyCharm 优化性能
2022年08月10日
by littlefean
"""
from typing import *
import sys
import gc

sys.setrecursionlimit(5001)
print(gc.get_threshold())
gc.set_threshold(700, 10, 5)


def main():
    return None


if __name__ == "__main__":
    main()
