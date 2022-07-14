# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年06月22日
by littlefean
"""
from typing import *


class Solution1:
    def strongPasswordCheckerII(self, password: str) -> bool:
        res = False
        if len(password) < 8:
            return False
        f1 = any(char in password for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        f2 = any(char in password for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
        f3 = any(char.isdigit() for char in password)
        f4 = any(char in password for char in "!@#$%^&*()-+")
        for i in range(1, len(password)):
            if password[i - 1] == password[i]:
                return False

        return f1 and f2 and f3 and f4


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        f1 = any(char in password for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        f2 = any(char in password for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
        f3 = any(char.isdigit() for char in password)
        f4 = any(char in password for char in "!@#$%^&*()-+")
        return next(
            (
                False for i in range(1, len(password)) if password[i - 1] == password[i]
            ),
            f1 and f2 and f3 and f4
        )


def val(char: str) -> int:
    return {}[char]


class Solution2:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        num = sum(val(s[i]) * power ** i for i in range(k))
        kArr = [num]
        for i in range(1, len(s) - k + 1):
            newNum = kArr[-1]
            newNum -= val(s[i - 1])
            newNum //= power
            newNum += val(s[i + k - 1]) * power ** (k - 1)
            kArr.append(newNum)
        index = -1
        for i, v in enumerate(kArr):
            if v % modulo == hashValue:
                index = i
                break
        return s[index:index + k]


def x(s: str) -> str:
    res = s[:]
    left = -1
    for i in range(1, len(res)):
        if res[i] == "(" and res[i - 1].isdigit():
            left = i
            break
    if left != -1:
        res = (res, "*", left)
    right = -1
    for i in range(0, len(res) - 1):
        if res[i] == ")" and res[i + 1].isdigit():
            right = i
            break
    if right != -1:
        res = (res, "*", right)
    return res


def x_(s: str) -> str:
    res = s[:]
    left = next(
        (i for i in range(1, len(res)) if res[i] == "(" and res[i - 1].isdigit()),
        -1
    )

    if left != -1:
        res = (res, "*", left)
    right = next((i for i in range(len(res) - 1) if res[i] == ")" and res[i + 1].isdigit()), -1)

    if right != -1:
        res = (res, "*", right)
    return res


def judge(n):
    res = True
    for i, v in enumerate([13, 3, 4, 5]):
        if n % (i + 2) != v:
            return False
    return res


def judge_(n):
    res = True
    return next(
        (False for i, v in enumerate([13, 3, 4, 5]) if n % (i + 2) != v),
        res
    )


def main():
    return None


if __name__ == "__main__":
    main()
