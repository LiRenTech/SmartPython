# -*- encoding: utf-8 -*-
"""
PyCharm 005 函数注解
0分22秒 函数注释，是三引号的东西
如何获取文档注释
如何书写文档注释

2022年08月17日
by littlefean
"""
from typing import *


def func(a: int, b: float):
    """
    vege hjuu ui gjufmdede
    Args:
        a: sdfasdf
        b: dsfasdds

    Returns: fj

    """
    ...


def main():
    # 注释
    print(func.__doc__)
    func(1, 1)

    return None


if __name__ == "__main__":
    main()
