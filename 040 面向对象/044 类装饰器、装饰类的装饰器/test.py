# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月12日
by littlefean
"""
from typing import *


class Deco:
    def __init__(self, char):
        self.char = char
        ...

    def __call__(self, f):
        def newFunc():
            print(self.char * 10)
            res = f()
            print(self.char * 10)
            return res

        return newFunc


@Deco("=")
@Deco("*")
def func():
    print("helloWord")


def main():
    func()
    return None


if __name__ == "__main__":
    main()
