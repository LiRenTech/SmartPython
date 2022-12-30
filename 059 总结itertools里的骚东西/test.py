from itertools import *

arr = [1, 2, 3, 4, 5]

# acc 前缀和
acc = accumulate(arr)
print(list(accumulate("ABCDEF")))
print(list(acc))

# chain 把各种序列串起来
ch = chain(arr, {1, 3, 4}, {"a": 12, "b": 155})
print(list(ch))

for item in ch:
    print(item)

# combinations  组合数 讲过了

combinations_with_replacement("ABCDEFG", 3)  # 可以重复的

com = compress("ABCDEFG", [True, False, True, False, True, False, True])
for item in com:
    print(item)

# 如果长度不匹配怎么办


# ==== count
# 根老师对着干
# for i in count(10):
#     print(i)
# 这样就停不下来了
# 还用于 zip() 来添加序列号
# (start + step * i for i in count())

# for item in cycle("ABCDEF"):
#     print(item)

# dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
# 根据标准丢弃元素，一旦发现没有达到丢弃标准，这个及其后面的都要

# filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
# 输入一个标准，和一坨东西，在一坨东西中找符合标准的

# 和filter相反，filter 得到的是不符合标准的东西，意思就是过滤
for item in filter(lambda x: x % 2, range(10)):
    print(item)

print([item for item in groupby("AABBCCDD")])
print([k for k, g in groupby('AAAABBBCCDAABBB')])
print([list(g) for k, g in groupby('AAAABBBCCD')])

# 和切片一样的
# islice('ABCDEFG', 2) --> A B
# islice('ABCDEFG', 2, 4) --> C D
# islice('ABCDEFG', 2, None) --> C D E F G
# islice('ABCDEFG', 0, None, 2) --> A C E G

print([item for item in pairwise("ABCDEFG")])
print([a + b for a, b in pairwise("ABCDEFG")])  # 3.10

print([item for item in product(range(3), repeat=4)])

print([item for item in repeat(10, 5)])

print(list(map(pow, range(10), repeat(2))))  # ??? map

print(list(starmap(pow, [(2, 5), (3, 2), (10, 3)])))  # [32, 9, 1000]
# 用于[AB, AB, AB]类型的列表，两两结合变成新列表

# takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
# 和dropwhile相反

print(list(zip_longest("ABCDEF", "1234", fillvalue="?")))

# =========== 自带
#
# zip()
# map()
# filter()
# from functools import reduce
#
# reduce()

print("==" * 20)
print(list(chain("abc", "def")))
print(list(chain("abc", "def", [1, 2, 3])))
print(list(chain("abc", "def")))
print(list(chain.from_iterable(["abc", "BCD", "QWE"])))
# chain from_iterable 只能拆一层

# reduce(lambda a, b: a * b, [1, 3, 4, 5, 4, 3])

from functools import reduce
from operator import mul

reduce(mul, [1, 3, 4, 5, 4, 3])
n = 5
print(reduce(lambda a, b: a * b, list(range(1, n + 1))))


def f(n): return 1 if n == 0 else n * f(n - 1)


print(list(pairwise("ABCDEF")))
# starmap()


# =============

import itertools

m = itertools.groupby([93, 15, 5, 4, 12, 24, 42], lambda x: x % 3 == 0)
for k, v in m:
    print(k, list(v))

# =============

g = (i for i in range(10))
for n in islice(g, 5):
    print(n)

dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])
takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])

for num in [134514] * 5:
    print(num)

for num in repeat(134514, 5):
    print(num)

# [1^2, 2^4, 3^6, 4^8 ...]
# a = 1
# b = 2
# while True:
#     print(a ** b)
#     a += 1
#     b += 2

arr = [2, 0, 7, 7, 0, 5, 1, 5]
for a, b in zip(arr, cycle([1, -1])):
    print(a * b)  # 正负交替

word1 = "abcdefghij"
word2 = "134514"
from operator import add
print("".join(starmap(add, zip_longest(word1, word2, fillvalue=""))))

# print(sum(count(1)))

print(list(compress("ABCDEFG", [1, 1])))