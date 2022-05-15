
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
print(bool())  # False
print(bool(((),)))  # True  不要小看这个小逗号，对解析非常有影响
print(bool(((((((((((((()))))))))))))))  # False
print(bool((((((((((((((),))))))))))))))  # True

# 元组和字典
# print(bool({{{{{}}}}}))
print(bool({2: 1}))  # True
print(bool({None}))  # True
