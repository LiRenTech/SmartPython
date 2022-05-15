arr = [1, 2, 4, 5]
for i, n in enumerate(reversed(arr)):
    # print(i, n)
    ...
for i, n in reversed(list(enumerate(arr))):
    print(i, n)
