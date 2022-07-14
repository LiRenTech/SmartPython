# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年07月12日
by littlefean
"""
from typing import *
from enum import Enum, unique


@unique
class Block(Enum):
    AIR = 0
    STONE = 1
    GRASS = 2
    DIRT = 3


def main():
    print(Block.AIR.value)
    print(Block(1))
    print()
    for k, v in Block.__members__.items():
        print(k, v)
    return None


if __name__ == "__main__":
    main()
