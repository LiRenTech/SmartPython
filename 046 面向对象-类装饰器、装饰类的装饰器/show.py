# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年07月12日
by littlefean
"""
from typing import *


def deco(obj):
    obj.b = 15
    return obj


@deco
class A:
    ...


def main():
    # func()
    a = A()
    print(a.__dict__)
    print(A.__dict__)
    return None


if __name__ == "__main__":
    main()
