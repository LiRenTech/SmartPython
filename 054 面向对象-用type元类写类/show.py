# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年07月13日
by littlefean
"""
from typing import *


class Person:
    count = 0

    def say(self):
        print(f"{self.name}")

    def __init__(self, name):
        print("new")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("new")
        print(cls, *args, **kwargs)
        return None


# def say(self):
#     print(f"{self.name}")


def main():
    # L = type("Person", (), {"__init__": __init__, "count": 0, "say": say})
    a = Person("张兲")
    # a.say()
    return None


if __name__ == "__main__":
    main()
