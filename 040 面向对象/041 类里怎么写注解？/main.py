# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年07月02日
by littlefean
"""
import typing
from typing import *


class A:
    def __init__(self):
        self.val = 15

    def f(self) -> "A":
        return self

    @classmethod
    def g(cls) -> Type["A"]:
        return cls


class B:
    def __init__(self):
        self.value = 10

    @staticmethod
    def f() -> A:
        return A()

    @staticmethod
    def g() -> Type[A]:
        return A


def main():
    a = A()
    print(a.f().f().f().f().f().val)
    print(a.g()().g().g()().g().g()())

    return None


if __name__ == "__main__":
    main()
