# -*- encoding: utf-8 -*-
"""
PyCharm show2
2022年07月11日
by littlefean
"""
from typing import *
from dataclasses import dataclass
from collections import namedtuple


@dataclass()
class Vec:
    x: int
    y: int


Loc = namedtuple("Loc", ["x", "y"])


def main():
    v1 = Vec(2, 2)
    print(v1)
    l1 = Loc(58, 10)
    print(l1)
    return None


if __name__ == "__main__":
    main()
