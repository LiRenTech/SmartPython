# arr = [1, 2, 3, 4]
# arr2 = arr
# print(arr, arr2)
#
# arr[0] = 1000
#
# print(arr, arr2)

# 两个都变了


# arr = [1, 2, 3, 4]
# arr2 = arr.copy()
# print(arr, arr2)
#
# arr[0] = 1000
#
# print(arr, arr2)
#
# # 可以了，但是还有隐患

# arr = [1, 2, 3, 4]
# # arr2 = arr[::]  # 不至于，看着像腹肌
# arr2 = arr[:]
# print(arr, arr2)
#
# arr[0] = 1000
#
# print(arr, arr2)

# arr = [[1, 2, 3], 4, 5]
# arr2 = arr.copy()
# print(arr, arr2)
# arr[1] *= 2
# print(arr, arr2)
# # ok
# arr[0].clear()
# print(arr, arr2)
# # no no no

# arr = [[1, 2, 3], 4, 5]
# arr2 = arr[:]
# print(arr, arr2)
# arr[1] *= 2
# print(arr, arr2)
# # ok
# arr[0].clear()
# print(arr, arr2)
# # no no no 也不行的


import copy

# arr = [[1, 2, 3], 4, 5]
# arr2 = copy.copy(arr)
# arr[0].clear()
# print(arr, arr2)


arr = [[1, 2, 3], 4, 5]
arr2 = copy.deepcopy(arr)
arr[0].clear()
print(arr, arr2)
