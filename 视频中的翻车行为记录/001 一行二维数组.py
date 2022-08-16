# -*- encoding: utf-8 -*-
"""
PyCharm 001 一行二维数组
7分48秒，小括号出来的东西是生成器，在python技巧030的3分27秒也出现了
10分20秒，下标越界
2022年08月16日
by littlefean
"""
from typing import *

from sys import getsizeof


def showList():
    """
    展示生成器和列表推导式的占用空间差异
    :return:
    """
    for length in range(1, 1000):
        # 生成器
        lst = [i ** 0.5 for i in range(length)]
        g = (i ** 0.5 for i in range(length))
        myList = [1]
        myG = iter(range(1))

        print(f"{length}："
              f"生成器空间：{getsizeof(g)}，推导式空间：{getsizeof(lst)}，"
              f"默认列表：{getsizeof(myList)}，默认生成器：{getsizeof(myG)}")


def iterTest():
    # 迭代器和for xx in列表不一样，迭代器迭代到什么地方它是有记忆的。
    g = iter([1, 2, 3, 4, 5, 6, 7])
    for n in g:
        print(n)
        if n == 3:
            break
    print("=====")
    for n in g:
        print(n)


def showType():
    print(
        type(range(1, 2)),  # range
        type(iter([1, 2])),  # list_iterator
        type(iter((1, 2, 3))),
        type(iter({1, 2, 3})),
        type((i ** 0.5 for i in range(5))),
        type(i ** 0.5 for i in range(5)),  # 中括号去掉
    )


def main():
    g = (i for i in range(10))
    print(list(g))
    g.send(12)
    g.close()
    # g.throw(123)
    return None


if __name__ == "__main__":
    main()
