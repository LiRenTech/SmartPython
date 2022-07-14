# -*- encoding: utf-8 -*-
"""
PyCharm 033 字符串转义字符总结
2022年07月01日
by littlefean
"""
from typing import *

r = r"\t\\  "  # 一旦写了r，后面就不能写东西了

# \r 是回车，return
# \n 是换行，newline


a = """
 \000
 \0
 
 \0000
 
 \\
 \a 响铃
 \b 退格符
 \c
 \d
 \e
 \f 换页
 \g
 \h
 \i
 \j
 \k
 \l
 \m
 \n  换行的意思
 \o
 \p 
 \q
 \r 重新显示当前行
 \s 
 \t 制表符
 \ u 单独写不行
 \u0000
 \u331222
 \u1447
 \u9999
 
 \v  vertical 的缩写，垂直制表符 几乎没用，pycharm和黑框都看不到效果
 \w 
 \ x 不能
 \x5555
 \x23  
 \xab
 \xff
 
 \"
 \' 为什么要设计两种引号都表示字符串？因为这样就可以嵌套了
 a = "ab'c"b"'c"
 \y
 \z
 
 \A
 \B
 \C
 \D
 \E
 \F
 \G
 \H
 \I
 \J
 \K
 \L
 \M
 \\N 
 \O
 \P
 \Q
 \R
 \S
 \T
 \\U
 \V
 \W
 \X
 \Y
 \Z
"""


def v():
    print("没有什么东西是对的\v我们是一个正常的人")


def warp():
    string = "____'----"  "-----'______"  # 不是这种平白无故嵌套的
    string2 = "abc" + "bcd" + "cbd"
    string2 = "abc" "bcd" "cbd"
    print(string)
    print(string2)


def tab():
    arr1 = ["周星仔", "simi", "skrskr", "一头猪"]
    arr2 = [1234, 213, 12, 1]
    for i in range(4):
        print(f"{arr1[i]}\t{arr2[i]}")
    # 起到了自动对齐的效果，打印一大堆数据的时候有用
    # 有时候差的太多了就对不齐了。
    ...


def testA():
    # \a 的作用
    print('\a')
    input(">>>")
    print('\a')  # 电脑出现一声噔~
    # 如果想让给自己做一个定时提醒程序，可以用这个简单的print杠a实现
    input(">>>")


def animation():
    # \r 的作用
    # 一个围绕中心旋转的小加载动画
    from time import sleep
    s = r"-\|/"
    i = 0
    while True:
        sleep(0.1)
        i += 1
        print(f"{s[i % 4]}\r", end="")


def main():
    print("\xaa")
    print("\x11")
    print("\x61")
    print("\x62")
    print("\x63")
    print(b'\xe4\xb8\xad\xe6\x96\x87')
    print('\xe4\xb8\xad\xe6\x96\x87')
    print('\u4e2d\u6587')  # 中文 unicode
    # 为什么一个中文是两个字节
    # 字节是bytes
    # 1bytes = 8bit 我们经常说巴比特巴比特。。。
    # 两个字节就是16比特
    # 一个比特就是一个0或者1
    # 一个汉字要用16比特
    # 1111000011110000 => \u4e2d  => 一个汉字
    # \u4e2d 表示四个十六进制数字拼在一起
    # 一个十六进制数字需要用四位二进制数拼在一起，所以就对应过来了。

    print("我是一个\b正常人")  # 相当于按了一下删除键把前面那个字给删了

    print("你是你\f我是我\f你不是我\f我不是你")  # 走纸换页用的，一般没什么用

    print("你是人吗？\r我不是人！")  # 做打印小动画有用 相当于把当前行给删了
    # animation()
    tab()
    warp()
    v()
    input("end....")
    return None


if __name__ == "__main__":
    main()
