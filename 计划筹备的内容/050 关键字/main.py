# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年06月01日
by littlefean
"""
from typing import *
import keyword


def main():
    # print(keyword.kwlist)
    lst = [
        # 等待理解的关键字
        'assert',
        'async',
        'await',
        'yield',
    ]

    # help("assert")
    async def f():
        await f()
        ...

    return None


if __name__ == "__main__":
    main()
