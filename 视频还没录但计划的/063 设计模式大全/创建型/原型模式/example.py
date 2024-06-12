class A:
    def __init__(self, x):
        # ===
        # 这里中途可能花费了很大的时间复杂度用来计算出一个数值
        # ===
        self.x = x

    def build1(self):
        for i in range(10000000):
            self.x += 15

    def build2(self):
        for i in range(10000000):
            self.x += 20

    def clone(self):
        return A(self.x)


class B:

    def __init__(self, a):
        self.a = a

    def func(self):
        print(self.a)


"""
原型模式可能应用到的地方：
1. 性能优化：由于创建复杂对象时，原型模式可以减少创建对象的过程，从而提高性能。
地形生成、

2. 资源优化：由于创建复杂对象时，原型模式可以减少内存占用，从而节省系统资源。
和第一个差不多

3. 代码复用：由于创建复杂对象时，原型模式可以减少代码量，从而提高代码复用率。
子弹克隆


"""
