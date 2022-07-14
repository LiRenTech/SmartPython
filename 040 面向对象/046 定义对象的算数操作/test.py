# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月12日
by littlefean
"""
from typing import *


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if type(other) == self.__class__:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f"{self.__dict__}"

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    __repr__ = __str__


def main():
    a = Vector(1, 1, 1)
    print(abs(a))

    return None


if __name__ == "__main__":
    main()
