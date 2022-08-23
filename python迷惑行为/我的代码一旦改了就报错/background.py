# -*- encoding: utf-8 -*-
"""
PyCharm background
2022年08月23日
by littlefean
"""
from typing import *
import inspect


def test():
    """sss"""
    print("sss")


def main():
    print(inspect.getsource(test))
    return None


if __name__ == "__main__":
    main()
