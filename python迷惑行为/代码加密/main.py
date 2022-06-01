# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年06月01日
by littlefean
"""
from typing import *


def add(a, b):
    return a + b


def encode(string: str) -> str:
    # 加密代码
    res = ""
    for char in string:
        res += chr(ord(char) + 1)
    return res


def decode(string: str) -> str:
    # 解密代码
    res = ""
    for char in string:
        res += chr(ord(char) - 1)
    return res


def test():
    # 字符串可以加密
    string = "print(add(1, 2))"
    exec(string)


def main():
    code = decode("qsjou)bee)2-!3**")
    exec(code)
    print(code)
    print(decode(code))
    return None


if __name__ == "__main__":
    main()
