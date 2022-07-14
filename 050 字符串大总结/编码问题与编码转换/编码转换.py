# -*- encoding: utf-8 -*-
"""
PyCharm 字符转化
2022年07月01日
by littlefean
"""
from typing import *


def main():
    """..."""

    a = "这里是中文"
    # 如何区分encode和decode？
    print(a.encode())  # 一个字符串encode就是变成编码形势了
    # b'\xe5\x88\xab\xe7\x9c\x8b\xe6\x88\x91\xe5\x8f\xaa\xe6\x98\xaf\xe4\xb8\x80\xe5\x8f\xaa\xe7\xbe\x8a'
    # en- 表示让它能够，使之成为，enlarge 使之扩大，enable 使他扩大
    # encode 就是 使它成为密码 code翻译里有“代码，密码” 的意思
    # 就是让字符串 使之成为我们看不懂的密码形式 code形式
    print("this is english".encode("ascii"))
    print("this is english".encode("utf-8"))
    # print("这里是中文".encode("ascii"))  # 这个不能转化，因为ascii的范围比较小
    print("这里是中文".encode("utf-8"))
    print("这里是jabc".encode("utf-8"))
    print("这里是中文".encode("gbk"))

    return None


if __name__ == "__main__":
    main()
