# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年06月17日
by littlefean
"""
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


def main():
    try:
        dfs2(10)
    except DeepException:
        ...

    # 问题，压栈的那些dfs2去哪里了？直接消失了？

    return None


if __name__ == "__main__":
    main()
