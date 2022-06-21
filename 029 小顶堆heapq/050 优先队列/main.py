import queue

priQue = queue.PriorityQueue()
priQue.put([3, "赵"])
print(priQue.queue)
priQue.put([2, "钱"])
print(priQue.queue)
priQue.put([1, "孙"])
print(priQue.queue)
priQue.put([7, "李"])
print(priQue.queue)
priQue.put([5, "周"])
print(priQue.queue)
while priQue:
    print(priQue.get())
