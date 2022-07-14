# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年07月12日
by littlefean
"""
from typing import *
from enum import Enum, unique

Fruit = {
    'APPLE': 1,
    'BANANA': 2,
    'ORANGE': 3,
}


class F:
    APPLE = 1
    BANANA = 2
    ORANGE = 3


class A:
    a = 1
    a = 15  # 传统写法不会报错


@unique  # 不存在表示值相同的方块，设置了相同的值会报错
class Block(Enum):
    AIR = 0
    STONE = 1
    GRASS = 2
    DIRT = 3
    # AIR = 1


def main():
    print(Block.STONE)
    print(Block(3))  # 双向访问
    dic = Block.__members__
    print(dic)
    return None


if __name__ == "__main__":
    main()
