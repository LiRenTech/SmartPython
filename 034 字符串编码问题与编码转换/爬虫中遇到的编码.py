# -*- encoding: utf-8 -*-
"""
PyCharm 爬虫中遇到的编码
2022年07月10日
by littlefean
"""
import base64
from typing import *


def main():
    """"""
    # html = HtmlGetter(url, encode="ISO-8859-1", decode="utf-8").get()

    # 爬虫发现 response.text 是一堆乱码
    # 怎么办，先把乱码 转化成 比特流 这个过程叫加密，用 ISO-8859-1
    # 转化成比特流之后，再解密成 字符串 解密用 utf-8
    # 这个转化成01010的比特流就很重要，因为加密成正确的比特流之后，
    # 我们就可以把它转化成各种不同的编码了，我们最常用的就是 utf-8，所以一般解密我们都是用的utf-8

    """
    response = requests.get(self.url, headers=self.headers, verify=False)
    html = response.text
    # html = html.encode("ISO-8859-1")
    # html = html.decode("utf-8")
    if self.encode != "":
        html = html.encode(self.encode)
    if self.decode != "":
        html = html.decode(self.decode)
    
    """
    print("这是中文".encode())  # 默认不写是utf8
    print(type("这是中文".encode()))
    a = bytes()
    print(a)
    print(b"0100110001011001\056abzwo")
    # print(b"0100110001011001\056abzwo中文")  # SyntaxError:
    # can only contain ASCII literal characters

    print(b"0100110001011001\056abzwo")

    # ascii扩展码部分
    # print(b"²")
    # print(b"≡")
    # ASCII range???
    # ASCII码正规127个，最大附加到了255个
    # 扩展码不是标准的ASCII码

    # 字节数组 trans

    b = b"abc123567"
    print(list(b))
    print(list(b"\065\48\1\2\3\4\5\6\7"))
    """
    ascii 记忆方法
    死吧！ 0，零表示一个穷光蛋，都一分钱没有了，死吧！
    留屋！ A，A是长辈，爷爷，应该让他留在屋里，不要让他再外面风吹日晒了
    酒气！ a，小a是你的爸爸，天天出去喝酒，所以一身酒气。
    """
    print(chr(48))
    print(chr(65))
    print(chr(97))

    print("这拆成是".encode())

    # ISO-8859-1 编码
    # 向下兼容ASCII
    print(0xff)
    print(0x7F)

    # gbk 国标，扩展
    return None


if __name__ == "__main__":
    main()
