# 此算法用来实验a.py运行四次之后会变成多少行

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
