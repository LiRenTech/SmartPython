# 暴力枚举算法
from itertools import combinations


def test():
    doSomeThings = ["剪指甲", "哼歌", "拉粑粑", "喝水", "做扩胸运动", "嚼口香糖", "动耳朵", "嘴里含着人参"]
    for i in range(1, 8 + 1):
        for item in combinations(doSomeThings, i):
            print(item)


test()
