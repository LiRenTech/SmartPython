# -*- encoding: utf-8 -*-
"""
PyCharm 002 推导式效率

8分34秒 t3-t1 低级错误

2022年08月17日
by littlefean
"""
from typing import *
from time import perf_counter


def code1():
    arr = []
    for i in range(1000):
        if i % 7 == 0:
            continue
        arr.extend((i, j) for j in range(1000) if j % 55 != 0)


def code2():
    s = {i for i in range(1000000) if i % 7 != 0}


def problem(reverse=False):
    c1: float
    c2: float
    if reverse:
        t1 = perf_counter()
        code1()
        t2 = perf_counter()
        code2()
        t3 = perf_counter()
        print(t2 - t1, t3 - t2)
    else:
        t1 = perf_counter()
        code2()
        t2 = perf_counter()
        code1()
        t3 = perf_counter()
        print(t3 - t2, t2 - t1)
    ...


def main():
    # 实际上连续执行两段还可能是有问题的
    # problem(reverse=False)
    problem(reverse=True)

    # 第二种测试方法
    def func():
        ...

    from timeit import timeit
    timeit(func, number=10000)

    # 真的快慢，还是要看底层，看C源码，看逻辑，还有列表扩容机制

    return None


if __name__ == "__main__":
    main()
