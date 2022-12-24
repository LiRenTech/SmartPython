"""



"""

import os
from keyword import kwlist
from _ast import *
import ast
from collections import defaultdict

# 统计数量的信息
COUNT_DIC = defaultdict(int)
# 统计使用率
COUNT_FREQUENCY_DIC = defaultdict(int)

ignore = set("for while def with".split())

docDic = {
    'False': "假值，可以经过int转化为0",
    'None': "空值",
    'True': "真值，可以经过int()转化为1",
    'and': "逻辑与",
    'as': "起别名，通常和import,with 连用",
    'assert': "断言语句",
    'async': "异步",
    'await': "异步",
    'break': "跳出循环使用",
    'class': "定义类",
    'continue': "继续本轮循环",
    'def': "定义函数",
    'del': "删除对象",
    'elif': "多年不写py之后最容易写错的关键字",
    'else': "和if连用，也可以和for，while连用",
    'except': "和try连用一起捉虫子",
    'finally': "出事儿后的善后工作",
    'for': "循环，也在列表推导式中出现",
    'from': "引用时候使用",
    'global': "在函数中声明某个变量是全局变量",
    'if': "条件判断",
    'import': "引入模块",
    'in': "属于一种运算符",
    'is': "内存地址是否相同",
    'lambda': "缩句爱好者使用，但需要保证一行实现",
    'nonlocal': "当出现函数嵌套的时候，你要在内层修改外层的变量",
    'not': "逻辑非",
    'or': "逻辑或",
    'pass': "py特色",
    'raise': "产生了错误",
    'return': "函数的出口",
    'try': "捉虫子专用",
    'while': "发现死循环的时候通常是这里出了问题",
    'with': "经常打开文件的时候使用，经典as f",
    'yield': "生成器",
    "ForElse": "接在for后面的else",
    "WhileElse": "接在while后年面的else",
    "ClassDef": "类里的方法",
    "AsyncFunctionDef": "异步函数",
    "AsyncFor": "异步循环",
    "AsyncWith": "异步with",
}


class For(For):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        COUNT_DIC["for"] += 1
        if kwargs["orelse"]:
            COUNT_DIC["ForElse"] += 1


FLAG = []


class While(While):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs["orelse"]:
            COUNT_DIC["WhileElse"] += 1
            FLAG.append(1)


class ClassDef(ClassDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        COUNT_DIC["ClassDef"] += 1


class FunctionDef(FunctionDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        COUNT_DIC["def"] += 1


class AsyncFunctionDef(AsyncFunctionDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        COUNT_DIC["AsyncFunctionDef"] += 1


class AsyncFor(AsyncFor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        COUNT_DIC["AsyncFor"] += 1


class With(With):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        COUNT_DIC["with"] += 1


class AsyncWith(AsyncWith):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        COUNT_DIC["AsyncWith"] += 1


def count(scriptPath: str):
    print("\t>>>", scriptPath)
    with open(scriptPath, encoding="utf-8") as f:
        try:
            codeStr = f.read()
        except UnicodeDecodeError:
            print("编码错误 UnicodeDecodeError ", scriptPath)
            return
    try:
        eval(ast.dump(ast.parse(codeStr)))
    except MemoryError:
        return
    except NameError:
        print("nameErr", scriptPath)
    except SyntaxError:
        print("SyntaxError", scriptPath)

    for line in codeStr.split("\n"):
        if line.startswith("#"):
            continue
        words = line.split()
        for kw in kwlist:
            if kw in ignore:
                continue
            n = words.count(kw)
            COUNT_DIC[kw] += n
        # 额外统计 try:
        COUNT_DIC["try"] += words.count("try:")

    ...


def countByFolder(path: str):
    """统计一个文件夹下所有的py文件"""
    for path, folders, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                count(path + os.sep + file)


def main():
    countByFolder(r"D:\LiRen\SmartPython")
    countByFolder(r"D:\理刃科技\制作---程序\Littlefean Python")
    countByFolder(r"D:\Software\WorkSoftware\Python\Lib\site-packages")
    showList = [(k, v, docDic[k]) for k, v in sorted(COUNT_DIC.items(), key=lambda x: x[1], reverse=True)]
    for i in range(3):
        for item in showList:
            print(item[i], end="\t")
        print()


if __name__ == "__main__":
    main()
