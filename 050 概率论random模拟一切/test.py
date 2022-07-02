# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月02日
by littlefean
"""
from typing import *
from random import *


def main():
    # random 可以干什么

    randrange(1, 10, 3)
    random()
    randint(-5, 10)
    uniform(1, 20)

    # 抽奖，抽签
    # 在一坨东西里随机选一个
    print(choice([1, 2, 3, 4, 5, 6]))
    print(choice(range(10)))
    # 随机抽多个
    print(sample(list(range(100)), 10))

    # 洗牌序列
    print(shuffle(list(range(100))))


    return None


if __name__ == "__main__":
    main()
