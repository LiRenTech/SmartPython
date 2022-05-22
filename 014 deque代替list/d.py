from collections import deque
print(deque())
print(deque([]))
print(deque(()))
print(deque({}))
print(deque({1, 2, 3}))
print(deque([4, 5, 6]))
print(deque((7, 8, 9)))
print(deque({"a": 5, "b": 7}))

que = deque([1, 2, 3])
print(que)
print(que == [1, 2, 3])  # False
que.pop()
que.popleft()
que.append(999)
que.appendleft(666)
print(que)
