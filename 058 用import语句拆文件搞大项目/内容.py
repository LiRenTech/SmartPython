"""
用import 语句搞大项目
"""

# import 的写法

"""
基础内容：

import xxx
from xxx import xxx
import numpy as np
as的作用是起别名

"""

# 跨文件夹引入办法

"""
项目文件夹
    main.py
    文件夹1
        a.py
    文件夹2
        文件夹3
            b.py

-------
其中，a.py中有一个A类，b.py中有一个B类
如果a.py中想要引入b.py里的B类，那么就需要在a.py的最上面写上
from 文件夹2.文件夹3.b import B
原则就是从项目文件夹开始走，逐层找到要找的py文件


"""

# 循环引用

"""
a.py
b.py
-------
其中 a.py 中有一个f函数，b.py 中有g函数
如果 f函数调用g函数，g函数内部调用f函数，
b.py:
from a import g

a.py:
from b import f

无法实现。会出现循环引用的问题
但改成
b.py:
import a
a.py:
import b

然后调用的时候
a.f()
b.g()
这样就不会出现循环引用的问题了

但如果不是函数，是类，这样写就又不行了
通常这样的设计会是：
假设一个银行系统，为客户建立了People类，为各种银行卡建立了Card类。
People类里记录着开卡信息（用Card类描述），Card类里也需要说明拥有者信息（用People类描述）。

可以使用注解来实现，目的是写起来有代码提示。
详见视频
"""


