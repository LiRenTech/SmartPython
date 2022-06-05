# -*- encoding: utf-8 -*-
"""
PyCharm new

2022年06月04日
by littlefean
"""
from typing import *
from random import randint
import os
import sys


def main():
    # 创建一个新文件，
    # 新文件py里写的内容和自己一样
    # 运行新文件
    # 最后把自己删除
    with open(__file__, encoding="utf-8") as sf:
        sfc = sf.read()
    rand = randint(1, 1000000000000000)
    with open(f"{rand}.py", "w", encoding="utf-8") as f:
        f.write(sfc)
    # 执行新文件
    # os.system(f"{rand}.py")
    eval(open(f"{rand}.py", encoding="utf-8").read())
    os.remove(__file__)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        input()
