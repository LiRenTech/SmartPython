# -*- encoding: utf-8 -*-
"""
PyCharm test2
2022年07月12日
by littlefean
"""
from typing import *


class Deco:
    def __init__(self, f):
        self.f = f
        ...

    def __call__(self, *args, **kwargs):
        print("======")
        self.f()
        print("======")

    def __str__(self):
        return "decoType"


@Deco
def func():
    print("helloWord")


def main():
    # func()
    res = Deco(func)
    print(res, type(res))
    return None


if __name__ == "__main__":
    main()
