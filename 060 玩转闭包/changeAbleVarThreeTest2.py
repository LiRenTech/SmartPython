"""
闭包函数访问可变数据类型测试
可变数据类型变得复杂
嵌套三层
"""


def f():
    a1 = []

    def g():
        a2 = [a1]

        def h():
            print(a2, id(a2), id(a2[0]))
            return a2

        return h

    return g


# ============

g1 = f()
h1 = g1()
h1().append(111)
h1()[0].append(222)
h1()
print(h1.__closure__)

g2 = f()
h2 = g2()
h2()
print(h2.__closure__)
