# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年06月11日
by littlefean
"""
from typing import *
import heapq


class Person:
    def __init__(self, name, n):
        self.name = name
        self.n = n

    def __repr__(self):
        return f"<{self.name}>"


def main():
    arr = [Person("a", 5), Person("b", 10), Person("c", 4), Person("d", 3), Person("e", 1)]
    newList = [(-item.n, item) for item in arr]
    heapq.heapify(newList)
    print(newList)
    print(newList[0])

    # print(heapq.heappop(newList))
    number, p = heapq.heappop(newList)
    number *= -1
    print(number, p)
    return None


if __name__ == "__main__":
    main()
