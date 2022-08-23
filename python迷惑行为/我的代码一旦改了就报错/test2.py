# -*- encoding: utf-8 -*-
"""

https://hpyculator.readthedocs.io/zh_CN/latest/utils_api/hpyfunc.html#hpyfunc-dont-change-my-code
来自 Howie皓子 的优化
"""
from typing import *
import inspect


def dont_change_my_code(fun: Callable, sign: str) -> None:
    """沙雕系列：别修改我的代码！
    直接使用print输出hash值，未计算出结果则输出-1

    :param fun: 不要修改这个函数！
    :param sign: 标识符
    :return: None"""
    two_part_text = inspect.getsource(fun).split(sign)
    if len(two_part_text) > 2:
        raise Exception("标识符只能出现一次")
    if len(two_part_text) == 1:
        return
    for num in range(1_0000):
        if easy_text_hash(two_part_text[0] + str(num) + two_part_text[1]) == num:
            print(num)
    print("完毕")
    return None


def easy_text_hash(string: str) -> int:
    res = 153434884
    for i, char in enumerate(string):
        res += ord(char) ** (i + 1)
        res %= 10000
    return res


def fun_name_aaa():
    """给组员：你要是改了，，有你好果子吃,,,"""
    if easy_text_hash(inspect.getsource(fun_name_aaa)) != '!!!':  # ""里面的是标识符
        print("改了是吧，有你好果子吃")


def main():
    dont_change_my_code(fun=fun_name_aaa, sign="'!!!'")
    return None


if __name__ == "__main__":
    main()
