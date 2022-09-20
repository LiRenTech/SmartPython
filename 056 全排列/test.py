# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年09月19日
by littlefean
"""
from typing import *

"""
[0, 1, 2]
[0, 2, 1]
[1, 0, 2]
[1, 2, 0]
[2, 0, 1]
[2, 1, 0]
"""


def main():
    N = 3
    path = []
    s = set()
    res = []

    def dfs():
        if len(path) == N:
            print(path)
            res.append(path[:])
            return
        for i in range(N):
            if i in s:
                continue
            s.add(i)
            path.append(i)
            dfs()
            s.remove(path.pop())
        ...

    dfs()
    print(res)
    from itertools import permutations
    for item in permutations(range(4)):
        print(item)
    return None


if __name__ == "__main__":
    main()
