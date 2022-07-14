# -*- encoding: utf-8 -*-
"""
PyCharm test2
2022年07月11日
by littlefean
"""
from typing import *


class E:
    ...


class F:
    ...


class G:
    ...


class B(E):
    ...


class C(F):
    ...


class D(G):
    ...


class A(B, C, D):
    ...


def main():
    for item in A.mro():
        print(item)
    return None


if __name__ == "__main__":
    main()
