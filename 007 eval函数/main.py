# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年06月21日
by littlefean
"""
from typing import *


def main():
    # 自动解析数字
    # n = eval(input())

    # 解析字典、元组、列表、集合等数据结构嵌套的字符串表示
    dic = eval("{1: [1, 2, 3]}")

    # 坑队友
    # eval("__import__('os').remove('...')")  # ... 里面写一些删除的东西

    # 一行代码低效率实现阶乘
    def jie(num):
        return eval("*".join(str(i) for i in range(1, num + 1)))

    print("------------")
    print(jie(1))
    print(jie(2))
    print(jie(3))
    return None


if __name__ == "__main__":
    main()
