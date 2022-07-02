# -*- encoding: utf-8 -*-
"""
PyCharm 字符串是否有两个相邻一样字符
2022年07月02日
by littlefean
"""
from typing import *


def validate(string: str) -> bool:
    return all(string[i] != string[i - 1] for i in range(1, len(string)))


def main():
    return None


if __name__ == "__main__":
    main()
