# -*- encoding: utf-8 -*-
"""
PyCharm 编码表
2022年07月10日
by littlefean
"""
from typing import *


def main():
    #  Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
    N = 0x10ffff
    print(N)  # 111_4111
    # 100 多万，这个chr是unicode编码

    # todo unicode编码和utf-8有什么区别和联系

    # todo ascii的前一部分是不是utf-8的子集

    # todo ascii和utf-8字符占用空间差异多大

    # todo utf-8 和utf-16 有什么区别

    # chr 和 ord 都是unicode的转化
    # ord("a")
    for i in range(256):
        print(i, chr(i))

    return None


if __name__ == "__main__":
    main()
