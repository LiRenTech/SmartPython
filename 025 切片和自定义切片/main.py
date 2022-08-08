a = [i for i in range(10)]

print(a[:])

print(a[::])

# print(a[::, :])

s = slice(1, 5)

# s_ = [1:5]  # 不能单独提出去

print(a[s])

print(s.start)
print(s.stop)
print(s.step)

s2 = slice(1)
print(s2.start, s2.stop, s2.step)

# print(a[:5, 5:])

print([i for i in range(100)][::3][::-1])
print([i for i in range(100)][::-3])
print([i for i in range(100)][::-0x2])
print([i for i in range(100)][True + True:True * 10:])
print("<<", [i for i in range(100)][True + True:True << 5:])

# [a: b: c]
"""
a 开始下标 -1表示最后一个元素
b 结束下标
c 步长，如果是负数，就再翻转一下，如果是0，就不选择了
"""

print([i for i in range(100)][-20: 20])  # start 和end空了，没有交集了
print([i for i in range(10)][-10: -1])
print([i for i in range(10)][5: -2])
print([i for i in range(10)][5: -10])  # 越界自动为空
print([i for i in range(10)][500: -10])  # 越界为空


# 步长为负数的时候的顺序问题  待研究
print([i for i in range(10)][2:5:])
print([i for i in range(10)][2:5:2])
print([i for i in range(10)][2:5:-1])  # []
print([i for i in range(10)][2:5][::-1])  # []
