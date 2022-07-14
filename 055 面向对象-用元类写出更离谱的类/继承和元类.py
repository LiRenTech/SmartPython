# -*- encoding: utf-8 -*-
"""
PyCharm 继承和元类
2022年07月13日
by littlefean
"""
from typing import *


# 解决继承没有办法解决的问题
# 规定类里面不可以出现 某种字母开头的函数
# 更灵活的控制 创建类的过程

# 如果你连继承都还没玩转，那你就不用去想怎么去用元类来优化你的代码了


class A:
    def __init__(self):
        print("???")


class B(A):
    ...


class AA(type):
    def __new__(cls, name, bases, dic):
        print("!!!!!!!!")
        return type.__new__(cls, name, bases, dic)


# 场景1 一旦写出了一个类，就触发了一个操作，这个是继承无法实现的


# BB类一旦被定义，就触发了一个操作
class BB(metaclass=AA):
    # 这个类一旦产生，就自动触发了元类的东西

    ...


# 场景2 一旦写出了一个类，就立刻让这个类里面增加两个类属性


class C:
    value = 1
    data = 2
    info = 3


class D(C):
    ...


print(D.__dict__)
print(D.value)
print(D.data)
print(D.info)


# 可以拿到， 但是没有完全在这个子类的体内


class CC(type):
    def __new__(cls, name, bases, dic):
        return type.__new__(cls, name, bases, dic)

    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)
        self.value = 15
        self.info = 15
        self.data = 15


class DD(metaclass=CC):
    ...


print(DD.__dict__)


# 这样直接就在DD体内了，更加直接，不过可能能用继承实现还是可以用继承实现， 这个例子比较简单

def main():
    return None


if __name__ == "__main__":
    main()
