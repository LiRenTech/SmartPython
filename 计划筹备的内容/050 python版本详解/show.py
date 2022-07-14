# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年06月29日
by littlefean
"""
import asyncio
from typing import *

"""
3.1

3.2
3.3
3.4
3.5



3.6



3.7
3.8
3.9
3.10
3.11

"""

# 3.5

"""
async 和 await 
*[]  **{}
新的矩阵乘法运算符: a @ b.
typing库
改进了zip支持
"""
a = (15,)
b = (155,)
print(a @ b)

# 3.6
"""
f"{}"
100_000
"""


# 允许在异步函数内同时出现yield和await，也就是可以实现异步生成器
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


# 异步推导式

# result = [i async for i in aiter() if i % 2]
# result = [await fun() for fun in funcs if await condition()]

# https://blog.csdn.net/Qwertyuiop2016/article/details/123556754


# 3.7

import importlib.resources as res


# https://blog.csdn.net/be5yond/article/details/120062721

# 3.9

# 3.10
# https://blog.csdn.net/qq_56630261/article/details/123996258

# 3.11
# https://xw.qq.com/cmsid/20220605A014JA00

def main():
    """

    :return:
    """

    return None


if __name__ == "__main__":
    main()
