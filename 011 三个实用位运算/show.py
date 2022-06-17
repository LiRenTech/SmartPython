# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年06月17日
by littlefean
"""
from typing import *


def main():
    left = 1
    right = 1000
    mid = (left + right) >> 1
    print(mid)
    # 比如说求中点位置，就可以用位运算，相当于除以二
    return None


if __name__ == "__main__":
    main()
