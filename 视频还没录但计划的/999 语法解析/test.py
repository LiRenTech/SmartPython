import ast
import pprint

# https://blog.csdn.net/ThinkTimes/article/details/110831176

# 直接传入字符串
# ast.literal_eval("a = 155")
string = """
for i in range(10):
    ...
else:
    ...
"""
root = ast.parse(string)
d = ast.dump(root)

print(d)

from _ast import *
from keyword import *
from collections import Counter

count = {item: 0 for item in kwlist}


class For(For):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        count["for"] += 1
        ...

    ...


class FunctionDef(FunctionDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        count["def"] += 1


a = Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=ListComp(elt=Name(id='i', ctx=Load()), generators=[
    comprehension(target=Name(id='i', ctx=Store()),
                  iter=Call(func=Name(id='range', ctx=Load()), args=[Num(n=10)], keywords=[]), ifs=[], is_async=0)]))])
print(count)
