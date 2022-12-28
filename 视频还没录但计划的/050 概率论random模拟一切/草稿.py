from random import *
from typing import Sequence


class Arr(Sequence):
    def __init__(self):
        self.arr = []

    def push(self, n):
        self.arr.append(n)

    def __getitem__(self, item):
        return self.arr[item]

    def __len__(self):
        return len(self.arr)


a = Arr()
a.push(12)
a.push(11)
a.push(1111)
print(choice(a))

# ============

array1 = [1, 2, 3, 4, 5]
for i in reversed(range(1, len(array1))):
    print(i)

print(sample({i for i in range(1000)}, 5))
print(sample(list(range(1000)), 5))

# ===========

print("=" * 20)
for _ in range(100):
    print(uniform(1000, 900))

# ========
print(randrange(5))

