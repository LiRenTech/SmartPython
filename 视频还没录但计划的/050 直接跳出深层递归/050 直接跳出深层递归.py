"""
PyCharm test
2022年06月17日
by littlefean
"""
from random import random
from typing import *


def dfs(n):
    if n < 0:
        return
    print(">", n)
    dfs(n - 1)
    print("<", n)


class DeepException(BaseException):
    ...


def dfs2(n):
    if n < 0:
        raise DeepException
    print(">>", n)
    dfs2(n - 1)
    print("<<", n)


def dfsBi(n, count):
    if n < 0:
        return
    if n > 100:
        return
    if count > 500:
        return
    print(">" * n)
    dfsBi(n - 1, count + 1) if random() < 0.5 else dfsBi(n + 1, count + 1)
    print("-" * n)


def dfsBi_(n, count):
    if count > 500:
        raise DeepException
    if n < 0:
        return
    if n > 100:
        return
    # if count > 500:
    #     raise DeepException
    print(">" * n)
    dfsBi_(n - 1, count + 1) if random() < 0.5 else dfsBi_(n + 1, count + 1)
    print("-" * n)


def main():
    # try:
    #     dfs2(10)
    # except DeepException:
    #     ...
    def f():
        # 问题，压栈的那些dfs2去哪里了？直接消失了？
        try:
            dfsBi_(50, 0)
        except DeepException:
            ...

    print("f1")
    f()
    print("f2")
    return None


if __name__ == "__main__":
    main()
