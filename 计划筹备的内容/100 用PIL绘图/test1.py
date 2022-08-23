# -*- encoding: utf-8 -*-
"""
PyCharm test1
火灾图
2022年08月21日
by littlefean
"""
from typing import *
from random import random


def main():
    arr = [[0] * 100 for _ in range(100)]
    for line in arr:
        for i in range(len(line)):
            line[i] = 1 if random() < 0.4 else 0
    # 感染
    for y in range(len(arr)):
        if arr[y][0] == 0:
            continue
        q = [(0, y)]
        while q:

            position = q.pop()

    return None


if __name__ == "__main__":
    main()
