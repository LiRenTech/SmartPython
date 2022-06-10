lines = 1


def run():
    global lines
    cacheLen = lines
    for _ in range(cacheLen):
        lines += lines


run()  # 2
run()  # 8
run()  # 2048
run()  # 10 ^ 620
print(lines)
