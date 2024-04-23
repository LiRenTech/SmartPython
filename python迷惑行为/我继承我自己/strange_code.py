class A:
    def __new__(cls, *args, **kwargs):
        return A


class A(A()()()(A(A(A(A(A)))))):
    pass

# 这样的写法可以迷惑人，让人误以为是无限递归，让抄作业的人看不懂，但是实际上是可以运行的