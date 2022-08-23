# -*- encoding: utf-8 -*-
"""
曼德波罗集
2022年08月21日
by littlefean
"""
import math
from PIL import Image
from time import time

from typing import Tuple


def func(x, c):
    """
    曼德波罗集 中使用到的迭代函数
    :param x: 默认从0开始迭代
    :param c: 传入一个复数
    :return:
    """
    try:
        return x ** 2 + c
    except OverflowError:
        return complex(math.nan, math.nan)


def isDivergent(x, y):
    """
    判断一个虚数点是否会发散
    :param x: 实部
    :param y: 虚部
    :return: 是否会发散，迭代到发现发散的次数
    """
    n = complex(x, y)
    num = func(0, n)
    res = False
    step = 0
    for _ in range(100):
        num = func(num, n)
        if isInfComplex(num):
            res = True
            break
        step += 1

    return res, step


def isInfComplex(n: complex):
    # 判断一个复数是否是无穷大
    return math.isnan(n.real) or math.isnan(n.imag)


def stepToColor(step: int) -> Tuple[int, int, int]:
    """将迭代步数转换为颜色，用于渲染"""
    r, g, b = 0, 0, 0
    f = lambda x: int(x ** 2 * (255 / 33))  # 将0~33映射到0~255
    if step > 66:
        r, g = 255, 255
        b = f(step - 66)
    elif step > 33:
        r = 255
        g = f(step - 33)
    else:
        r = f(step)
    return r, g, b


def arrayToImg(arr):
    arrayLen = len(arr)
    # 渲染成图
    img = Image.new("RGB", (arrayLen, arrayLen), (0, 0, 0))
    for y in range(arrayLen):
        for x in range(arrayLen):
            img.putpixel((x, y), stepToColor(arr[y][x]))
    img.show()
    img.save(f"{str(time())}.png")


def getPic1():
    arrayLen = 2048  # 图片边长
    numLen = 4  # 观察的数据范围 x和y均为 -numLen/2 ~ numLen/2 的正方形视野
    arr = [[0] * arrayLen for _ in range(arrayLen)]

    print("二维数组初始化完毕")

    _b = arrayLen / numLen
    _d = numLen / 2
    for y in range(arrayLen):
        for x in range(arrayLen):
            flag, step = isDivergent(x / _b - _d, y / _b - _d)
            arr[y][x] = step if flag else 0
    print("计算完毕")
    arrayToImg(arr)



def getPic2():
    # 以另一种方式生成图片
    arrayLen = 2048  # 图片边长
    numLen = 4  # 观察的数据范围 x和y均为 -numLen/2 ~ numLen/2 的正方形视野
    arr = [[0] * arrayLen for _ in range(arrayLen)]

    print("二维数组初始化完毕")
    _b = arrayLen / numLen
    _d = numLen / 2
    for y in range(arrayLen):
        for x in range(arrayLen):
            a = x / _b - _d
            b = y / _b - _d
            c = complex(a, b)
            num = func(0, c)
            for _ in range(100):
                num = func(num, c)
                if isInfComplex(num):
                    break
                addX, addY = round(num.real), round(num.imag)
                if 0 <= addX < arrayLen and 0 <= addY < arrayLen:
                    arr[y][x] += 1

    print("计算完毕")
    arrayToImg(arr)
    ...


def main():
    getPic2()
    return None


if __name__ == "__main__":
    main()
    # test()
