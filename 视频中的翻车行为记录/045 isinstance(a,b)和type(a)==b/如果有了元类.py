# assert isinstance(b, C)


class AType(type):
    ...


class A(metaclass=AType):
    ...


print(isinstance(A, AType))  # True
aa = A()
print(isinstance(aa, AType))  # False 隔了一层，就不是了

print(isinstance(type, type))  # True type它自己创造了它自己


# class MyClass:
#     ...


# MyClass.__base__ = MyClass
# __base__ 是只读属性，不能更改
# print(isinstance(MyClass, MyClass))

# ===========

class Y1(type):
    ...


class C1(metaclass=Y1):
    ...


class C2(C1):
    ...


print(isinstance(C2, Y1))  # True

c2 = C2()
print(isinstance(c2, Y1))  # False 不能隔层
print(isinstance(C2, type))  # True
print(type(C1))  # Y1
print(type(C1) is Y1)
print(type(C1) is type)
print(isinstance(C1, type))
# type 就只能跟着箭头往右走一次
print(type(C2) == Y1)
print(type(C2) == type)


# 如果不能往右走，那就先往下走，再往右走

# ===============

class M1(type):
    ...


class M2(M1):
    ...


class Class22(metaclass=M2):
    ...


class Class23(Class22):
    ...


print(isinstance(Class23, M1))  # True
print(type(Class23))
"""
结论，
某一个东西 type 一下，找到的是逆着箭头走，一旦跨过分界线就停止的东西
而isinstance 则是跨过分界线板块后的那些所有的东西
而issubclass 则是不跨过分界线的所有部分

"""
