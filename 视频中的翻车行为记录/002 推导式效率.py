# -*- encoding: utf-8 -*-
"""
PyCharm 002 推导式效率

8分34秒 t3-t1 低级错误

2022年08月17日
by littlefean
"""
from typing import *
from time import *


def myAll(arr):
    for item in arr:
        if not bool(item):
            return False
    return True


def main():
    # 实际上连续执行两段还可能是有问题的
    # arr = list(range(1_0000_0000))
    # print("start")
    # t1 = perf_counter_ns()
    #
    # myAll(arr)
    #
    # t2 = perf_counter_ns()
    #
    # all(arr)
    #
    # t3 = perf_counter_ns()
    #
    # d1 = t2 - t1
    # d2 = t3 - t2
    # print(d1, d2,  d1 / d2)

    # 第二种测试方法
    def func():
        myAll(list(range(1_0000_0000)))

    from timeit import timeit
    print(timeit(func))

    # 真的快慢，还是要看底层，看C源码，看逻辑，还有列表扩容机制

    return None


if __name__ == "__main__":
    main()
