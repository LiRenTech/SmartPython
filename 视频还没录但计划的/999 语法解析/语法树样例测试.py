"""
if - elif - else 在语法树里会翻译成 if else 嵌套


"""

from _ast import *
import ast


class For(For):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs["orelse"]:
            # 有else 接在了 for 后面
            ...
        ...

    ...


class While(While):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs["orelse"]:
            print("while else!!!")
            # 有else 接在了 for 后面
            ...
        ...


def main():
    string = """
while True:
    ...
else:
    ...
"""
    root = ast.parse(string)
    d = ast.dump(root)
    eval(d)
    myPrint(d)


def myPrint(string: str):
    tab = 0
    tabStr = "    "
    for char in string:
        if char in "([{":
            # print()
            # print(tabStr * tab, end=char)
            print(char, end="")
            tab += 1
            print("\n", end=tabStr * tab)
        elif char in ")]}":
            print()
            tab -= 1
            print(tabStr * tab, end=char)
        elif char == ",":
            print(char)
            print(tabStr * tab, end="")
        else:
            print(char, end="")
        ...
    ...


if __name__ == "__main__":
    main()
