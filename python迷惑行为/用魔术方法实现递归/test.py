# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年10月18日
by littlefean
"""
from typing import *


def deco(f):
    def newF(this, i):
        f(this, i)
        print("循环中", i)

    return newF


# 用魔法装饰魔法
class N:
    @deco
    def __matmul__(self, i):
        if i == -1:
            return
        else:
            self @ (i - 1)

    def __and__(self, n):
        return 1 if n == 1 else n * (self & n - 1)


def main():
    jie = N()
    print(jie & 3)

    return None


if __name__ == "__main__":
    main()
