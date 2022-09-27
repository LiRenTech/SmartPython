# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年09月21日
by littlefean
"""
from typing import *

import sys

for item in sys.path:
    print(item)
sys.path.insert(0, "../")

import phe


def main():
    print(phe.f())
    return None


if __name__ == "__main__":
    main()
