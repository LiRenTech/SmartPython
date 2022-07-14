# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年07月11日
by littlefean
"""
from typing import *
from random import choice


class Person:
    _FirstName = ["岳", "王", "李", "张", "赵"]
    _LastName = ["三", "建国", "宇航", "超", "子航", "鹏"]

    def __init__(self, name):
        self.name = name

    def say(self):
        print(f"大家好我叫{self.name}")

    @classmethod
    def createMan(cls):
        return cls(choice(cls._FirstName) + choice(cls._LastName))

    def __hash__(self):
        return 15863485

    def __str__(self):
        return f"str:【{self.name}】"

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.name}\")"


def main():
    a = Person.createMan()
    a.a = 15
    a.B = 15

    # for item in dir(Person):
    #     print(item, "\t\t\t\t\t\t\t", getattr(a, item))

    return None


if __name__ == "__main__":
    main()
