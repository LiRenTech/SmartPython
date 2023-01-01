# -*- encoding: utf-8 -*-
"""
PyCharm 输入技巧
2022年08月10日
by littlefean
"""
from typing import *

def list_input():
    # 使用列表接收单行输入的数据
    nums1 = list(map(int, input().split()))  # 接收数字
    nums2 = [_ for _ in input().split()]  # 同上
    nums3 = list(input().split())  # 接收字符串
    print(f"{nums1=!r} {nums2=!r} {nums3=!r}")  # !r 表示输出前调用 repr()

    # 先输入数字n,再输入n行列表(每行一个列表, 用空格分隔)
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]  # 可读性较低, 不太优雅
    print(f"{nums=}")

    # 先输入数字n,再输入n行数字(每行一个数)
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    print(f"{nums=}")


def input_many():
    """多组输入"""
    # 次数未知的多组输入
    while True:
        try:
            a, b, c = map(int, input().split())
            print(a + b + c)
            ...
        except ValueError:  # 实际使用过程中若有问题可将异常类型改为空或Exception
            break

    # 有次数的多组输入(给定数据输入次数, 对每次输入的数据进行处理)
    n = int(input())
    while n:
        num = int(input())
        print(num)
        ...
        n -= 1


def main():
    # 一行输入两个变量
    a, b = map(int, input().split())
    # 一行输入n个变量用一个元组接收
    *c, = map(int, input().split())

    print(a, b, c)

    return None


if __name__ == "__main__":
    main()
