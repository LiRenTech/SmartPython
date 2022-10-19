# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年10月19日
by littlefean
"""
from typing import *
# 蓝桥杯 3.8.6 用不了这个模块

import graphlib
from graphlib import TopologicalSorter


def main():
    # 拓扑排序
    # graph = {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
    # print(tuple(ts.static_order()))

    # 检测有向图是否有环
    graph = {1: {2}, 2: {1}}
    ts = TopologicalSorter(graph)
    try:
        print(ts.prepare())
    except graphlib.CycleError:
        print("有环")
        ...
    return None


if __name__ == "__main__":
    main()
