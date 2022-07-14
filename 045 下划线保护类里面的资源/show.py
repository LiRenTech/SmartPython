# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年07月12日
by littlefean
"""
from typing import *


class A:
    c = 5
    _c = 5
    __c = 5

    def __init__(self):
        self.b = 5
        self._b = 5
        self.__b = 5

    def test1(self):
        print(self.b)
        print(self._b)
        print(self.__b)
        self.f()
        self._f()
        self.__f()

    @classmethod
    def test2(cls):
        print(cls.c)
        print(cls._c)
        print(cls.__c)
        cls.g()
        cls._g()
        cls.__g()

    def f(self):
        ...

    def _f(self):
        ...

    def __f(self):
        ...

    @classmethod
    def g(cls):
        ...

    @classmethod
    def _g(cls):
        ...

    @classmethod
    def __g(cls):
        ...


class B(A):
    def __init__(self):
        super().__init__()

    def test3(self):
        print(super().c)
        print(super()._c)
        # print(super().__c)
        print(super().g())
        print(super()._g())
        # print(super().__g())


"""
类的内部
子类内部
类的外部 模块内部
模块的外部

"""


def main():
    b = B()
    # print(b.b)
    # print(b._b)
    # print(b.__b)
    # print(b.f())
    # print(b._f())
    # print(b.__f())

    a = A()
    print(a.b)
    print(a._b)
    print(a.__b)
    print(a.f())
    print(a._f())
    print(a.__f())
    print(A.c)
    print(A._c)
    print(A.__c)
    print(A.g())
    print(A._g())
    print(A.__g())
    return None


if __name__ == "__main__":
    main()
