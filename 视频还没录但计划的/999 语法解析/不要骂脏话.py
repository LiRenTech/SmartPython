from typing import *
import time
import ast
import inspect

import ast


def deco(oldFunction):
    def newFunction(*args, **kwargs):
        t1 = time.perf_counter()
        res = oldFunction(*args, **kwargs)
        t2 = time.perf_counter()

        return res

    return newFunction


def noPrint(oldFunc):
    def newFunc(*args, **kwargs):
        oldFuncStr = inspect.getsource(oldFunc)
        newStr = "".join(line + "\n" for line in oldFuncStr.split("\n") if not line.strip().startswith("print("))
        exec(newStr, oldFunc.__globals__)
        # return oldFunc(*args, **kwargs)

    return newFunc


class DirtyWordsException(BaseException):
    ...


def noFunk(oldFunc):
    def newFunc(*args, **kwargs):
        oldFuncStr = inspect.getsource(oldFunc)
        root = ast.parse(oldFuncStr)
        for node in ast.walk(root):
            if isinstance(node, ast.Name) and "fuck" in node.id.lower():
                raise DirtyWordsException("脏话")
        return oldFunc(*args, **kwargs)

    return newFunc


# @noFunk
arr = []


@noPrint
def f():
    fuck = 155
    bbb = 1
    arr.append(15)
    print(bbb)
    print(123)
    return


f()
print(arr)
# Module(body=[
#     FunctionDef(name='f', args=arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
#                 body=[Assign(targets=[Name(id='bbb', ctx=Store())], value=Num(n=1)), Expr(
#                     value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='bbb', ctx=Load())], keywords=[])),
#                       Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Num(n=123)], keywords=[])),
#                       Return(value=None)], decorator_list=[Name(id='noFunk', ctx=Load())], returns=None)])
