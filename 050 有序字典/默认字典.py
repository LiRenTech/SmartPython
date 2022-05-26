import random
from collections import defaultdict

ddic = defaultdict()

string = "qwertyuiop"
for char in string:
    ddic[char] = 1

print(ddic)
print(ddic.keys())

# 用于实现字典套列表，字典套集合，就可以表示图的结构
"""
defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值，返回的是工厂函数的默认值
"""
b = defaultdict(list)
b["第一个"] = '一个字符串'
b["第二个"].append(1)
print(b)

graph = defaultdict(set)

for i in range(10):
    for _ in range(3):
        graph[i].add(random.randint(1, 10))
print(graph)

numIndex = defaultdict(int)  # 默认返回0


