# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年08月19日
by littlefean
"""
from typing import *
from api import *


def main():
    run()
    """
    为什么是pyi呢？因为i是interface的意思
    有接口的意思，但是python没有接口，
    只是提供一个特殊的扩展
    存根文件仅包含模块公共接口的描述，没有任何实现。
    
    鼠标中键点击函数，会跳转到pyi那里
    
    鼠标悬停函数上方，显示的是pyi那里函数的的文档注释
    如果pyi和py里都写了函数注释，则会显示pyi里的注释
    如果pyi里的没写注释，py里的写了注释，则显示不到注释了
    
    如果两个地方都写了实现，则以py里的实现为主
    不管pyi里有没有实现，总是按py里的实现走
    
    """

    swim()
    # jump()  # 出现警告了，说明如果两个都有文件的时候，有没有这个方法，pyi说了算

    return None


def xxx():
    ...


if __name__ == "__main__":
    main()
