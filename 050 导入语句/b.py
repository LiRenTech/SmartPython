
# from typing import List

# from typing import a  # 被覆盖了
#
# print(a)

# from typing import _b, _, a, __c

# print(a, _b, _, __c)  # 想要什么都能导入进来，有针对性质的导入


from typing import *
# print(a)
# print(_b)  # 找不到了啦！
# print(_)
# print(__c) # 凡是下划线开头的都不能正常引入

# func()
# _func()
# __func() 带下划线不行

"""
用途：在模块里写了一些临时变量存储，但是不想对外开放，不想给别人用，修改造成危险，就可以加前导下划线。
"""
# from c import C
#
# cObj = C()
# cObj.gogogo()
# cObj.gogogo()



