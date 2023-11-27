# .f().f().f() 的方式
class MyClass1:
    def __init__(self):
        self._v = 0

    def add(self, v):
        self._v += v
        return self


c1 = MyClass1()
c1.add(1).add(1).add(5).add(10)


def f(*args, **kwargs):
    # 在这里对参数进行判断，进行不同的操作逻辑...
    return f


f('eat')('sleep')('sing')


class MyClass2:
    def __init__(self):
        self._v = 0

    def __getitem__(self, item):
        self._v += item
        return self

    def __call__(self, *args, **kwargs):
        # 结尾加一个小括号只是消除pycharm的警告
        return self


c2 = MyClass2()
c2[1][1][2][10][5][6]()


# .a.a.a的方式
class A:
    @property
    def b(self):
        return self

    def __call__(self, *args, **kwargs):
        return self


a = A()
a.b.b.b.b.b.b.b()
