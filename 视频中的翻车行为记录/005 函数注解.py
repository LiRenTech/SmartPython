# -*- encoding: utf-8 -*-
"""
PyCharm 005 函数注解
0分22秒 函数注释，是三引号的东西
9分27秒 a:int 不是空值
2022年08月17日
by littlefean
"""
from typing import *


def main():
    a: int
    print(type(a))
    # 一个变量名，指向一个内存地址
    # 这个变量名还没有指向一块内存地址

    return None


if __name__ == "__main__":
    main()
