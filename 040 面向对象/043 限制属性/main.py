# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年07月11日
by littlefean
"""
from typing import *


class Position:
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    p = Position(1, 3)
    p.__class__.__slots__.append("z")
    p.__slots__.append("z")
    p.z = 15
    return None


if __name__ == "__main__":
    main()
