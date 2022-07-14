"""
文件名对导入问题的影响
"""

# import 123
# from . import 123

# import ^_^
# from . import ^_^
# wdnmd 导入不了！

import 离谱
#
print(离谱.离大谱)
print(离谱.离离原上谱)
离谱.离离原上谱.append(离谱.离大谱)
print(离谱.离离原上谱)
#
# # 其实也没什么离谱的，python3 utf-8的支持。
# 不推荐用中文，麻烦，虽然队友看到不会砸掉你的电脑，但是你也快了。

import _file

print(_file._arr)  # 只有一个下划线的警告了
print(_file.__dic)  # 两个下划线的没有警告




