# -*- encoding: utf-8 -*-
"""
PyCharm 元类和obj的关系
2022年07月13日
by littlefean
"""
from typing import *


def main():
    print(object)
    print(type(object))
    print(object.__class__)  # type
    print(object.__bases__)  # ()

    return None


if __name__ == "__main__":
    main()
