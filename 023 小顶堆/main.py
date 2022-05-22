import heapq

h = [i for i in range(10)]
h.reverse()
heapq.heapify(h)  # 这个函数没有返回值，直接传递列表改变列表
print(h)
for i in range(10):
    print(heapq.heappop(h))  # 每次弹出的时候都会维护一下小顶
    print(h)


#
# https://leetcode.cn/problems/qn8gGX/


# 序列比较默认比较的是第一个元素


