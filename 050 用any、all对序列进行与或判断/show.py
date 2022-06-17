# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年06月17日
by littlefean
"""
from typing import *
from time import perf_counter


def main():
    # any(一个序列):  bool(每一个元素)，但凡有一个是True，就返回True了
    print(any([1, 1, 1, 1]))  # True

    # print(any(1, 1, 1, 1))  # 不能拆开写，只能传一个参数

    print(any((0, 0, 0, 1, 0)))  # True

    print(any([0, 0, 0, 0, 0]))  # False

    print(any([" ", "#", "$", ":", ""]))  # True
    print(any("123456"))
    print(any(""))  # False
    print(any([]))  # False
    print(any(["", "", "", ""]))  # False
    print(any(["", False, 0, 0.0, (), {}, []]))  # False

    print(all([1, 13, 13, 13, 123]))  # True 所有的都是True
    print(all([0, 1, 1, 1, 1]))  # False

    # speedTest()
    speedTestSignal()
    return None


def myAny(series):
    for item in series:
        if item:  # 不要写成 if bool(item)  会慢六倍速度左右！！
            return True
    return False


def myAll(series):
    for item in series:
        if not item:
            return False
    return True


def speedTest():
    # 速度测试

    N = 10000_0000
    arr = list(range(1, N))
    t1 = perf_counter()

    print(all(arr))
    t2 = perf_counter()

    print(myAll(arr))

    t3 = perf_counter()
    print(t2 - t1, t3 - t1)
    """
    6.785137 7.364915300000001
    6.5468219 7.122900499999999
    0.6386403 0.6973506
    0.6420742 0.7011412
    0.6599428 0.7179033
    0.7496174 0.8072769
    
    可以发现，还是自己写的快一点点
    是不是因为先执行了自己的，后执行了all，和顺序有影响呢？
    交换了顺序之后发现
    
    0.057376099999999985 0.7144853
    0.059252200000000005 0.7843093
    0.05834890000000001 0.8313154
    
    N = 10000_0000
    0.5795687999999999 7.158511399999999
    0.5736235000000001 7.0475506999999995
    
    所以这个实验，不准确，和谁先谁后有很大关系
    应该单独测试，不要一起测试，可能是和垃圾回收机制有关系
    """

    ...


def speedTestSignal():
    # 更加标准的速度测试
    N = 10000_0000
    arr = list(range(1, N))
    t1 = perf_counter()
    print(myAll(arr))
    # print(all(arr))
    t2 = perf_counter()

    print(t2 - t1)
    """ N = 10000_0000
    
    all()
    0.5967585999999998
    0.5775873000000002
    0.5761730999999999
    0.5800913000000001
    
    myAll()
    1.2924113000000002
    1.2927265999999997
    1.2714261
    1.3011073
    """
    ...


if __name__ == "__main__":
    main()
