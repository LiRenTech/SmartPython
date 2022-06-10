# 二进制的应用，一个序列里的所有组合
# 暴力枚举算法
def test():
    doSomeThings = ["剪指甲", "哼歌", "拉粑粑", "喝水", "做扩胸运动", "嚼口香糖", "动耳朵", "嘴里含着人参"]
    print("start:", 0b0000000)  # 一个都不做
    print("end:", 0b1111111)  # 同时做
    for n in range((len(doSomeThings) + 1) ** 2):
        print(bin(n))
        string = bin(n)[2:]
        things = [doSomeThings[i] for i, char in enumerate(string) if char == "1"]
        print("一边".join(things))


# 其实可以用组合来做。
# from itertools import combinations

def test2():
    doSomeThings = ["剪指甲", "哼歌", "拉粑粑", "喝水", "做扩胸运动", "嚼口香糖", "动耳朵", "嘴里含着人参"]
    for n in range((len(doSomeThings) + 1) ** 2):
        # 00000000
        # 01011010
        things = []
        for i in range(len(doSomeThings)):
            res = n >> i & 1
            if res == 1:
                things.append(doSomeThings[i])
        print(" 同时 ".join(things))


# # 获取一个二进制所有位
# a = int("01011010", 2)
# print(a)
# for dig in range(8):
#     print(bin(a >> dig), a >> dig & 1)

test2()
