class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)

r"""
         1
      /     \
    2        3
  /   \
4       5

"""

root.left = n1
root.right = n2
n1.left = n3
n1.right = n4


def dfs(node):
    if not node:
        return
    # 这里是先序遍历，可以顺便把剩下三种方法都讲了
    print(node.val)
    dfs(node.left)
    dfs(node.right)


# dfs(root)


def bfs():
    q = [(root, 0)]
    while q:
        node, level = q.pop(0)
        if node is None:
            continue
        print(node.val)
        q.append((node.left, level + 1))
        q.append((node.right, level + 1))


# bfs()

from collections import deque


def bfsFast():
    q = deque([(root, 0)])
    while q:
        node, level = q.popleft()
        if node is None:
            continue
        print(node.val)
        q.append((node.left, level + 1))
        q.append((node.right, level + 1))


bfsFast()

# =====

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
