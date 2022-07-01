# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年06月21日
by littlefean
"""
from typing import *


def f(a: int, b: float, c) -> int:
    ...


def foo(arr: list):
    ...


# List的大写注解可以写中括号表示里面的元素类型是什么
def foo2(arr: List[int]):
    ...


# 列表注解可以嵌套
# 字典的注解可以 Dict[key, value]
def foo3(arr: List[List[int]], dic: Dict[str, int], s: Set[str]) -> None:
    print(arr[0])
    # dic[1] = 1  # 编辑器给出了警告
    ...


# 函数类型怎么写
# Callable[[int], str] is a function of (int) -> str.

def g(func: Callable[[int], str]):
    ...


# 注解表达式，来自《流畅的python》p131
def foo4(a: str, maxLen: "int > 0" = 41) -> int:
    ...


foo4("a", -21)  # 编辑器也丝毫没有给出提示


def foo5(a: str, maxLen: int) -> int:
    """

    :param a:
    :param maxLen: 保证 > 0
    :return:
    """
    ...


foo5("", 15)  # 这样鼠标悬停还能看到注释。


# 类类型
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(node: Node):
    if not node:
        return
    print(node)
    # 有了注解以后写下点就出来属性了，很方便，这依赖于你的编辑器是不是好。
    dfs(node.left)
    dfs(node.right)
    ...


# 注解也可以是字符串
def bfs(node: "Node"):
    ...


class A:
    def __init__(self):
        self.val = 100
        ...

    @classmethod
    def a(cls) -> Type["A"]:
        return cls


def main():
    from inspect import signature

    sig = signature(foo4)
    print(sig, type(sig))  # (a: str, maxLen: 'int > 0' = 41) -> int <class 'inspect.Signature'>

    return None


if __name__ == "__main__":
    main()
