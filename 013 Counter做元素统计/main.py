from collections import Counter
from random import randint
from time import perf_counter

s = "🐕💩🐕💩🐕💩🐕💩🐕💩🐕🐕🐕🐕💩💩💩💩💩💩"

dic = {}

string = ""

for _ in range(100_0000):
    # 可以随便加下划线，不能连续加两个
    string += str(randint(0, 9))
    ...

print(string)
t1 = perf_counter()

dic = {}
for char in string:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1

t2 = perf_counter()
dic2 = Counter(string)
t3 = perf_counter()
print(t2 - t1, t3 - t2)  # 快四倍左右
