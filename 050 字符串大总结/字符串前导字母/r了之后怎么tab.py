# -*- encoding: utf-8 -*-
"""
PyCharm r了之后怎么tab
2022年07月03日
by littlefean
"""
from typing import *


def main():
    a = r"\\\\\\\123123"
    b = r"aaab\tsss"
    b = r"aaab\\tsss"
    b = "aaab\tsss"
    c = r"D:\WpSy	stem"
    # pycharm 里面加tab 不能按
    for char in c:
        if char == "\t":
            print("是tab")
    print(c)
    print(b)
    return None


if __name__ == "__main__":
    main()
