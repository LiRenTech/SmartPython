from queue import PriorityQueue
import heapq

arr = [1, 3, 4, 6, 2, 5, 6, 8, 3, 2]
print(arr)
heapq.heapify(arr)
print(arr)
a = heapq.heappop(arr)
print(arr)
heapq.heappush(arr, 5)
print(arr)

q = PriorityQueue()
q.put(1)
q.put(3)
q.put(4)
q.put(6)
q.put(5)
print(q.queue)
q.get()
print(q.queue)

# ======= 速度测试
print("=" * 100)



