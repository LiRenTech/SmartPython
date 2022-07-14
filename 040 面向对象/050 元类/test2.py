# -*- encoding: utf-8 -*-
"""
PyCharm test2
2022年07月13日
by littlefean
"""
from typing import *
from random import *


class MyMeta(type):

    def __add__(self, other: "MyMeta"):
        dic = {}
        for k, v in self.__dict__.items():
            dic[k] = v
        for k, v in other.__dict__.items():
            dic[k] = v

        return MyMeta(
            self.__name__ + other.__name__,
            self.__bases__ + other.__bases__,
            dic
        )

    ...


class Human(metaclass=MyMeta):
    LastName = list("赵钱孙李周吴郑王")
    FirstName = ["建国", "鹏"]

    @classmethod
    def create(cls):
        return cls(
            choice(cls.LastName) + choice(cls.FirstName),
            "男" if random() < 0.5 else "女"
        )

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Wolf(metaclass=MyMeta):
    Kinds = ["灰色", "白色", "灰黑色"]

    @classmethod
    def create(cls):
        return cls(choice(cls.Kinds))

    def __init__(self, kind):
        self.kind = kind


def main():
    Werewolf = Wolf + Human

    return None


if __name__ == "__main__":
    main()
