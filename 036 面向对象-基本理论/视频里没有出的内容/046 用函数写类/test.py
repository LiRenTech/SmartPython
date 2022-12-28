# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月04日
by littlefean
"""
from typing import *


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"({self.name}, {self.age})"
    def __call__(self, *args, **kwargs):
        # class Son:
        #     def __init__(self):
        #         self.val = None
        print(self, type(self))
        return Person


def toStr(self):
    return f"({self.left}, {self.age})"


Person.__str__ = toStr


# a.__str__ = toStr
# print(a)


def People(name: str, age: int):
    Res = type("obj", (), {})
    res = Res()

    # def res(): ...
    # res = {}

    def get(self, attName):
        return self.attName

    def setAtt(self, n, v):
        self.__dict__[n] = v

    res.__class__.__getattribute__ = get
    res.__class__.__setattr__ = setAtt

    res.age = age
    res.left = name

    res.__class__.__str__ = lambda self: f"{self.left}"
    res.__class__.__repr__ = res.__str__
    return res


def main():
    # p1 = People("小明", 15)
    # print(p1)
    #
    # print(Person.__dict__)
    # for k, v in Person.__dict__.items():
    #     print(k, "\t", v)
    # print(type(Person.__dict__))

    p = Person("xxx", 1)
    print(p)
    p()
    p()
    print(Person.__dict__)
    print(type(Person.__dict__))
    # print(p.__dict__)
    # print(getattr(p1, "name"))
    # print(p1)
    #
    # p2 = Person("小兲", 19)
    # print(p1.age)
    # print(p2.age)
    return None


if __name__ == "__main__":
    main()
