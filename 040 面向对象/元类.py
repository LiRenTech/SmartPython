# -*- encoding: utf-8 -*-
"""
PyCharm 元类
2022年07月02日
by littlefean
"""
from typing import *


def say(self):
    print(self, "eat")


# type(类名，继承关系，属性)
Person = type("Person", (), {"count": 0, "say": say})

p = Person()
p.say()


def main():
    return None


if __name__ == "__main__":
    main()
