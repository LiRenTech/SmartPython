arr = []


def f():
    arr.append(f)
    return arr


f()[0]()[1]()[-1]()[2]()[3]()

print(arr)
print(len(arr))

lst = []


def g(array):
    array.append(array)
    return g


g(lst)(lst)(lst)


