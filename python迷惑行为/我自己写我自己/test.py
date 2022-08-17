arr = [1]


def run():
    global arr
    cacheLen = len(arr)
    for _ in range(cacheLen):
        arr += arr.copy()


run()
print(len(arr))
run()
print(len(arr))
run()
print(len(arr))
