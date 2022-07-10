# -*- encoding: utf-8 -*-
"""
PyCharm super写法
2022年07月07日
by littlefean
"""
from typing import *


class A:
    def __init__(self):
        self.a = 12


class B(A):
    def __init__(self):
        super().__init__()  # 写这一行就行
        self.b = 155


def main():
    return None


if __name__ == "__main__":
    main()
