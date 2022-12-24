# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年11月13日
by littlefean
"""
from typing import *


def f():
    # 普通函数
    return 1


def g():
    # 生成器函数
    # 把yield想象成print，产出的东西会缓存到一个队列里
    # 外层用for接受这个 for item in gen()
    # 就可以从这个里面取出东西来了
    for i in range(100):
        yield i ** 2


async def af():
    # 异步函数
    return 1


async def ag():
    # 异步生成器函数
    for i in range(100):
        yield i ** 2


def main():
    print(type(f))
    print(type(af))
    print(type(g))
    print(type(ag))
    # 上面全都是 func
    return None


if __name__ == "__main__":
    main()
