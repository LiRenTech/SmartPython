# -*- encoding: utf-8 -*-
"""
PyCharm 复数
2022年10月19日
by littlefean
"""
from typing import *
import cmath


def main():
    print(cmath.phase(-1 + 0j))  # 传入一个虚数，返回这个虚数的弧度

    print(cmath.polar(1 + 1j))  # ===> (长度 ， 角度)

    return None


if __name__ == "__main__":
    main()
