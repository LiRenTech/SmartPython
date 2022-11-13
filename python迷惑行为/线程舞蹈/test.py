# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年11月13日
by littlefean
"""
from typing import *
from threading import Thread


def t(n):
    if n < 0:
        return
    print(n)
    Thread(target=t, args=(n - 1,)).start()

# 不能有返回值?
# def fab(x):
#     if x < 0:
#         return 0
#     if x == 1:
#         return 1
#     return Thread(target=fab, args=(x - 1,)).start() + Thread(target=fab, args=(x - 2,)).start()


def main():
    t(15)
    return None


if __name__ == "__main__":
    main()
