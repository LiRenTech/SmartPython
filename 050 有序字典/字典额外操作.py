# 合并字典

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)
# {'a': 1, 'b': 3, 'c': 4}

#  如果存在相同的key，来自第一个字典的key会被覆盖。

