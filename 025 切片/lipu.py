class A:
    def __init__(self):
        self.val = [i for i in range(100)]

    def __getitem__(self, arg):
        print(arg)
        argType = type(arg)
        if argType == tuple:
            print(len(arg))
            res = self.val
            for item in arg:
                res = res[item]
            return res
        elif argType == slice:
            return self.val[arg]
        elif argType == int:
            return self.val[arg]
        else:
            print("不可以哦")

    def __str__(self):
        return f"{self.val}"


a = A()
# 我疯了
print(a[5, 5, "abc", (1, 2)])
# 我更离谱了
print(a[a])


