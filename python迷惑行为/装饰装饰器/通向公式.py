# -*- encoding: utf-8 -*-
"""
PyCharm mathTest
此模块用于找出最终套娃的时候的 通项公式
2022年10月30日
by littlefean
"""
from typing import *


def main():
    def f(x):
        return 2 ** (2 ** x - 1)

    dp = [1]
    dp.extend((dp[-1] * dp[-1]) << 1 for _ in range(10))
    for i, n in enumerate(dp):
        print(n)
        print(f(i))
        print()
    return None


if __name__ == "__main__":
    main()
