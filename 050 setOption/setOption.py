# 集合操作符总结一下

s1 = {1, 2, 3}
s2 = {2, 3, 4}
# print(s1 + s2)  # bug

print(s1 & s2)  # 与 Tom & Jerry
print(s1 | s2)  # 或
print(s1 ^ s2)  # 非 shit + 6 = ^

print(s1 and s2)
print(s1 or s2)
print(not s2)
print(not s1)
print(s1.difference(s2))
while s1:
    print(s1)
    s1.pop()

s3: set
# 如何实现一个有序集合
