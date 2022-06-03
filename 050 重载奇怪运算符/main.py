# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年06月03日
by littlefean
"""
from typing import *


class A:
    def __init__(self):
        ...

    def __call__(self, *args, **kwargs):
        ...

    def __matmul__(self, other):
        ...

    def __my__(self):
        ...


def main():
    a = A()
    b = A()
    c = a @ b
    # @ py3.5新增的矩阵乘法运算符
    # print([1, 2, 3] @ [4, 5, 6])r

    return None


if __name__ == "__main__":
    main()
