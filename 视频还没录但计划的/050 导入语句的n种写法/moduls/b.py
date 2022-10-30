# -*- encoding: utf-8 -*-
"""
PyCharm b
2022年10月22日
by littlefean
"""
from typing import *

import os
import sys

# 向上逐层查找 发现存在__ProjectRoot__.py  则当做项目根目录.
pathPoint = os.path.dirname(__file__)
while pathPoint != os.path.abspath(os.path.join(pathPoint, "..")):  # 判断是否到了顶级目录 /
    pathPoint = os.path.abspath(os.path.join(pathPoint, ".."))
    if os.path.exists(os.path.join(pathPoint, 'ProjectRoot.py')):
        sys.path.append(pathPoint)


def main():
    return None


if __name__ == "__main__":
    main()
