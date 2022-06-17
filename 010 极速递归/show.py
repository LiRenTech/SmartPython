# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年06月17日
by littlefean
"""
from typing import *

# 先引入
from functools import lru_cache


# 装饰你要递归的函数
@lru_cache(None)
def fab(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fab(n - 1) + fab(n - 2)


def main():
    for i in range(1, 101):
        print(i, fab(i))
    """
    注意点：
    装饰的函数的每一个参数都是要可哈希的，
    int、float、str都可以，但是传了一个list不可以。
    """
    return None


if __name__ == "__main__":
    main()
