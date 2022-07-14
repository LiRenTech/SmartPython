# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月12日
by littlefean
"""
from typing import *
import abc


class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def f(self):
        ...

    @abc.abstractmethod
    def g(self):
        ...


class B(A):
    def f(self):
        pass

    def g(self):
        pass

    ...


def main():
    return None


if __name__ == "__main__":
    main()
