# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年07月11日
by littlefean
"""
from typing import *


class Student:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def addScore(self, value):
        self.score += value
        self.score = min(self.score, 100)


def main():
    stuList = [
        Student("小明", 15, "男", 60),
        Student("小王", 15, "男", 60),
        Student("小兲", 15, "男", 60),
        Student("小粒", 15, "男", 60),
    ]
    for item in stuList:
        if item.name == "小兲":
            item.addScore(5)

    return None


if __name__ == "__main__":
    main()
