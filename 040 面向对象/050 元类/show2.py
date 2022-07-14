# -*- encoding: utf-8 -*-
"""
PyCharm show2
2022年07月13日
by littlefean
"""
from typing import *


class MyMeta(type):
    def __lshift__(self, other):
        for k, v in other.__dict__.items():
            setattr(self, k, v)
        return self
    ...


class A(metaclass=MyMeta):
    ...


def main():
    # A << int
    print(A.__dict__, len(A.__dict__))

    # A << int

    A << int << dict << set

    print(A.__dict__, len(A.__dict__))

    return None


if __name__ == "__main__":
    main()
