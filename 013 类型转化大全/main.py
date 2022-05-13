"""

int         float           bool            None            complex




list        str             set             tuple




dict
"""

# 基础数据类型之间的相互转化
# print(bool(1))
# print(bool(12))
# print(bool(0))
#
# print(bool(0.0))
# print(bool(0.1))

print(bool(0 + 0j))
print(bool(0 + 1j))
print(bool(1 + 0j))

# print(int(1 + 35j))  # bug!
# print(float(1 + 35j))  # bug!
# 虚数不能转成float 和 int


# 复合数据类型之间的相互转化
print(tuple({1, 2, 3}))

t = (1, 5, 10)
set(t)
print(set(t))

# 含有不可哈希的元素，不可转化


# t = (1, [], 10)
# set(t)
# print(set(t))
# 什么样的对象是可以哈希的？
# 不可哈希的：
"""
[]
{set}
{dict}
(..含有不可哈希的东西的...)
class Node...(自定义对象没有实现__hash__方法)
"""


class Node:
    def __init__(self):
        self.val = None

    def __hash__(self):
        return hash(self.val)


# 可以哈希的
"""
基础数据元素
1, 2, 3, 1.4, "abc..."
None, True, False
1 + 1j

(基础数据元素, 基础数据元素, 基础数据元素, ...)
(1, 2)
((基础),(基础),(基础))
((1, 2), (2, 2))
"""

print(hash(((1, 2), (2, 2))))
print(hash(((1, 2), (2, False, "abcabc"))))  # 类型不一样也是可以的


# print(tuple("abcabc"))
# print(str((1, 2, 3)))
# # e = eval("(1, 2, 3)")
# # print(e, type(e))
# e = eval("[1, 2, 3]")
# print(e, type(e))
# e = eval("{1, 2, 3}")
# print(e, type(e))

class A:
    def __init__(self):
        ...


a = A()
s = str(a)
# 如果没有给自定义对象实现字符串化的方法，就会转化成内存地址的字符串表示
print(s)

"""
10种类型两两组合有45种组合，45乘以2就有90种转化，不可能一一列举。
图
没必要吧 10种类型所有的两两组合都讲一遍，只讲有用的
其他没讲的都是大同小异。

"""

from collections import Counter

s = "abababbbaabbc"
dic = Counter(s)
print(dic)
# 为什么多套了一个Counter，在打印的时候
# 其实Counter是dict的子类，比较值得话其实还是一样的。
print(dic == {'b': 7, 'a': 5, 'c': 1})  # 值是相等的
print(dic is {'b': 7, 'a': 5, 'c': 1})  # 两个不是一个对象，地址不一样，甚至这两行右边的写了两遍的地址也不一样

print(Counter([1, 1, 2, 3]))

s = "{'b': 7, 'a': 5, 'c': 1}"
e = eval(s)
print(e, type(e))

# s = {1, 2, 3}
# print(dict(s))  # 不能

dic = Counter("ababababa")

print(dic.keys(), type(dic.keys()))
print(dic.values(), type(dic.values()))

print(['a', 'b'] == dic.keys())  # x
print(('a', 'b') == dic.keys())  # x
print([1, 2] == [1, 2])  # 对

# 但是你可以这样
print(list(dic.keys()))
print(list(dic.values()))
print(tuple(dic.keys()))
print(tuple(dic.values()))

print(list(dic.items()))  # [('a', 5), ('b', 4)]  组合成对
print(tuple(dic.items()))

# 复杂数据类型转bool

# 应用场景，做算法题检测列表是否是空的，特殊条件处理

arr = []
if not arr:
    print("empty")

# 原理：
print(bool(arr))  # False
if not bool(arr):
    print("empty")

print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(set()))  # False

print("=====")

# 数组
print(bool([1, 2, 3]))  # True
print(bool([None]))  # True
print(bool([...]))  # True
print(bool([[]]))  # True
# 元组
print(bool((1, 1)))  # True
print(bool((())))  # False
print(bool(((),)))  # True  不要小看这个小逗号，对解析非常有影响
print(bool(((((((((((((()))))))))))))))  # False
print(bool((((((((((((((),))))))))))))))  # True

# 元组和字典
print(bool({{{{{}}}}}))
print(bool({2: 1}))  # True
print(bool({None}))  # True
