class A:
    ...


class B(A):
    ...


class C(B):
    ...


b = B()
c = C()

print(type(b))  # <class '__main__.B'>
print(type(b) == A)  # False
print(isinstance(b, A))  # True

# b的类型是A的类型 如果用户自己写了一个MyInt类，isinstance可以识别出来int。
# isinstance 更好

print(type(c))  # <class '__main__.C'>
print(type(c) == A)  # False
print(type(c) == B)  # False
print(isinstance(c, A))  # True
print(isinstance(c, B))  # True

# isinstance可以识别继承
# 这只是个demo，录视频的时候可以加更多东西

print(isinstance(c, (A, int, dict)))  # 可以写更多的东西，相当于or在一起

# 举一些实际的例子
# 找到以前的使用type的地方。

# 做点补充，各种内置类的继承关系

print(type(None))

# 复杂的继承关系

issubclass(A, B)  # 和isinstance的区别就是第一个参数传入的是类，而不是实例

# 这时候再把三种物质都拿出来，元类，类，实例
# 那么类可不可以是元类的实例

# 可以结合assert使用
assert isinstance(b, B)

