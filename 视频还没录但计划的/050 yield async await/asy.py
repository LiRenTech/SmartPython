# -*- encoding: utf-8 -*-
"""
PyCharm asy
2022年11月13日
by littlefean
"""
from typing import *


def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value


async def async_function():
    return 1


async def await_coroutine():
    # await语法只能出现在通过async修饰的函数中，否则会报SyntaxError错误。
    result = await async_function()
    print(result)


run(await_coroutine())


def main():
    return None


if __name__ == "__main__":
    main()
