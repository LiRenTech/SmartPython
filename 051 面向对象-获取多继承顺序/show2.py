# -*- encoding: utf-8 -*-
"""
PyCharm show2
2022年07月12日
by littlefean
"""
from typing import *


class D:
    ...


class Y(D):
    ...


class J(D):
    ...


class S(J, Y):
    ...


def main():
    print(S.mro())
    print(J.mro())
    print(S.__bases__)
    print(J.__bases__)
    return None


if __name__ == "__main__":
    main()
