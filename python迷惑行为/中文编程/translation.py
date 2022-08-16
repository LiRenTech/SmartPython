# -*- encoding: utf-8 -*-
"""
PyCharm translation
此文件对中文编程的代码字符串进行关键字和一些中文符号的替换
2022年08月14日
by littlefean
"""
from typing import *

signDic = {
    "：": ":",
    "，": ",",
    "（": "(",
    "）": ")",
    "【": "[",
    "】": "]",
    "“": "\"",
    "”": "\"",
    "‘": "'",
    "’": "'",
    "；": ";",
    "？": "?",
    "、": "\\",
    "！": "!",
    "￥": "$",
    "《": "<",
    "》": ">",
    "的": ".",
}
kwDic = {
    "迭代": "for",
    "返回": "return",
    "在": "in",
    "类": "class",
    "如果": "if",
    "是": "is",
    "导入": "import",
    "定义": "def",
}


def trans(string: str) -> str:
    for k, v in (signDic | kwDic).items():
        string = string.replace(k, v)
    return string


def main():
    return None


if __name__ == "__main__":
    main()
