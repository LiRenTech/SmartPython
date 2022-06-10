# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年06月10日
by littlefean
"""
from typing import *
from itertools import product


def main():
    count = 0
    # 三重循环
    for x, y, z in product(range(5), range(5), range(5)):
        print(x, y, z)
        count += 1
    print(count)  # 5 * 5 * 5

    return None


if __name__ == "__main__":
    main()
