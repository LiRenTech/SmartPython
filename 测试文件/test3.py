# -*- encoding: utf-8 -*-
"""
PyCharm test3
2022年08月15日
by littlefean
"""
from typing import *


def findTargetSumWays(nums: List[int], target: int) -> int:
    length = len(nums)
    maxNum = 2 ** length
    res = 0
    for i in range(maxNum):
        sumNum = 0
        for x in range(length):
            if i >> x & 1 == 1:
                sumNum += nums[x]
            else:
                sumNum -= nums[x]
        if target == sumNum:
            res += 1
    return res


def main():
    return None


if __name__ == "__main__":
    main()
