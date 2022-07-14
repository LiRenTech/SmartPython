# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月12日
by littlefean
"""
from typing import *


class Student:
    def __init__(self, name, score, ):
        self.name = name
        self._score = score

    def __str__(self):
        return f"({self.name}, {self._score})"

    @property
    def score(self):
        print("get")
        return self._score

    @score.setter
    def score(self, value):
        print("检测方法运行了啦")
        if type(value) not in (int, float):
            ...
        elif 0 <= value <= 100:
            self._score = value

    @score.deleter
    def score(self):
        print("删除了啦")

    def changeScore(self, n):
        self._score += n
        self._score = min(self._score, 100)
        self._score = max(self._score, 0)


def main():
    s1 = Student("张兲", 60)
    for _ in range(365):
        s1.changeScore(1)

    s1.score = 60
    print(s1.score)
    del s1.score

    return None


if __name__ == "__main__":
    main()
