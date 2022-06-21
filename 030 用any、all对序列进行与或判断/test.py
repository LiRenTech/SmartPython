# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年06月20日
by littlefean
"""
from typing import *


def main():
    res = any(item % 5 == 0 for item in range(1, 100))

    print(res)

    return None


if __name__ == "__main__":
    main()
