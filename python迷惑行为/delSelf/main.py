# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年06月04日
by littlefean
"""
from typing import *


def main():
    # # 1
    # import os
    # os.remove(__file__)
    # # 2
    # eval("__import__('os').remove(__file__)")  # 隐藏式传入os库并把自己删除

    # 3 加密一层
    # newString = ""
    # for char in "__import__('os').remove(__file__)":
    #     newString += chr(ord(char) + 1)
    # print(newString)
    # newString = "``jnqpsu``)(pt(*/sfnpwf)``gjmf``*"
    # originString = ""
    # for char in newString:
    #     originString += chr(ord(char) - 1)
    # print(originString)

    # 简化代码
    # eval("".join([chr(ord(char) - 1) for char in "``jnqpsu``)(pt(*/sfnpwf)``gjmf``*"]))

    return None


if __name__ == "__main__":
    main()
