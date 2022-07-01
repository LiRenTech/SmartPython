# -*- encoding: utf-8 -*-
"""
PyCharm 合并字典
2022年06月29日
by littlefean
"""
from typing import *

d = {'spam': 1, 'eggs': 2, 'cheese': 3}
e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}

# 方法1
print({**d, **e})
# 方法2
from collections import ChainMap

print(dict(ChainMap(e, d)))
# 方法3
print(dict(d, **e))
# 方法4
d.update(e)
print(d)

# 方法5
print(e | d)
print(e & d)
print(e ^ d)

def main():
    a = 141534

    return None


if __name__ == "__main__":
    main()
