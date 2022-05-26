# -*- encoding: utf-8 -*-
"""
PyCharm videoComment
2022年05月23日
by littlefean
"""
from typing import *
from htmlGetter import HtmlGetter


def main():
    w = HtmlGetter("https://www.bilibili.com/video/BV1yT4y1B7zq").dynamicGet()
    print(w)
    return None


if __name__ == "__main__":
    main()
