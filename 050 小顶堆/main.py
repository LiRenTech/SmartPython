import heapq
from random import randint

h = [-randint(1, 100) for _ in range(8)]
print(h)
heapq.heapify(h)  # 这个函数没有返回值，直接传递列表改变列表
print(h)
while h:
    a = -heapq.heappop(h)
    print(a)
    # print(h)

#
# https://leetcode.cn/problems/qn8gGX/


# 序列比较默认比较的是第一个元素

print(heapq.nlargest(2, [1, 2, 3, 4, 5, 3, 2, 1]))
