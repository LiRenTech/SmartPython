# -*- encoding: utf-8 -*-
"""
PyCharm 重男轻女的影响模拟
重男轻女社会的现象

生孩子如果生了女孩就会继续生孩子，直到生出男孩
生出女孩就会堕胎

2022年11月09日
by littlefean
"""
from typing import *
from random import choice


class Person:
    lastName = list("赵钱孙李周吴郑王")
    firstName = "超 鹏 子航 清 梦天 嘉".split()

    def __init__(self):
        self.name = "xxx"
        self.age = 1

    @classmethod
    def getRandom(cls):
        res = cls()
        res.name = choice(cls.lastName) + choice(cls.firstName)
        return res

    def __str__(self):
        return f"({self.name})"


class Man(Person):
    def __init__(self):
        super().__init__()
        self.gender = "男"
        ...

    def natureMotive(self):
        ...


class Woman(Person):
    def __init__(self):
        super().__init__()
        self.gender = "女"

    def natureMotive(self):
        ...


class Social:
    def __init__(self):
        self.manArr = []
        self.womanArr = []
        for _ in range(100):
            self.manArr.append(Man.getRandom())
            self.womanArr.append(Woman.getRandom())

    def __str__(self):
        res = "".join(str(item) for item in self.manArr) + "".join(str(item) for item in self.womanArr)
        res += f"\n人数{len(self.manArr) + len(self.womanArr)}"
        res += f"\n男人:{len(self.manArr)}"
        res += f"\n女人:{len(self.womanArr)}"
        return res

    def printStage(self):
        # 打印年龄比例阶段图，带年龄比例的
        ...

    def tick(self):
        # 过去一年
        for man in self.manArr:
            man.age += 1
        for woman in self.womanArr:
            woman.age += 1

        ...


def main():
    s = Social()
    print(s)
    return None


if __name__ == "__main__":
    main()
