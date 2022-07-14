# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月13日
by littlefean
"""
from typing import *


class A:
    DATA = 0

    def __init__(self):
        self.val = 0

    @classmethod
    def create(cls) -> Type["A"]:
        return cls

    ...


def main():
    a = A.create()
    number: int
    number = 3
    return None


if __name__ == "__main__":
    main()
