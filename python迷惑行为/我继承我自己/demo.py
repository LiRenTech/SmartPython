class MyClass:
    def __init__(self):
        self.x = 10

    pass


class MyClass(MyClass):
    def __init__(self):
        super().__init__()
        self.x = 11
        self.y = 20

    pass


a = MyClass()
print(a.x, a.y)
print(dir(a))

# 自己是可以扩展的
# 与字典类似
dic = {"a": 1, "b": 2}
# dic = dic | {"c": 3}
dic |= {"c": 3}
print(dic)


# 论如何说服你的团队成员学习并使用git
class int(int):
    def __new__(cls, x):
        res = super().__new__(cls, x)
        res.y = 20
        import random
        if random.random() < 0.01:
            res += 1
        return res

    pass


n = int("100")
print(n, type(n))

# 甚至可以把 int 给换掉
