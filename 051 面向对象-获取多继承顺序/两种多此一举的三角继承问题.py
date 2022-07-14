# -*- encoding: utf-8 -*-
"""
PyCharm 两种多此一举的三角继承问题
2022年07月11日
by littlefean
"""
from typing import *


class B:
    ...


class C(B):
    ...


# class A(B, C):
#     ...

class A(C, B):
    ...


def main():
    return None


if __name__ == "__main__":
    main()
