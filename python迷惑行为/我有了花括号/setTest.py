from random import randint


class MyObj:
    index = 0

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    __repr__ = __str__

    def __hash__(self):
        # MyObj.index += 1
        # return MyObj.index
        return randint(1, 100000)


s = {MyObj("a"), MyObj("c"), MyObj("e")}
print(s)
for item in s:
    print(item)
# {a, c, e}

s2 = set()
s2.add(MyObj("a"))
s2.add(MyObj("c"))
s2.add(MyObj("e"))
print(s2)

for item in s2:
    print(item)
