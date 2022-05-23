def robot(obj):
    obj.b = 155
    return obj


@robot
class A:
    def __init__(self):
        self.a = None


a1 = A()
print(a1.a)
print(a1.b)
