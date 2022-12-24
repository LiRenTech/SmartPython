# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年06月12日
by littlefean
"""
from typing import *
import threading


def f():
    for i in range(100000):
        print("\t", i)
    ...


def g():
    for i in range(100000):
        print(i)
    ...


def main():
    return None


if __name__ == "__main__":
    main()
