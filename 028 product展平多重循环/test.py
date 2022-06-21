# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年06月10日
by littlefean
"""

import itertools


def main():
    for x, y, z, i in itertools.product(range(10), range(10), range(10), range(3)):
        if x == y == 50:
            break
        print(x, y, z)

    return None


if __name__ == "__main__":
    main()
