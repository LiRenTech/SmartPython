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

    def __str__(self):
        return f"{self.val}"


a = A()
# print(a)
print(a[:5])
# print(a[5:10, :])
# 多重切片
print(a[5:, 5:, 5:])
