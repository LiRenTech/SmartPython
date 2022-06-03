# 集合操作符总结一下

s1 = {1, 2, 3}
s2 = {2, 3, 4}
# print(s1 + s2)  # bug

print(s1 & s2)  # 与 Tom & Jerry
print(s1 | s2)  # 或
print(s1 ^ s2)  # 非 shit + 6 = ^

print("and", s1 and s2)  # &
print("or", s1 or s2)  # ???
print(not s2)  # 判断空取反
print(not s1)  # 判断空取反
print(s1.difference(s2), s1 - s2)  # 差集

while s1:
    print(s1)
    s1.pop()

s3: set

# 不报错的删除
s = {1, 2, 3}
s.remove(2)
s.discard(2)

# 如何实现一个有序集合


# in

# 集合之间的包含关系
print({1, 2, 3} <= {1, 2, 3, 4})
print({1, 2, 3} <= {1, 3, 4, 5})

# 集合占用内存？
print({1}.__sizeof__())
print({1, 2}.__sizeof__())
print({1, 2, 3}.__sizeof__())
print((1,).__sizeof__())
print([1].__sizeof__())
print([1, 2, 3].__sizeof__())
print("1".__sizeof__())
print({n for n in range(333)}.__sizeof__())  # 返回的单位是比特
