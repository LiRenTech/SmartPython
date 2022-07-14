# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月12日
by littlefean
"""
from typing import *


class A:
    def __init__(self):
        ...

    def __lshift__(self, other):
        print(other, end="")
        return self


endl = "\n"
cout = A()


def main():
    cout << "abc" << "cda" << endl
    return None


if __name__ == "__main__":
    main()
