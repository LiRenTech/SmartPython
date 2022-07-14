# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月11日
by littlefean
"""
from typing import *


class FF:
    ...


class G:
    ...


class D(FF):
    ...


class E(FF, G):
    ...


class F(G):
    ...


class B(D):
    ...


class C(E, F):
    ...


class A(B, C):
    ...


def main():
    for item in A.mro():
        print(item)
    return None


if __name__ == "__main__":
    main()
