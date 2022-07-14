# -*- encoding: utf-8 -*-
"""
PyCharm test3
2022年07月11日
by littlefean
"""
from typing import *


class E:
    ...


class D(E):
    ...


class C(D, E):
    ...


class B:
    ...


class A(B, C):
    ...


def main():
    return None


if __name__ == "__main__":
    main()
