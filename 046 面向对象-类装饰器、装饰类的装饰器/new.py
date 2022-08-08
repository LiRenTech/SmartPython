# -*- encoding: utf-8 -*-
"""
PyCharm new
2022年07月23日
by littlefean
"""
from typing import *


class Deco:
    def __init__(self, flag):
        self.flag = flag
        ...

    def __call__(self, obj):
        obj.name = "newName" if self.flag else "oldName"
        return obj


@Deco(True)
class A:
    ...


def rD(flag: bool) -> Callable:
    def D(obj):
        obj.val = 15 if flag else 14
        return obj

    return D


@rD(True)
class A:
    ...


@rD(False)
class B:
    ...


def main():
    a = A()
    b = B()
    print(a.val)
    print(b.val)
    return None


if __name__ == "__main__":
    main()
