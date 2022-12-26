from __future__ import annotations  # 允许竖线语法
from typing import overload


# 其实overload并非真正的函数重载，带有@overload的函数会被ide识别为用法
# 最终这个函数指向最后定义的函数
# 并且一个函数内带有overload装饰器的都是一个函数


@overload
def func(a: str, b: int) -> str:
    """
    a[b]
    """


print(id(func))


@overload
def func(a: int, b: str) -> int:
    """
    a + len(b)
    """


print(id(func))


@overload
def func(a: int, b: list, c: tuple) -> int:
    """
    a - len(b) + len(c)
    """


print(id(func))


def func(a: str | int, b: str | int, c: tuple = None):
    print("===")
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    if isinstance(a, str) and isinstance(b, int) and not c:
        # 第一个overload
        return a[b]
    elif isinstance(a, int) and isinstance(b, str) and not c:
        # 第二个overload
        return a + len(b)
    elif isinstance(a, int) and isinstance(b, list) and isinstance(c, tuple):
        # 第三个overload
        a - len(b) + len(c)
    print("===")


print(id(func))


# 1.png
# 图片里的 -> None 是因为截屏的时候没写返回值

print(func("abc", 1))
print(func(5, "abcde"))
print(func(3, [1, 2, 3], ()))
