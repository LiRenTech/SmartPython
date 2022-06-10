from functools import cmp_to_key

arr = [3, 1, 4, 1, 5, 9, 2, 6]

# 区别
# sorted(arr)
# arr.sort()

arr2 = [(1, 2), (2, 2), (5, 0)]

arr2.sort(key=lambda item: item[0], reverse=True)
print(arr2)
arr2.sort(key=lambda item: item[1], reverse=True)
print(arr2)


def cmp(a, b):
    # return 1 表示 a 应该比 b 大
    # return -1 表示 b 比 a 大
    # return 0 表示 一样大
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

print(arr3)
print(sorted(arr3, key=cmp_to_key(cmp)))
