# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年07月05日
by littlefean
"""
from typing import *


class A:
    def __init__(self, n=1):
        self.n = n

    def __str__(self):
        return f"<{self.n}>"

    @classmethod
    def default(cls):
        return cls(1000)

    @staticmethod
    def default2():
        return A(1000)


def main():
    a = A(15)
    print(a)  # 自动调用str方法
    print(a.__str__())  # 相当于这样

    print(A.__str__(a))
    # 魔术方法用str方法，第一个self参数的作用就出来了
    # 也就是说self参数表示的是一个实例

    print(a.__str__())
    # 再来回顾这个，a没有 __str__ 方法，他就会向上找它的类有没有这个方法
    # 如果有，就调用它的类的方法，然后第一个参数就自动传进来了

    # 疑点
    b = A()
    # 这个过程应该相当于
    # b = A.__init__(?,?)
    # 这个没法解释了

    return None


if __name__ == "__main__":
    main()
