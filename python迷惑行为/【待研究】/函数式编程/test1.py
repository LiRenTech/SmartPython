# -*- encoding: utf-8 -*-
"""
PyCharm test1
2022年08月27日
by littlefean
"""
from typing import *

b = 10


def f(a=b + 1):
    return a


print(f())  # 11
print(f())  # 11
b = 100
print(f())  # 11  没变

# if __name__ == "__main__":
#     main()
