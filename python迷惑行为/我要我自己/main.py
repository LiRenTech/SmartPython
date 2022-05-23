from typing import *


class A:
    def __init__(self):
        self.val = [i for i in range(100)]

    def __iter__(self):
        for item in self.val:
            yield item

    def __getitem__(self, arg):
        arr = self.val
        if type(arg) is tuple:
            for item in arg:
                self.__getitem__(item)  # todo
        elif type(arg) is (int, slice):
            print(f"self.val[{arg}]")
            return self.val[arg]

    def __str__(self):
        return f"{self.val}"


a = A()
# 我疯了
# print(a[5, 5, "abc", (1, 2)])
# # 我更离谱了
# print(a[a])

print(a[1, 4, 5])

a.val = [[y] * 10 for y in range(10)]
print(a[1])
