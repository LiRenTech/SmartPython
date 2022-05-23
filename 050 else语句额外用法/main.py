"""
大家都熟悉的
if else
if elif else
if elif elif elif.....elif else
接下来是python独特的
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8]

haveThree = False
for n in arr:
    if n == 3:
        haveThree = True
    break
if haveThree:
    print("有三")
else:
    print("没有三")

for n in arr:
    if n == 3:
        break
    print(n)
else:
    print("没有3")
print("有三")

from collections import deque

q = deque()
q.append(1)
while q:
    print(q)
    n = q.popleft()
    if n == 10:
        break
    q.append(n + 1)
    q.append(n + 5)
    ...
else:
    print("没有发生break")

# for else 语句是一种python特有的结构

try:
    a = 15
    a /= 5
except:
    # 发生错误之后执行代码
    ...
else:
    # 没有发生错误执行代码
    ...


# try:
#     ...
#
# else:
#     # try 后面必须跟except，不能缺少
#     ...