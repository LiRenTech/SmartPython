import ast
import keyword
import operator
import pprint

# https://blog.csdn.net/ThinkTimes/article/details/110831176

# 直接传入字符串
# ast.literal_eval("a = 155")


# from _ast import *
import ast
import _ast
from keyword import kwlist
from collections import defaultdict

counting = defaultdict(int)


def decoClass(cls):
    """
    传入一个类，这个类必须是语法树类
    这个函数会给这个类加工，更改init方法，让他变得能够统计
    Args:
        cls:

    Returns:

    """

    def f(func):
        def newFunc(*args, **kwargs):
            counting[cls.__name__] += 1
            return func(*args, **kwargs)

        return newFunc

    cls.__init__ = f(cls.__init__)


# decoClass(For)
# decoClass(Nonlocal)
# decoClass(If)
# decoClass(Assert)
# decoClass(AsyncFor)
# decoClass(AsyncWith)
# decoClass(AsyncFunctionDef)
# decoClass(FunctionDef)

# for classStr in dir(_ast):
#     setattr(eval(f"_ast.{classStr}"), "a", 12)
#     ...

string = """
def f():
    print("哈哈")
    ...

for i in range(1000):
    for j in range(10):
        f()
        print(i * j)
"""
root = ast.parse(string)
d = ast.dump(root)

print(d)

for node in ast.walk(root):
    print(node, node.__class__)   # __class__ 拿到这个节点属于什么类

# eval(d)

print(counting)
