# -*- encoding: utf-8 -*-
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
# indent 用于设置缩进 4 就是四个空格

# 随便找的一个json文件
with open("j.json", encoding="utf-8") as f:
    d = eval(f.read())
# pp.pprint(d)  # 直接打印格式化后的形式

string = PrettyPrinter(indent=1, width=20, depth=None, compact=False, sort_dicts=True).pformat(d)
# 打印的层级数量由 depth 控制 如果数据结构的层级被打印得过深，其所包含的下一层级会被替换为 ...
# compact = False 则长序列的每一项将被格式化为单独的行。
# compact = True 则将在 width 可容纳的的情况下  把尽可能多的项放入每个输出行。(就是每一项打完换不换行的意思）
# sort_dicts=True 字典的键会排序后输出显示

print(string)
