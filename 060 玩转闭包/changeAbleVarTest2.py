"""
闭包函数访问可变数据类型测试
可变数据类型变得复杂
"""


def f():
    a = [[1], [2]]
    g = []
    g.append(g)

    def v():
        print(a, id(a[0]), id(a[1]), id(g))

    return v


v1 = f()
v2 = f()

v1()
v2()
