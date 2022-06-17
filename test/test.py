from array import array
from time import perf_counter
from random import randint

# print(lst)
# print(arr)

# 测试随机修改
N = 1000000


def test1():
    lst = list(range(100))
    arr = array("i", lst)
    t1 = perf_counter()

    for _ in range(N):
        lst[randint(0, len(lst) - 1)] = 666

    t2 = perf_counter()

    for _ in range(N):
        arr[randint(0, len(arr) - 1)] = 666

    t3 = perf_counter()
    print(t2 - t1, t3 - t2)


def test2():
    """
    append
    """
    arr1 = array("i")

    t1 = perf_counter()
    lst1 = [1 for _ in range(N)]
    t2 = perf_counter()
    for _ in range(N):
        arr1.append(1)
    t3 = perf_counter()
    print(lst1.__sizeof__())
    print(arr1.__sizeof__())
    print(t2 - t1, t3 - t2)


def test3():
    t1 = perf_counter()
    arr = array("i", range(N))
    t2 = perf_counter()
    lst = list(range(N))
    t3 = perf_counter()
    print(t2 - t1, t3 - t2)


test3()
