# -*- encoding: utf-8 -*-
"""
PyCharm 基本理论
2022年07月01日
by littlefean
"""
from dataclasses import dataclass

"""

万物皆对象

int、bool、float、list 都是对象，没错的，1也是个对象


"""
a = 1
a.bit_length()
print(a.numerator)
print(a.imag)

"""
区分属性和变量
动态添加属性
对象里有一些内置属性 a.__dict__

对象属性的增删改查

动态添加属性只能是一个的
o1.a = 1
o2.b = 2
o2.a ??? no!!


类属性的增删改查

实例属性  去找  类属性  优先查找机制
实例属性去改 __class__

"""


class A:
    count = 1
    ...


a = A()
print(hasattr(a, "ab"))

a.ab = 1555
print(hasattr(a, "ab"))

a.__class__.count = 22

print({}.__sizeof__())
print(set().__sizeof__())
print([].__sizeof__())
print(().__sizeof__())
print(a.__sizeof__())

"""
用类属性限制产生的实例的属性

__slots__
"""


class C:
    __slots__ = ["x", "y"]
    ...


c1 = C()
c1.x = 15
# c1.z = 15

c1.__class__.__slots__.append("z")
print(C.__slots__)  # ['x', 'y', 'z']


# c1.z = 15  # 这样也不行了

class D:
    __slots__ = ["a", "b"]

    def __init__(self, c):
        self.c = c
        self.a = 1
        self.b = 1

d = D(123)


"""
概念区分
类产生对象
但是类也是对象
所以应该这样叫

类产生实例
类和实例都是对象

"""

"""
self 参数的理解
man.eat()

Person.eat(self)
用实例调用实例方法的时候，第一个self参数会自己把自己调用进去，就不用再填了。

如果你的实例方法什么都没写，没写self，一个参数都没有
会报一个硬多给了一个参数的错误

"""


class Person:
    def __init__(self):
        self.name = "human.."

    def eat(self, n):
        print(f"human {self} Eat!", n)


p1 = Person()

Person.eat(p1, 1)

p1.eat(1)

"""
所有的方法都是存在类对象里的
"""

"""
类方法：
用实例也可以调用类方法

可以玩对象绑定
新建一个func = 那个类.那个类方法
然后 func() 就可以了

类方法也是
cls 参数传的是这个类或者这个类的子类
"""

"""
用type元类创建类
def say
type("Person", (), {"count": 0, "say": say})
"""


def say(self):
    print(self, "eat")


Person = type("Person", (), {"count": 0, "say": say})

p = Person()
p.say()

"""
指明元类
类检测元类的优先：自己类指定、父类指定、模块级别指定、type
"""

__metaclass__ = type


class P:
    __metaclass__ = ...


# class Pe(metaclass=):
#     ...


"""
私有属性的意义
setAge，可以设置数据检测 0< x < 200 且类型必须是int

xx_  避开关键字
__xxx__ 系统内置属性

只读属性是 _xx 然后只提供get方法

@property
def age():
    ...
    
这样也就不能设置属性了

"""


class Board:
    def __init__(self):

        self.__board = [[0] * 19 for _ in range(19)]

        # 只读属性
        self.__boardWidth = 19

        self._boardName = "xxx"

    @property
    def width(self):
        return self.__boardWidth

    # 棋盘名字的get和set

    @property
    def boardName(self):
        return self._boardName

    @boardName.setter
    def boardName(self, name):
        if type(name) == str:
            self._boardName = name

    def setBoard(self, value, x, y):
        if type(x) == type(y) == int and x in range(19) and y in range(19):
            self.__board[y][x] = value
            ...
        else:
            # 越界的操作、非法的操作可以直接当作什么都没做处理
            # 减少了出bug的可能性
            pass


"""
str repr 区别
"""


@dataclass
class Student:
    name: str
    score: int

    def __str__(self):
        return f"({self.name}, {self.score})"

    def __repr__(self):
        return f"({self.name}, {self.score}, {id(self)})"


s1 = Student("liu", 19)
print(s1)
print(repr(s1))

arr = [Student("", 1), Student("", 1), Student("", 1)]  # 在内层用的是repr
# 如果是在终端情况下，直接敲这个实例，返回这个实例的repr形式
print(arr)
# print 先找 __str__ 如果没有就先会找 __repr__ 如果再没有就 id了


# repr 面向程序员 str 面向用户
# repr 还可以 o = eval(repr(obj))

"""
中括号方法对应的三个魔术方法
p[?]      getitem
p[?] = ?  setitem
del p[?]  delitem
"""
