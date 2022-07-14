# -*- encoding: utf-8 -*-
"""
PyCharm test3
2022年07月13日
by littlefean
"""
from typing import *

from random import choice


def mergeFunc(f1, f2):
    def newFunc():
        print("~~~~~~")
        f1()
        f2()
        print("~~~~~~")

    return newFunc


class MyMeta(type):

    def __add__(self, other: "MyMeta"):
        mergeName = self.__name__ + other.__name__
        mergeDic = self.__dict__ | other.__dict__
        for k, v in self.__dict__.items():
            for ko, vo in other.__dict__.items():

                if type(v) == type(vo) == staticmethod:
                    # print("检测到了方法合并")
                    mergeDic[k + ko] = mergeFunc(v, vo)
                else:
                    # print("普通合并")
                    mergeDic[k + ko] = choice([v, vo])
        return type(mergeName, (), mergeDic)


class A(metaclass=MyMeta):
    a = 12

    @staticmethod
    def jump():
        print("jump")

    @staticmethod
    def swim():
        print("swim")


class B(metaclass=MyMeta):
    b = 22

    @staticmethod
    def run():
        print("run")

    @staticmethod
    def laugh():
        print("laugh")


def main():
    C = A + B
    C.run()
    C.jump()
    print(C.ab)
    for k, v in C.__dict__.items():
        print(k, "\t\t\t\t\t", v)
    C.jumplaugh()
    return None


if __name__ == "__main__":
    main()
