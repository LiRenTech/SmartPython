class A:
    def __init__(self, arg):
        self.lst = [arg]
        self.val = A

    def __str__(self):
        return str(self.lst)

    def __lshift__(self, other):
        print(other, end=" ")
        return self

    __repr__ = __str__


endl = "\n"

cout = A(1).val(2).val(3).val(4).val(5).val(6).val(7)
cout << 5 << 5 << endl


class Int(int):
    def __init__(self, n=0):
        self.n = n

    def __pos__(self):
        self.n += 1
        return Int(self.n)

    def __str__(self):
        return self.n


a = Int()
for _ in range(1000):
    ++a
print(a)
