# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年08月28日
by littlefean
"""
import code
from builtins import callable
from typing import *
import ast


def isPrim(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


Function = isPrim.__class__

print(isPrim.__class__)
# a = Function()  # 参数要传code对象

# print(a)
for k, v in Function.__dict__.items():
    print(k, v)

# 发现 函数类 有 __code__内置属性
print(isPrim.__code__)
# <code object isPrim at 0x000001744583ADB0, file "D:/LiRen/SmartPython/禁用xxx系列/禁用def/aaa.py", line 13>
print(type(isPrim.__code__.__class__))
print(type(isPrim.__code__))
print(repr(isPrim.__code__))
print(isPrim.__code__)  # 无法字符串化

# print(sin.__code__, "...")  #  'builtin_function_or_method' object has no attribute '__code__'
# 拿到code类

# 需要十三个参数！！！？！！
# a = type(isPrim.__code__)(0, 0, 0, 0, 1024, 1, "")
print(isPrim.__code__.co_flags)  # 67
print("code:", isPrim.__code__.co_code)
c = b'|\x00d\x01k\x00r\x0cd\x02S\x00x.t\x00d\x01t\x01|\x00d\x03\x13\x00\x83\x01d\x04\x17\x00\x83\x02D\x00]\x14}\x01|\x00|\x01\x16\x00d\x05k\x02r$d\x02S\x00q$W\x00d\x06S\x00'

print(c.decode("ISO-8859-1"))
"""
class CodeType:
    Create a code object.  Not for the faint of heart.
    这行代码在 types.pyi 58行
    
CodeType(self: CodeType, argcount: int, posonlyargcount: int, kwonlyargcount: int, nlocals: int, stacksize: int, flags: int, codestring: bytes, constants: Tuple[Any, ...], names: Tuple[str, ...], varnames: Tuple[str, ...], filename: str, name: str, firstlineno: int, lnotab: bytes, freevars: Tuple[str, ...] = ..., cellvars: Tuple[str, ...] = ...)
"""


class Func:
    def __init__(self):
        ...
