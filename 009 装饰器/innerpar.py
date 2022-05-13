# def outer(x):
#     def plus(a, b):
#         return a + b
#
#     for i in range(10):
#         x = plus(x, 10)
#     return x

def logger(oldFunc):
    """夹层装饰器，给函数调用前后加两个打印突出显示"""
    def newFunc():
        print("~~~~~~~~~~~")
        oldFunc()
        print("~~~~~~~~~~~")
        ...

    return newFunc


def logger2(oldFunc):
    """夹层装饰器，只给头顶增加一个打印"""
    def newFunc():
        print("+++++++++++")
        oldFunc()
        ...

    return newFunc


def runDouble(oldFunc):
    """给一个函数装饰，装饰后这个函数就能运行两次了"""
    def newFunc():
        oldFunc()
        oldFunc()

    return newFunc


def counter(oldFunc):
    """记录一个函数打印了多少次"""
    count = 0

    def newFunc():
        nonlocal count
        count += 1
        oldFunc()
        print(f"这个函数{oldFunc.__name__}运行了{count}次")
        ...

    return newFunc


def shield(oldFunc):
    """防护盾装饰器，让一个函数在运行中不会发生错误导致程序终止"""
    def newFunc():
        try:
            oldFunc()
        except Exception as e:
            print(f"函数{oldFunc.__name__}出错了", oldFunc, e)

    return newFunc()


from functools import lru_cache


@lru_cache(None)
def func():
    print("hello")


@lru_cache()
def func2():
    ...


class Check(object):
    """类装饰器"""
    def __init__(self, fn):
        """
        传入的是被装饰的原的函数
        """
        self.__fn = fn

    def __call__(self, *args, **kwargs):  # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用
        print("登录")  # 在这之前可以写登录代码
        self.__fn()


@Check  # @Check <===> comment = Check(comment)
def comment():
    print("正在发表评论")


def robot(oldFunc):
    def newFunc(*args):
        print("started")
        res = oldFunc(*args)
        return res

    return newFunc


@robot
def f():
    ...
