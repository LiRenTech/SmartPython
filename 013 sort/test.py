arr2 = [(1, 2), (2, 2), (5, 0)]

from functools import cmp_to_key


def cmp(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        if a[1] > b[1]:
            return 1
        elif a[1] < b[1]:
            return -1
        else:
            return 0


from random import randint

arr3 = [(randint(1, 100), randint(1, 100)) for _ in range(100)]
arr3.sort(key=cmp_to_key(cmp), reverse=True)
print(arr3)
